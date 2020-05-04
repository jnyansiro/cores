from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import (
    User,
    Member,
    Project,
    Viewpoint,
    Sector,
    Goal,
    Comment,
    ProjectComment,
    ProjectMembership,
    Requirement,
    Scenario,
    Process,
    UseCase
)
from django.core.files.storage import FileSystemStorage


# Create your views here.
def indexsss(request):
    return render(request,'web/index.html',{})

def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {})
    indexhead = "Dashboard"
    current_projects = Project.objects.all().order_by("-id")[:6]
    total_projects = Project.objects.all().count()
    members = Member.objects.all().count()
    member = Member.objects.get(user=request.user)
    request.session["userphoto"] = str(member.profile_photo)
    profilephoto = request.session["userphoto"]
    print(request.session["userphoto"])
    hidesearch = "hide"
    return render(
        request,
        "index.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "current_projects": current_projects,
            "profilephoto": profilephoto,
            "total_projects": total_projects,
            'member':member,
            'members':members
        },
    )


def filterProject(request,project_id,page):
    if page == "viewpoint":
        pass


    



# user profile function
def profile(request):
    indexhead = "User Profile"
    member = Member.objects.get(user=request.user)
    user_id = request.user.id
    print(user_id)
    hidesearch = "hide"
    member_details = Member.objects.get(user=user_id)
    print(member_details)
    return render(
        request,
        "user/profile.html",
        {
            "member_details": member_details,
            "indexhead": indexhead,
            'member':member,
            "hidesearch": hidesearch,
        },
    )


# login function
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


# user logout
def logout(request):

    # builtin function for session destroy
    auth_logout(request)
    return render(request, "login.html", {})


def registration(request):
    if request.method == "POST":

        # Taking values from html page so as to save to the database
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        first_name = request.POST.get("first_name", None)
        second_name = request.POST.get("second_name", None)
        last_name = request.POST.get("last_name", None)
        gender = request.POST.get("gender", None)
        password = request.POST.get("password", None)
        password2 = request.POST.get("password1", None)

        # checking if password match
        if password == password2:
            if not User.objects.filter(username=username).exists():

                # creating user first
                user = User.objects.create_user(
                    email=email, username=username, password=password
                )

                # saving user details to the database
                user.save()
                if user:
                    # then creating member of the system
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
    member = Member.objects.get(user=request.user.id)
    if request.method == "POST":
        project_title = request.POST.get("project_title")
        sector = request.POST.get("sector")
        due_date = request.POST.get("due_date")
        project_photo = request.FILES.get("project_photo")
        project_files = request.FILES.get("project_docs")
        project_visibility = request.POST.get("visibility")
        # is_public = request.POST.get("participation")
        project_participation = request.POST.get("participation")
        print(project_participation)
        # is_invitational = request.POST.get("participation")
        project_description = request.POST.get("project_descriptions")

        # getting member who create of project
        member = Member.objects.get(user=request.user.id)
        project = Project.objects.create(
            created_by=member,
            project_photo=project_photo,
            project_files=project_files,
            project_title=project_title,
            project_visibility=project_visibility,
            description=project_description,
            due_date=due_date,
        )
        project.save()

        if project:
            project_membership = ProjectMembership.objects.create(
                project=project, member=member, member_role="Admin", status="active"
            )
            project_membership.save()
            indexhead = "Projects / My Project(s)"
            member = Member.objects.get(user=request.user)
            myProject = Project.objects.filter(created_by=member).order_by("-id")
            return myProjects(request)

    indexhead = "Project / Create-Project"
    hidesearch = "hide"
    sectors = Sector.objects.all().order_by("sector_name")
    print("sectors")
    return render(
        request,
        "projects/my_projects/create_project.html",
        {"indexhead": indexhead, "hidesearch": hidesearch, "sectors": sectors,'member':member},
    )


def editProject(request, project_id):
    indexhead = "Project / Create-Project"
    hidesearch = "hide"
    project = Project.objects.get(id=project_id)
    sectors = Sector.objects.all().order_by("sector_name")
    member = Member.objects.get(user=request.user)
    print("sectors")
    return render(
        request,
        "projects/my_projects/edit_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "sectors": sectors,
            "project": project,
            'member':member,
        },
    )


def deleteProject(request, project_id):
    delete_project = Project.objects.get(id=project_id).delete()
    if delete_project:
        return myProjects(request)


