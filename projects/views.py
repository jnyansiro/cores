from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import User, Member, Project,Viewpoint
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {})
    indexhead = "Dashboard"
    return render(request, "index.html", {"indexhead": indexhead})


def profile(request):
    indexhead = "User Profile"
    user_id = request.user.id
    print(user_id)
    member_details = Member.objects.get(user=user_id)
    print(member_details)
    return render(
        request,
        "user/profile.html",
        {"member_details": member_details, "indexhead": indexhead},
    )


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return index(request)
            message = "sorry your account is inactive communicate with your Admin"
            return render(request, "login.html", {"message": message})
        message = "Soory you have entered incorrect credentials"
        return render(request, "login.html", {"message": message})
    return render(request, "login.html", {})


def logout(request):
    auth_logout(request)
    return render(request, "login.html", {})


def registration(request):
    if request.method == "POST":

        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        first_name = request.POST.get("first_name", None)
        second_name = request.POST.get("second_name", None)
        last_name = request.POST.get("last_name", None)
        gender = request.POST.get("gender", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get("password1", None)
        if password == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    email=email, username=username, password=password
                )
                user.save()
                if user:
                    member = Member.objects.create(
                        user=user,
                        email=email,
                        first_name=first_name,
                        middle_name=second_name,
                        surname=last_name,
                        phone=phone,
                        gender=gender,
                    )
                    member.save()
                    if member:
                        reg_message = (
                            "you have successfully create an account login now"
                        )
                        return render(
                            request, "login.html", {"reg_message": reg_message}
                        )
                    message = "sorry failed to create an account please try again after 5 menutes"
                    return render(request, "registration.html", {"message": message})
            message = (
                "sorry Username already taken please use another different Username"
            )
            return render(request, "registration.html", {"message": message})
        message = "sorry password did not match, enter it correctly"
        return render(request, "registration.html", {"message": message})
    return render(request, "registration.html", {})


def forgetpassword(request):
    return render(request, "password_recover.html", {})


def pagenotfound(request, exception):

    return render(request, "pagenotfound.html", {})


def servererror(request):

    return render(request, "pagenotfound.html", {})


# project views
def createProject(request):
    if request.method == "POST":
        project_title = request.POST.get("project_title")
        sector = request.POST.get("sector")
        due_date = request.POST.get("due_date")
        project_photo = request.FILES.get("project_photo")
        project_files = request.FILES.get("project_docs")
        project_visibility = request.POST.get("visibility")
        is_public = request.POST.get("participation")
        is_discoverable = request.POST.get("participation")
        is_invitational = request.POST.get("participation")
        project_description = request.POST.get("project_description")

        if not empty(is_discoverable):
            is_discoverable = True
        else:
            is_discoverable = False

        if not empty(is_invitational):
            is_invitational = True
        else:
            is_invitational = False

        if not empty(is_public):
            is_public = True
        else:
            is_public = False
        # getting member who create of project
        member = Member.objects.get(user=request.user.id)
        print(member)
        project = Project.objects.create(
            created_by=member,
            project_title=project_title,
            project_visibility=project_visibility,
            is_public=is_public,
            is_discoverable=is_discoverable,
            is_invitational=is_invitational,
            description=project_description,
            due_date=due_date,
        )
        project.save()
        if project:
            myProjects = Project.objects.filter(created_by=member).order_by(-id)
            indexhead = "Projects / My Project(s)"
            return render(
                request,
                "myproject.html",
                {"myprojects": myProjects, "indexhead": indexhead},
            )

    indexhead = "Project / Create-Project"
    hidesearch = "hide"
    return render(
        request,
        "projects/my_projects/create_project.html",
        {"indexhead": indexhead, "hidesearch": hidesearch},
    )


def myProjects(request):
    indexhead = "Projects / My Project(s)"
    return render(
        request, "projects/my_projects/myproject.html", {"indexhead": indexhead}
    )

def viewMyproject(request):
    indexhead = "Projects / My Project(s)"
    hidesearch = "hide"
    return render(
        request, "projects/my_projects/view_myproject.html", {"indexhead": indexhead,'hidesearch':hidesearch}
    )


def viewProject(request):
    indexhead = "project Title"
    hidesearch = "hide"
    return render(
        request,
        "projects/other_projects/view_project.html",
        {"indexhead": indexhead, "hidesearch": hidesearch},
    )


def projectMembers(request):
    indexhead = "Projects / Project-Members"
    member_details = Member.objects.all()
    
    return render(
        request,
        "projects/my_projects/project_members.html",
        {"indexhead": indexhead, "member_details": member_details},
    )