def createProjectComment(request, project_id):
    indexhead = "Project Details"
    hidesearch = "hide"
    
    if request.method == "POST":
        comment = request.POST.get("comment")
        project = project_id
        member = Member.objects.get(user=request.user)

        #    then creating comment then ProjectComment
        comment_data = Comment.objects.create(comment=comment, commented_by=member)
        comment_data.save()
        if comment_data:
            project = Project.objects.get(id=project)
            project_comment = ProjectComment.objects.create(
                comment=comment_data, project=project
            )
            project_comment.save()
            if project_comment:
                comments = ProjectComment.objects.filter(project=project)
                return viewProject(request, project_id=project_id)
    return viewProject(request, project_id=project_id)


def projectIncentive(request, project_id=None):
    hidesearch = "hide"
    return render(
        request,
        "projects/my_projects/project_incentive.html",
        {"hidesearch": hidesearch, "project_id": project_id},
    )


def myProjects(request):
    indexhead = "Projects / My Project(s)"
    member = Member.objects.get(user=request.user)
    myProject = Project.objects.filter(created_by=member).order_by("-id")
    return render(
        request,
        "projects/my_projects/myproject.html",
        {"indexhead": indexhead, "myProject": myProject,'member':member},
    )


def viewMyproject(request, project_id):
    indexhead = "Projects / My Project Details"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    comments = ProjectComment.objects.filter(project=project).order_by("-id")
    total_comments = comments.count()
    hidesearch = "hide"
    project_id
    return render(
        request,
        "projects/my_projects/view_myproject.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project": project,
            "comments": comments,
            "total_comments": total_comments,
            "project_id": project_id,
            'member':member

        },
    )


def viewProject(request, project_id):
    indexhead = "Project Details"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    comments = ProjectComment.objects.filter(project=project).order_by("-id")
    total_comments = comments.count()

    return render(
        request,
        "projects/other_projects/view_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project": project,
            "comments": comments,
            "total_comments": total_comments,
            'member':member
        },
    )


def projectMembers(request, project_id=None):
    indexhead = "Projects / Project-Members"
    member = Member.objects.get(user=request.user)
    project_member = ProjectMembership.objects.filter(project=project_id)
    placeholder = "search member"

    return render(
        request,
        "projects/my_projects/project_members.html",
        {
            "indexhead": indexhead,
            "project_member": project_member,
            "placeholder": placeholder,
            "project_id": project_id,
            'member':member
        },
    )


def memberRequest(request, project_id):
    indexhead = "Project / Member Requests"
    member = Member.objects.get(user=request.user)

    return render(
        request,
        "projects/my_projects/member_request.html",
        {"indexhead": indexhead, "project_id": project_id,'member':member},
    )


def inviteMember(request, project_id=None):
    indexhead = "Project / Invite Members"
    member = Member.objects.get(user=request.user)

    return render(
        request, "projects/my_projects/member_request.html", {"indexhead": indexhead,'member':member}
    )


def projects(request):
    indexhead = "Projects"
    member = Member.objects.get(user=request.user)
    projects = Project.objects.all().order_by("-id")

    return render(
        request,
        "projects/other_projects/projects.html",
        {"indexhead": indexhead, "projects": projects,'member':member},
    )


def viewpoint(request, project_id=None, viewpoint_id=None):
    indexhead = "Project - ViewPoint"
    hidesearch = "hide"
    
    member = Member.objects.get(user=request.user)
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/viewpoint.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoint": viewpoint,
            "viewpoints": viewpoints,
            "project_id": project_id,
            'member':member
            ,'project':project
        },
    )


def viewpoints(request, project_id):
    
    indexhead = "Project - ViewPoint"
    project = Project.objects.get(id=project_id)
    hidesearch = "hide"
    projects = Project.objects.all().order_by('-id')
    if request.method == 'POST':
        project_id = request.POST.get('project')
        member = Member.objects.get(user=request.user)
        viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")[:4]
        viewpoints = Viewpoint.objects.filter(project=project_id).order_by("-id")
        project_id = project_id
        return render(
            request,
            "projects/viewpoints/viewpoints.html",
            {
                "indexhead": indexhead,
                "hidesearch": hidesearch,
                "viewpoint": viewpoint,
                "viewpoints": viewpoints,
                "project_id": project_id,
                'member':member,
                'project':project
                ,'projects':projects
            },
        )


    member = Member.objects.get(user=request.user)
    viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")[:4]
    viewpoints = Viewpoint.objects.filter(project=project_id).order_by("-id")
    project_id = project_id
    return render(
        request,
        "projects/viewpoints/viewpoints.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoint": viewpoint,
            "viewpoints": viewpoints,
            "project_id": project_id,
            'member':member,
            'project':project
            ,'projects':projects
        },
    )