def memberRequest(request):
    indexhead = "Project / Member Requests"
    
    return render(
        request, "projects/my_projects/member_request.html", {"indexhead": indexhead}
    )


def inviteMember(request):
    indexhead = "Project / Invite Members"

    return render(
        request, "projects/my_projects/member_request.html", {"indexhead": indexhead}
    )


def projects(request):
    indexhead = "Projects"

    return render(
        request, "projects/other_projects/projects.html", {"indexhead": indexhead}
    )


def viewpoint(request):
    indexhead = "Project - ViewPoint"
    hidesearch = "hide"
    return render(
        request, "projects/viewpoints/viewpoint.html", {"indexhead": indexhead,'hidesearch':hidesearch}
    )


def createViewpoint(request):
    if request.method == 'POST':
        viewpoint_title = request.POST.get('viewpoint_title')
        links = request.POST.get('links')
        viewpoint_photo = request.FILES.get('viewpoint_photo')
        viewpoint_docs = request.FILES.get('viewpoint_docs')
        viewpoint_descriptions = request.POST.get('viewpoint_descriptions')

        # getting member who to create a viewpoint
        user_id = request.user.id
        member = Member.objects.get(user=user_id)
        project = Project.objects.all()[0]
        print(project)

        viewpoint = Viewpoint.objects.create(
            project = project,
            created_by = member,
            viewpoint_name = viewpoint_title,
            viewpoint_links= links,
            viewpoint_photo = viewpoint_photo,
            viewpoint_docs = viewpoint_docs,
            description = viewpoint_descriptions
        )
        viewpoint.save()
        if viewpoint:
            allviewpoints = Viewpoint.objects.all().order_by(-id)
            indexhead = "Project - ViewPoint"
            hidesearch = "hide"
            return render(request,"viewpoint.html",{"indexhead": indexhead,'hidesearch':hidesearch,'allviewpoints':allviewpoints})
    
    indexhead = "Project - Create ViewPoint"
    hidesearch = "hide"
    return render(
        request, "projects/viewpoints/create_viewpoint.html", {"indexhead": indexhead,'hidesearch':hidesearch}
    )


def goals(request):
    indexhead = "Viewpoint-Goals"
    return render(request, "projects/Goals/goals.html", {"indexhead": indexhead})


def viewGoal(request):
    indexhead = "Goal Description"
    return render(request, "projects/Goals/view_goal.html", {"indexhead": indexhead})


def createGoal(request):
    indexhead = "Create Goal"
    return render(request, "projects/Goals/create_goal.html", {"indexhead": indexhead})


def requirements(request):
    indexhead = "Goal-Requirements"
    return render(
        request, "projects/requirements/requirements.html", {"indexhead": indexhead}
    )


def viewrequirement(request):
    indexhead = "Requirement Description"
    return render(
        request, "projects/requirements/view_requirement.html", {"indexhead": indexhead}
    )


def createRequirement(request):
    indexhead = "Create Requirement"
    return render(
        request,
        "projects/requirements/create_requirement.html",
        {"indexhead": indexhead},
    )


def scenarios(request):
    indexhead = "Requirement-Scenarios"
    return render(request, "projects/scenario/scenarios.html", {"indexhead": indexhead})


def viewscenario(request):
    indexhead = "Scenario Description"
    return render(
        request, "projects/scenario/view_scenario.html", {"indexhead": indexhead}
    )


def createScenario(request):
    indexhead = "Create Scenario"
    return render(
        request, "projects/scenario/create_scenario.html", {"indexhead": indexhead}
    )


def processes(request):
    indexhead = "Scenario-Processes"
    return render(request, "projects/process/process.html", {"indexhead": indexhead})


def viewprocess(request):
    indexhead = "Process Description"
    return render(
        request, "projects/process/view_process.html", {"indexhead": indexhead}
    )


def createProcess(request):
    indexhead = "Create Process"
    return render(
        request, "projects/process/create_process.html", {"indexhead": indexhead}
    )


def usecases(request):
    indexhead = "Process-Usecases"
    return render(request, "projects/usecase/usecases.html", {"indexhead": indexhead})


def viewusecase(request):
    indexhead = "Usecase Description"
    return render(
        request, "projects/usecase/view_usecase.html", {"indexhead": indexhead}
    )


def createUsecase(request):
    indexhead = "Create Usecase"
    return render(
        request, "projects/usecase/create_usecase.html", {"indexhead": indexhead}
    )