def createViewpoint(request, project_id):
    if request.method == "POST":
        viewpoint_title = request.POST.get("viewpoint_title")
        links = request.POST.get("links")
        viewpoint_photo = request.FILES.get("viewpoint_photo")
        viewpoint_docs = request.FILES.get("viewpoint_docs")
        viewpoint_descriptions = request.POST.get("viewpoint_descriptions")
        project_id = project_id

        # getting member who to create a viewpoint
        user_id = request.user.id
        member = Member.objects.get(user=user_id)
        project = Project.objects.get(id=project_id)

        viewpoint = Viewpoint.objects.create(
            project=project,
            created_by=member,
            viewpoint_name=viewpoint_title,
            viewpoint_links=links,
            viewpoint_photo=viewpoint_photo,
            viewpoint_docs=viewpoint_docs,
            description=viewpoint_descriptions,
        )
        viewpoint.save()
        if viewpoint:
            viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")[:4]
            viewpoints = Viewpoint.objects.filter(project=project_id).order_by("-id")
            indexhead = "Project - ViewPoint"
            hidesearch = "hide"
            return render(
                request,
                "projects/viewpoints/viewpoints.html",
                {
                    "indexhead": indexhead,
                    "hidesearch": hidesearch,
                    "viewpoints": viewpoints,
                    "viewpoint": viewpoint,
                    "project_id": project_id,
                    'member':member,
                    'project':project
                },
            )

    indexhead = "Project -ViewPoints"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/viewpoints/create_viewpoint.html",
        {"indexhead": indexhead, "hidesearch": hidesearch, "project_id": project_id,'member':member},
    )


def goals(request, project_id=None, viewpoint_id=None):
    indexhead = "Viewpoint-Goals"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        viewpoint = request.POST.get("viewpoint_id")
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoint = Viewpoint.objects.get(id=viewpoint)
        project = Project.objects.get(project_title=viewpoint.project)
        viewpointiees = Viewpoint.objects.filter(project=project.id).order_by("-id")
        viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")

        viewpoint_id = viewpoint_id
        return render(
            request,
            "projects/Goals/goals.html",
            {
                "indexhead": indexhead,
                "goals": goals,
                "viewpoints": viewpoints,
                "viewpoint_id": viewpoint_id,
                "viewpointiees": viewpointiees,
                'member':member,
                'project':project
            },
        )
    goals = Goal.objects.filter(viewpoint=viewpoint_id).order_by("-id")
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(id=viewpoint.project.id)
    viewpointiees = Viewpoint.objects.filter(project=project.id).order_by("-id")
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    viewpoint_id = viewpoint_id
    return render(
        request,
        "projects/Goals/goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "viewpoints": viewpoints,
            "viewpoint_id": viewpoint_id,
            "viewpointiees": viewpointiees,
            'member':member,
            'project':project
        },
    )


def viewGoal(request, goal_id):
    indexhead = "Goal Description"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        goal = request.POST.get("goal")
        goal = Goal.objects.get(id=goal)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        goals = Goal.objects.filter(viewpoint=viewpoint).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        return render(
            request,
            "projects/Goals/view_goal.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "viewpoint_id": viewpoint_id,
                "project_id": project_id,
                "goal_id": goal_id,
                "viewpoints": viewpoints,
                "goals": goals,
                'member':member,
                'project':project
            },
        )

    goal = Goal.objects.get(id=goal_id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    goals = Goal.objects.filter(viewpoint=viewpoint).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    return render(
        request,
        "projects/Goals/view_goal.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            "viewpoint_id": viewpoint_id,
            "project_id": project_id,
            "goal_id": goal_id,
            "viewpoints": viewpoints,
            "goals": goals,
            'member':member,
            'project':project
        },
    )


def createGoal(request, viewpoint_id):
    indexhead = "Create Goal"
    member = Member.objects.get(user=request.user)
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == "POST":
        goal_name = request.POST.get("goal_title")
        goal_photo = request.FILES.get("goal_photo")
        goal_link = request.POST.get("goal_link")
        goal_docs = request.FILES.get("goal_docs")
        description = request.POST.get("description")
        category = request.POST.get("category")
        created_by = Member.objects.get(user=request.user)
        viewpoint = viewpoint

        # then creating goal
        goal = Goal.objects.create(
            goal_name=goal_name,
            goal_photo=goal_photo,
            goal_link=goal_link,
            goal_docs=goal_docs,
            description=description,
            category=category,
            created_by=created_by,
            viewpoint=viewpoint,
        )
        goal.save()
        if goal:

            goals = Goal.objects.filter(viewpoint=viewpoint_id).order_by("-id")
            viewpoint = Viewpoint.objects.get(id=viewpoint_id)
            project = Project.objects.get(id=viewpoint.project.id)
            viewpointiees = Viewpoint.objects.filter(project=project.id).order_by("-id")

            viewpoint_id = viewpoint_id
            return render(
                request,
                "projects/Goals/goals.html",
                {
                    "indexhead": indexhead,
                    "goals": goals,
                    "viewpoint_id": viewpoint_id,
                    "viewpoints": viewpoints,
                    "viewpointiees": viewpointiees,
                    'member':member,
                    'project':project
                },
            )

    return render(
        request,
        "projects/Goals/create_goal.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "viewpoints": viewpoints,
            'member':member,
            'project':project
        },
    )


def requirements(request, goal_id):
    indexhead = "Goal-Requirements"
    member = Member.objects.get(user=request.user)
    if request.method == 'POST':
        goal_id = request.POST.get('goal')
        goal = Goal.objects.get(id=goal_id)
        requirements = Requirement.objects.filter(goal=goal)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
        project_id = project.id
        return render(
            request,
            "projects/requirements/requirements.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal_id,
                "project_id": project_id,
                "requirements": requirements,
                "viewpoints": viewpoints,
                "goals": goals,
                'member':member,
                'project':project
            },
        )


    goal = Goal.objects.get(id=goal_id)
    requirements = Requirement.objects.filter(goal=goal)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    goals = Goal.objects.filter(viewpoint=viewpoint)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal_id,
            "project_id": project_id,
            "requirements": requirements,
            "viewpoints": viewpoints,
            "goals": goals,
            'member':member,
            'project':project
        },
    )


def viewrequirement(request, requirement_id=None):
    indexhead = "Requirement Description"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        requirement = request.POST.get("requirement")
        requirement=Requirement.objects.get(id=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        return render(
            request,
            "projects/requirements/view_requirement.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "viewpoint_id": viewpoint_id,
                "project_id": project_id,
                "goal_id": goal.id,
                "viewpoints": viewpoints,
                "requirements": requirements,
                'requirement':requirement
                ,'member':member,
                'project':project
            },
        )
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    return render(
        request,
        "projects/requirements/view_requirement.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            "viewpoint_id": viewpoint_id,
            "project_id": project_id,
            "goal_id": goal.id,
            "viewpoints": viewpoints,
            "requirements": requirements,
            'requirement':requirement
            ,'member':member,
            'project':project
        },
    )



def createRequirement(request, goal_id):
    indexhead = "Create Requirement"
    member = Member.objects.get(user=request.user)
    goal = Goal.objects.get(id=goal_id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == 'POST':
        requirement_title = request.POST.get('requirement_title')
        requirement_link = request.POST.get('link')
        requirement_photo = request.FILES.get('requirement_photo')
        requirement_docs = request.FILES.get('requirement_docs')
        description = request.POST.get('requirement_descriptions')
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        requirement = Requirement.objects.create(
            name=requirement_title,
            requirement_photo=requirement_photo,
            requirement_links=requirement_link,
            created_by=created_by,
            requirement_docs=requirement_docs,
            description=description,
            goal=goal
        )
        requirement.save()
        if requirement:
            indexhead = "Goal-Requirements"
            requirements = Requirement.objects.filter(goal=goal).order_by('-id')
            return render(
            request,
            "projects/requirements/requirements.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal_id,
                "project_id": project_id,
                "requirements": requirements,
                "viewpoints": viewpoints,
                "goals": goals,
                'member':member,
                'project':project
            },
            )


    return render(
        request,
        "projects/requirements/create_requirement.html",
        {"indexhead": indexhead,'goal_id':goal_id,'viewpoints':viewpoints,'member':member},
    )


def scenarios(request,requirement_id):
    indexhead = "Requirement-Scenarios"
    member = Member.objects.get(user=request.user)
    if request.method == 'POST':
        requirement_id = request.POST.get('requirement')
        requirement = Requirement.objects.get(id=requirement_id )
        goal = Goal.objects.get(id=requirement.goal.id)
        requirements = Requirement.objects.filter(goal=goal)
        scenarios = Scenario.objects.filter(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
        project_id = project.id
        return render(
            request,
            "projects/scenario/scenarios.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                "viewpoints": viewpoints,
                'scenarios':scenarios,
                "goals": goals,
                'requirement_id':requirement_id
                ,'member':member,
                'project':project
            },
        )


    requirement = Requirement.objects.get(id=requirement_id )
    goal = Goal.objects.get(id=requirement.goal.id)
    requirements = Requirement.objects.filter(goal=goal)
    scenarios = Scenario.objects.filter(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    goals = Goal.objects.filter(viewpoint=viewpoint)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    return render(
        request,
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            'scenarios':scenarios,
            "viewpoints": viewpoints,
            "goals": goals,
            'requirement_id':requirement_id
            ,'member':member,
            'project':project
        },
    )



def viewscenario(request,scenario_id):
    indexhead = "Scenario Description"
    member = Member.objects.get(user=request.user)

    if request.method == "POST":
        scenario_id = request.POST.get("scenario")
        scenario = Scenario.objects.get(id=scenario_id)
        requirement=Requirement.objects.get(id=scenario.requirement.id)
        scenarios = Scenario.objects.filter(requirement=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        return render(
            request,
            "projects/scenario/view_scenario.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "scenario": scenario,
                "viewpoint_id": viewpoint_id,
                "project_id": project_id,
                "goal_id": goal.id,
                'scenarios':scenarios,
                "viewpoints": viewpoints,
                "requirements": requirements,
                'requirement_id':requirement.id
                ,'member':member,
                'project':project
            },
        )
    scenario = Scenario.objects.get(id=scenario_id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    return render(
        request,
        "projects/scenario/view_scenario.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            'scenario':scenario,
            "viewpoint_id": viewpoint_id,
            "project_id": project_id,
            "goal_id": goal.id,
            "viewpoints": viewpoints,
            'scenarios':scenarios,
            "requirements": requirements,
            'requirement_id':requirement.id
            ,'member':member,
            'project':project
        }
    )


def createScenario(request,requirement_id):
    indexhead = "Create Scenario"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == 'POST':
        scenario_title = request.POST.get('scenario_title')
        scenario_link = request.POST.get('link')
        scenario_photo = request.FILES.get('scenario_photo')
        scenario_docs = request.FILES.get('scenario_docs')
        description = request.POST.get('scenario_descriptions')
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        scenario = Scenario.objects.create(
            name=scenario_title,
            scenario_photo=scenario_photo,
            scenario_links=scenario_link,
            created_by=created_by,
            scenario_docs=scenario_docs,
            description=description,
            requirement=requirement
        )
        scenario.save()
        if scenario:
            indexhead = "Requirements-Scenarios:"
            requirements = Requirement.objects.filter(goal=goal).order_by('-id')
            scenarios = Scenario.objects.filter(requirement=requirement).order_by('-id')
            return render(
            request,
            "projects/scenario/scenarios.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                'requirement_id':requirement.id,
                'scenarios':scenarios,
                "viewpoints": viewpoints,
                "goals": goals,
                'member':member,
                'project':project
            }
            )
    return render(
        request,
        "projects/scenario/create_scenario.html",
        {"indexhead": indexhead,'requirement_id':requirement_id,'viewpoints':viewpoints,'member':member},
    )


def processes(request, scenario_id):
    indexhead = "Scenario-Processes"
    member = Member.objects.get(user=request.user)
    if request.method == 'POST':
        scenario_id = request.POST.get('scenario')
        scenario = Scenario.objects.get(id=scenario_id)
        processes = Process.objects.filter(scenario=scenario)
        requirement = Requirement.objects.get(id=scenario.requirement.id )
        goal = Goal.objects.get(id=requirement.goal.id)
        requirements = Requirement.objects.filter(goal=goal)
        scenarios = Scenario.objects.filter(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
        project_id = project.id
        return render(
            request,
            "projects/process/process.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                "viewpoints": viewpoints,
                'scenarios':scenarios,
                'processes':processes,
                'scenario_id':scenario.id,
                "goals": goals,
                'requirement_id':requirement.id
                ,'member':member,
                'project':project
            },
        )

    scenario = Scenario.objects.get(id=scenario_id)
    processes = Process.objects.filter(scenario=scenario)
    requirement = Requirement.objects.get(id=scenario.requirement.id )
    goal = Goal.objects.get(id=requirement.goal.id)
    requirements = Requirement.objects.filter(goal=goal)
    scenarios = Scenario.objects.filter(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    goals = Goal.objects.filter(viewpoint=viewpoint)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            'scenarios':scenarios,
            'scenario_id':scenario.id,
            "viewpoints": viewpoints,
            "goals": goals,
            'processes':processes,
            'requirement_id':requirement.id
            ,'member':member,
            'project':project
        },
    )

    


def viewprocess(request,process_id):
    indexhead = "Process Description"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        process_id = request.POST.get("process")
        process = Process.objects.get(id=process_id)
        scenario=Scenario.objects.get(id=process.scenario.id)
        processes = Process.objects.filter(scenario=scenario).order_by('-id')
        requirement=Requirement.objects.get(id=scenario.requirement.id)
        scenarios = Scenario.objects.filter(requirement=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        return render(
            request,
            "projects/process/view_process.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "scenario_id": scenario.id,
                "viewpoint_id": viewpoint_id,
                "project_id": project_id,
                "goal_id": goal.id,
                'process':process,
                'scenarios':scenarios,
                'processes':processes,
                "viewpoints": viewpoints,
                "requirements": requirements,
                'requirement_id':requirement.id
                ,'member':member,
                'project':project
            },
        )
    process = Process.objects.get(id=process_id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario).order_by('-id')
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    return render(
        request,
        "projects/process/view_process.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            'scenario_id':scenario.id,
            "viewpoint_id": viewpoint_id,
            "project_id": project_id,
            "goal_id": goal.id,
            'process':process,
            "viewpoints": viewpoints,
            'processes':processes,
            'scenarios':scenarios,
            "requirements": requirements,
            'requirement_id':requirement.id
            ,'member':member,
            'project':project
        },
    )


def createProcess(request,scenario_id):
    indexhead = "Create Process"
    member = Member.objects.get(user=request.user)
    scenario = Scenario.objects.get(id=scenario_id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == 'POST':
        process_title = request.POST.get('process_title')
        process_link = request.POST.get('link')
        process_photo = request.FILES.get('process_photo')
        process_docs = request.FILES.get('process_docs')
        description = request.POST.get('process_descriptions')
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        process = Process.objects.create(
            process_name=process_title,
            process_photo=process_photo,
            process_links=process_link,
            created_by=created_by,
            process_docs=process_docs,
            description=description,
            scenario=scenario
        )
        process.save()
        if process:
            indexhead = "Scenario-Processes:"
            requirements = Requirement.objects.filter(goal=goal).order_by('-id')
            scenarios = Scenario.objects.filter(requirement=requirement).order_by('-id')
            processes = Process.objects.filter(scenario=scenario).order_by('-id')
            return render(
            request,
            "projects/process/process.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                'requirement_id':requirement.id,
                'scenarios':scenarios,
                'scenario_id':scenario.id,
                "viewpoints": viewpoints,
                'processes':processes,
                "goals": goals,
                'member':member,
                'project':project
            },
            )

    return render(
        request, "projects/process/create_process.html", {"indexhead": indexhead,'viewpoints':viewpoints,'scenario_id':scenario_id,'member':member}
    )


def usecases(request, process_id):
    indexhead = "Process-Usecases"
    member = Member.objects.get(user=request.user)
    if request.method == 'POST':
        process_id = request.POST.get('process')
        process = Process.objects.get(id=process_id)
        scenario = Scenario.objects.get(id=process.scenario.id)
        usecases = UseCase.objects.filter(process=process).order_by('-id')
        processes = Process.objects.filter(scenario=scenario)
        requirement = Requirement.objects.get(id=scenario.requirement.id )
        goal = Goal.objects.get(id=requirement.goal.id)
        requirements = Requirement.objects.filter(goal=goal)
        scenarios = Scenario.objects.filter(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
        project_id = project.id
        return render(
            request,
            "projects/usecase/usecases.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                "viewpoints": viewpoints,
                'scenarios':scenarios,
                'processes':processes,
                'scenario_id':scenario.id,
                "goals": goals,
                'usecases':usecases,
                'process_id':process.id,
                'requirement_id':requirement.id
                ,'member':member,
                'project':project
            },
        )
    process = Process.objects.get(id=process_id)
    usecases = UseCase.objects.filter(process=process).order_by('-id')
    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario)
    requirement = Requirement.objects.get(id=scenario.requirement.id )
    goal = Goal.objects.get(id=requirement.goal.id)
    requirements = Requirement.objects.filter(goal=goal)
    scenarios = Scenario.objects.filter(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    goals = Goal.objects.filter(viewpoint=viewpoint)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            'scenarios':scenarios,
            'scenario_id':scenario.id,
            "viewpoints": viewpoints,
            "goals": goals,
            'usecases':usecases,
            'process_id':process.id,
            'processes':processes,
            'requirement_id':requirement.id
            ,'member':member,
            'project':project
        },
    )


def viewusecase(request,usecase_id):
    indexhead = "Usecase Description"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        usecase_id = request.POST.get("usecase")
        usecase = UseCase.objects.get(id=usecase_id)
        process = Process.objects.get(id=usecase.process.id)
        scenario=Scenario.objects.get(id=process.scenario.id)
        processes = Process.objects.filter(scenario=scenario).order_by('-id')
        requirement=Requirement.objects.get(id=scenario.requirement.id)
        scenarios = Scenario.objects.filter(requirement=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        usecases = UseCase.objects.filter(process=process).order_by('-id')
        project_id = project.id
        return render(
            request,
            "projects/usecase/view_usecase.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "scenario_id": scenario.id,
                "viewpoint_id": viewpoint_id,
                "project_id": project_id,
                "goal_id": goal.id,
                'process':process,
                'process_id':process.id,
                'scenarios':scenarios,
                'processes':processes,
                'usecase':usecase,
                'usecases':usecases,
                'usecase_id':usecase.id,
                "viewpoints": viewpoints,
                "requirements": requirements,
                'requirement_id':requirement.id
                ,'member':member,
                'project':project
            },
        )
    usecase = UseCase.objects.get(id=usecase_id)
    process = Process.objects.get(id=usecase.process.id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario).order_by('-id')
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    usecases = UseCase.objects.filter(process=process).order_by('-id')
    project_id = project.id
    return render(
        request,
        "projects/usecase/view_usecase.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            'scenario_id':scenario.id,
            "viewpoint_id": viewpoint_id,
            "project_id": project_id,
            "goal_id": goal.id,
            'process':process,
            "viewpoints": viewpoints,
            'processes':processes,
            'scenarios':scenarios,
            'usecase':usecase,
            'usecases':usecases,
            'usecase_id':usecase_id,
            'process_id':process.id,
            "requirements": requirements,
            'requirement_id':requirement.id
            ,'member':member,
            'project':project
        },
    )



def createUsecase(request, process_id):
    indexhead = "Create Usecase"
    member = Member.objects.get(user=request.user)
    process = Process.objects.get(id=process_id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == 'POST':
        usecase_title = request.POST.get('usecase_title')
        usecase_link = request.POST.get('link')
        usecase_photo = request.FILES.get('usecase_photo')
        usecase_docs = request.FILES.get('usecase_docs')
        description = request.POST.get('usecase_descriptions')
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        usecase = UseCase.objects.create(
            usecase_name=usecase_title,
            usecase_photo=usecase_photo,
            usecase_link=usecase_link,
            created_by=created_by,
            usecase_docs=usecase_docs,
            description=description,
            process=process
        )
        usecase.save()
        if usecase:
            indexhead = "Process-Usecases:"
            requirements = Requirement.objects.filter(goal=goal).order_by('-id')
            scenarios = Scenario.objects.filter(requirement=requirement).order_by('-id')
            processes = Process.objects.filter(scenario=scenario).order_by('-id')
            usecases = UseCase.objects.filter(process=process).order_by('-id')
            return render(
            request,
            "projects/usecase/usecases.html",
            {
                "indexhead": indexhead,
                "viewpoint_id": viewpoint_id,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                'requirement_id':requirement.id,
                'scenarios':scenarios,
                'scenario_id':scenario.id,
                "viewpoints": viewpoints,
                'processes':processes,
                'process_id':process.id,
                'usecases':usecases,
                "goals": goals,
                'member':member,
                'project':project
            },
            )

    return render(
        request, "projects/usecase/create_usecase.html", {"indexhead": indexhead,'viewpoints':viewpoints,'process_id':process_id,'member':member})

