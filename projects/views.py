from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q


# Create your views here.
def privacyPolicy(requiest):
    pass


def termsConditions(request):
    pass


def notification(request):
    user = Member.objects.get(user=request.user)
    notification = ActivityLog.objects.filter(affected_user=user).order_by("-id")
    return notification


def total_notification(request):
    user = Member.objects.get(user=request.user)
    notification = ActivityLog.objects.filter(
        affected_user=user, status="not seen"
    ).count()
    return notification


def project_rates(request, project_id):
    project = Project.objects.get(id=project_id)
    fivestar_rate = ProjectRate.objects.filter(
        project=project, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ProjectRate.objects.filter(
        project=project, star_rate__number_of_stars=4
    ).count()
    threestar_rate = ProjectRate.objects.filter(
        project=project, star_rate__number_of_stars=3
    ).count()
    twostar_rate = ProjectRate.objects.filter(
        project=project, star_rate__number_of_stars=2
    ).count()
    onestar_rate = ProjectRate.objects.filter(
        project=project, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics

def viewpoint_rates(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    fivestar_rate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__number_of_stars=4
    ).count()
    threestar_rate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__number_of_stars=3
    ).count()
    twostar_rate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__number_of_stars=2
    ).count()
    onestar_rate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics



def goal_rates(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    fivestar_rate = GoalRate.objects.filter(
        goal=goal, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = GoalRate.objects.filter(
        goal=goal, star_rate__number_of_stars=4
    ).count()
    threestar_rate = GoalRate.objects.filter(
        goal=goal, star_rate__number_of_stars=3
    ).count()
    twostar_rate = GoalRate.objects.filter(
        goal=goal, star_rate__number_of_stars=2
    ).count()
    onestar_rate = GoalRate.objects.filter(
        goal=goal, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics


def requirement_rates(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    fivestar_rate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__number_of_stars=4
    ).count()
    threestar_rate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__number_of_stars=3
    ).count()
    twostar_rate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__number_of_stars=2
    ).count()
    onestar_rate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics

def scenario_rates(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    fivestar_rate = ScenarioRate.objects.filter(
        scenario=scenario, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ScenarioRate.objects.filter(
        scenario=scenario, star_rate__number_of_stars=4
    ).count()
    threestar_rate = ScenarioRate.objects.filter(
        scenario=scenario, star_rate__number_of_stars=3
    ).count()
    twostar_rate = ScenarioRate.objects.filter(
        scenario=scenario, star_rate__number_of_stars=2
    ).count()
    onestar_rate = ScenarioRate.objects.filter(
        scenario=scenario, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics

def process_rates(request, process_id):
    process = Process.objects.get(id=process_id)
    fivestar_rate = ProcessRate.objects.filter(
        process=process, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ProcessRate.objects.filter(
        process=process, star_rate__number_of_stars=4
    ).count()
    threestar_rate = ProcessRate.objects.filter(
        process=process, star_rate__number_of_stars=3
    ).count()
    twostar_rate = ProcessRate.objects.filter(
        process=process, star_rate__number_of_stars=2
    ).count()
    onestar_rate = ProcessRate.objects.filter(
        process=process, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics

def usecase_rates(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    fivestar_rate = UseCaseRate.objects.filter(
        usecase=usecase, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ProcessRate.objects.filter(
        usecase=usecase, star_rate__number_of_stars=4
    ).count()
    threestar_rate = UseCaseRate.objects.filter(
        usecase=usecase, star_rate__number_of_stars=3
    ).count()
    twostar_rate = UseCaseRate.objects.filter(
        usecase=usecase, star_rate__number_of_stars=2
    ).count()
    onestar_rate = UseCaseRate.objects.filter(
        usecase=usecase, star_rate__number_of_stars=1
    ).count()

    if fivestar_rate ==0  and fourstar_rate == 0 and threestar_rate == 0 and twostar_rate == 0 and onestar_rate == 0:
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0
        
    else:
        mean_fivestar_rate = (fivestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_fourstar_rate = (fourstar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_threestar_rate = (threestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_twostar_rate = (twostar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        mean_onestar_rate = (onestar_rate/(fivestar_rate + fourstar_rate + threestar_rate + twostar_rate + onestar_rate))*100
        
    rate_statistics = [
        mean_fivestar_rate,
        mean_fourstar_rate,
        mean_threestar_rate,
        mean_twostar_rate,
        mean_onestar_rate,
    ]
    return rate_statistics

def indexs(request, message=None):
    members = Member.objects.all().count()
    members = members + 100
    projects = Project.objects.all().count()
    projects = projects + 10
    comments = Comment.objects.all().count()
    rates = StarRate.objects.all().count()
    return render(
        request,
        "web/index.html",
        {
            "members": members,
            "projects": projects,
            "rates": rates,
            "comments": comments,
            "message": message,
        },
    )


@login_required(login_url="login")
def index(request):

    indexhead = "Dashboard"
    current_projects = (
        Project.objects.all()
        .order_by("-id")
        .exclude(is_invitational=True, is_discoverable=False)[:6]
    )
    total_projects = Project.objects.all().count()
    members = Member.objects.all().count()
    member = Member.objects.get(user=request.user)
    profile_update = Member.objects.filter(user=request.user, profile_photo="").exists()
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
            "profile_update": profile_update,
            "member": member,
            "members": members,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# user profile function
@login_required(login_url="login")
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
            "member": member,
            "hidesearch": hidesearch,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# login function
def login(request):
    if request.user.is_authenticated:
        print(request.user.username)
        if not Member.objects.filter(user=request.user).exists():
            member = Member.objects.create(
                user=request.user,
                first_name=request.user.username,
                middle_name=request.user.username,
                surname=request.user.username,
                email=request.user.email

            )
            member.save()
            return redirect("projects:profile")

        return redirect("index")

    elif request.method == "POST":
        auth_logout(request)
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return redirect("index")
            message = "sorry your account is inactive communicate with your Admin"
            return render(request, "login.html", {"message": message})
        message = "Soory you have entered incorrect credentials"
        return render(request, "login.html", {"message": message})
    return render(request, "login.html", {})




# user logout
def logout(request):

    # builtin function for session destroy
    auth_logout(request)
    return redirect("login")

def recovery(request, user_id=None):

    if request.method == "POST":
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            user_account = User.objects.filter(id=user_id).update(
                password=password
            )
            
            if user_account:
                message = "Your password has been successfull Reseted, now you can login with new password"
                return render(request,'password_reset.html',{'message':message,'user_id':user_id})
            message1 = "Sorry failed to reset password try again"
            return render(request,'password_reset.html',{'message1':message1,'user_id':user_id})
        message1 = "Password did not match, please enter correctly"
        return render(request,'password_reset.html',{'message1':message1,'user_id':user_id})
    return render(request,'password_reset.html',{'user_id':user_id})




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
    if request.method == "POST":
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            link = "127.0.0.1:8000/reset-password/"+ str(user.id)
            message = "Dear " + user.username +" You can reset your account password by click on this link: " + link + ""

            # then sending email
            send_email = send_mail(
                    'CORES Password Reset',
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False
                    )
            print(send_email)
            if send_email:
                result = "password recovery link as been sent to " + email
                return render(request,"password_recover.html",  {"message":result})
            result = "sorry failed to send a link try again"
            return render(request,"password_recover.html",  {"message1":result})
        result = "sorry there is no account with this email address"
        return render(request,"password_recover.html",  {"message1":result})
    return render(request, "password_recover.html", {})


def pagenotfound(request, exception):

    return render(request, "pagenotfound.html", {})


def servererror(request):

    return render(request, "pagenotfound.html", {})


# project views and project workspace
@login_required(login_url="login")
def createProject(request):
    member = Member.objects.get(user=request.user.id)
    if request.method == "POST":
        project_title = request.POST.get("project_title")
        sector = request.POST.getlist("sector")
        due_date = request.POST.get("due_date")
        project_photo = request.FILES.get("project_photo")
        project_files = request.FILES.get("project_docs")
        project_visibility = request.POST.get("visibility")
        project_participation = request.POST.getlist("participation")
        project_description = request.POST.get("project_descriptions")
        incentives = request.POST.getlist("incentives")

        # getting member who create of project
        member = Member.objects.get(user=request.user.id)

        if project_photo:
            print("First one called:")
            print(project_photo)

            project = Project.objects.create(
                created_by=member,
                project_photo=project_photo,
                project_files=project_files,
                project_title=project_title,
                project_visibility=project_visibility,
                description=project_description,
                due_date=due_date,
            )
        else:
            print("seccond one called:")
            project = Project.objects.create(
                created_by=member,
                project_files=project_files,
                project_title=project_title,
                project_visibility=project_visibility,
                description=project_description,
                due_date=due_date,
            )
        project.save()

        if "Invitational" in project_participation:
            project.is_invitational = True
            project.save()

        if "Discoverable" in project_participation:
            project.is_discoverable = True
            project.save()

        if project_visibility == "public":
            project.is_public = True
            project.save()

        # Then create project sector
        for sector in sector:
            sector = Sector.objects.get(id=sector)
            project_sector = ProjectSector.objects.create(
                project=project, sector=sector
            )
            project_sector.save()
        # Createing project incentives
        for incentive in incentives:
            incentive = Incentive.objects.get(id=incentive)
            project_incentive = ProjectIncentive.objects.create(
                project=project, incentive=incentive
            )
            project_incentive.save()

        # create default viewpoints
        default_viewpoints = DefaultViewpoint.objects.all()
        for default_viewpoint in default_viewpoints:
            viewpoint = Viewpoint.objects.create(
                project=project,
                viewpoint_name=default_viewpoint.viewpoint_name,
                viewpoint_photo=default_viewpoint.viewpoint_photo,
                description=default_viewpoint.description,
                created_by=member
            )
            viewpoint.save()
         

        if project:
            project_membership = ProjectMembership.objects.create(
                project=project, member=member, member_role="Admin", status="active"
            )
            project_membership.save()
            return redirect("projects:myprojects")

    indexhead = "Project / Create-Project"
    hidesearch = "hide"
    sectors = Sector.objects.all().order_by("sector_name")
    incentives = Incentive.objects.all().order_by("incentive_type")
    return render(
        request,
        "projects/my_projects/create_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "sectors": sectors,
            "incentives": incentives,
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def sendInvitation(request, project_id, member_id):
    member = Member.objects.get(id=member_id)
    project = Project.objects.get(id=project_id)
    if not ProjectMembership.objects.filter(project=project, member=member).exists():
        invitation = ProjectMembership.objects.create(
            project=project, member=member, member_role="member", status="invited"
        )
        invitation.save()
        if invitation:
            link = "invitations"
            activity = (
                "You have been invited by "
                + str(Member.objects.get(user=request.user))
                + " on "
                + str(project.project_title)
                + " project"
            )
            notify(request, affected_user=member, activity=activity, link=link)
            return inviteMembers(request, project_id=project_id)

    return inviteMembers(request, project_id=project_id)


@login_required(login_url="login")
def inviteMembers(request, project_id, member_id=None):
    indexhead = "Invite Members:"
    placeholder = "search Members"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    project_membership = ProjectMembership.objects.filter(project=project)
    ids = []
    for id in project_membership:
        id = id.member.id
        ids.append(id)
    print(ids)
    member_details = enumerate(
        Member.objects.exclude(id__in=ids).order_by("-id"), start=1
    )
    return render(
        request,
        "projects/my_projects/invite_members.html",
        {
            "indexhead": indexhead,
            "placeholder": placeholder,
            "project_id": project_id,
            "member": member,
            "project": project,
            "member_details": member_details,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewMemberDetails(request, member_id):
    indexhead = "User Detals:"
    hidesearch = "hide"
    member_details = Member.objects.get(id=member_id)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "user/details.html",
        {
            "member_details": member_details,
            "indexhead": indexhead,
            "member": member,
            "hidesearch": hidesearch,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def updatePersonalDetails(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        surname = request.POST.get("surname")
        date_of_birth = request.POST.get("date_of_birth")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        job_email = request.POST.get("job_email")
        profile_photo = request.FILES.get("profile_photo")
        member = Member.objects.get(user=request.user)

        if profile_photo:
            member.profile_photo = request.FILES["profile_photo"]
            member.save()
            profile_photo = member.profile_photo
        else:
            profile_photo = member.profile_photo

        if date_of_birth == "" or date_of_birth == None:
            date_of_birth = member.date_of_birth

        update_profile = Member.objects.filter(id=member.id).update(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            phone=phone,
            date_of_birth=date_of_birth,
            gender=gender,
            email=email,
            job_email=job_email,
            profile_photo=profile_photo,
        )
        if update_profile:
            return redirect("projects:profile")
    return redirect("projects:profile")


@login_required(login_url="login")
def updateResidenceDetails(request):
    if request.method == "POST":
        country = request.POST.get("country")
        region = request.POST.get("region")
        district = request.POST.get("district")
        member = Member.objects.get(user=request.user)

        update_profile = Member.objects.filter(id=member.id).update(
            country=country, region=region, district=district
        )
        if update_profile:
            return redirect("projects:profile")
    return redirect("projects:profile")


@login_required(login_url="login")
def updateJobDetails(request):
    if request.method == "POST":
        professional = request.POST.get("professonal")
        job_title = request.POST.get("job_title")
        institution_name = request.POST.get("institution_name")
        member = Member.objects.get(user=request.user)

        update_profile = Member.objects.filter(id=member.id).update(
            professional=professional,
            job_title=job_title,
            institution_name=institution_name,
        )
        if update_profile:
            return redirect("projects:profile")
    return redirect("projects:profile")


@login_required(login_url="login")
def editProject(request, project_id):
    indexhead = "Project / Edit-Project"
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
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def deleteProject(request, project_id):
    delete_project = Project.objects.get(id=project_id).delete()
    if delete_project:
        return redirect("projects:myprojects")


@login_required(login_url="login")
def createProjectComment(request, project_id):
    indexhead = "Project Details"
    hidesearch = "hide"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if ProjectMembership.objects.filter(project=project,member=member,status="active").exists():

        if request.method == "POST":
            comment = request.POST.get("comment")

            #    then creating comment then ProjectComment
            comment_data = Comment.objects.create(comment=comment, commented_by=member)
            comment_data.save()
            if comment_data:
                
                project_comment = ProjectComment.objects.create(
                    comment=comment_data, project=project
                )
                project_comment.save()
                if project_comment:
                    if project.created_by != member:
                        link = "commented"
                        activity = (
                            "Dear "
                            + str(project.created_by)
                            + " You have one new comment on "
                            + str(project.project_title)
                            + " project from "
                            + str(member)
                        )
                        notify(
                            request,
                            affected_user=project.created_by,
                            activity=activity,
                            link=link,
                        )
                        return redirect("projects:viewproject", project_id=project_id)
        return redirect("projects:viewproject", project_id=project_id)
    message = "sorry you can not comment on this Project, you are not active member of this project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def createViewpointComment(request, viewpoint_id):
    indexhead = "Viewpoint Details"
    hidesearch = "hide"

    if request.method == "POST":
        comment = request.POST.get("comment")
        member = Member.objects.get(user=request.user)

        #    then creating comment then ProjectComment
        comment_data = Comment.objects.create(comment=comment, commented_by=member)
        comment_data.save()
        if comment_data:
            viewpoint = Viewpoint.objects.get(id=viewpoint_id)
            viewpoint_comment = ViewPointComment.objects.create(
                comment=comment_data, viewpoint=viewpoint
            )
            viewpoint_comment.save()
            if viewpoint_comment:
                if viewpoint.created_by != member:
                    link = "commented"
                    activity = (
                        "Dear "
                        + str(viewpoint.created_by)
                        + " You have one new comment on "
                        + str(viewpoint)
                        + " Viewpoint from "
                        + str(member)
                    )
                    notify(
                        request,
                        affected_user=viewpoint.created_by,
                        activity=activity,
                        link=link,
                    )
                    return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)
    return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def projectIncentive(request, project_id=None):
    project = Project.objects.get(id=project_id)
    project_members = ProjectMembership.objects.filter(
        project=project, status="active", member_role="member"
    ).order_by("member")

    # getting project member incentives
    project_incentives = enumerate(
        ProjectMemberIncentive.objects.filter(
            projectincentive__project=project
        ).order_by("-id"),
        start=1,
    )

    # getting project incentives for assigning incentives to the members
    incentive_types = ProjectIncentive.objects.filter(project=project).order_by("-id")

    # getting list of incentive Ids so as to exclude on adding new project Incentives
    incentive_list = []
    for incentive_type in incentive_types:
        incentive_list.append(incentive_type.incentive.id)

    # getting all Incentives exclude all which are in project incentive
    types = Incentive.objects.all().exclude(id__in=incentive_list)

    hidesearch = "hide"
    headindex = "Project Incentives"
    if request.method == "POST":
        incentive = ProjectIncentive.objects.get(id=request.POST.get("incentive_type"))
        member = Member.objects.get(id=request.POST.get("member"))
        description = request.POST.get("description")

        # Then create ProjectIncentive
        project_incentive = ProjectMemberIncentive.objects.create(
            projectincentive=incentive, member=member, description=description
        )
        project_incentive.save()
        if project_incentive:
            link = "incentives"
            activity = (
                "Dear "
                + str(member)
                + " you have been awarded a gift for best Contribution on "
                + str(project.project_title)
                + " project, just go and view your Gift on Incentives"
            )
            notify(request, affected_user=member, activity=activity, link=link)
            project_incentives = enumerate(
                ProjectMemberIncentive.objects.filter(
                    projectincentive__project=project
                ).order_by("-id"),
                start=1,
            )
            return redirect("projects:projectincentives", project_id=project_id)

    return render(
        request,
        "projects/my_projects/project_incentive.html",
        {
            "project_incentives": project_incentives,
            "incentive_types": incentive_types,
            "project_members": project_members,
            "indexhead": headindex,
            "hidesearch": hidesearch,
            "project_id": project_id,
            "project": project,
            "types": types,
            "member": Member.objects.get(user=request.user),
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def add_incentive(request, project_id):
    project = Project.objects.get(id=project_id)
    incentives = request.POST.getlist("incentives")
    for incentive in incentives:
        new_incentive = Incentive.objects.get(id=incentive)
        project_incentive = ProjectIncentive.objects.create(
            project=project, incentive=new_incentive
        )
        project_incentive.save()
    return redirect("projects:projectincentives", project_id=project_id)


@login_required(login_url="login")
def remove_incentive(request, incentive_id):
    project = ProjectMemberIncentive.objects.get(id=incentive_id)
    remove = ProjectMemberIncentive.objects.filter(id=incentive_id).delete()
    return redirect(
        "projects:projectincentives", project_id=project.projectincentive.project.id
    )


@login_required(login_url="login")
def membershipProjects(request):
    indexhead = "Projects / Membership Project(s)"
    member = Member.objects.get(user=request.user)
    membershipprojects = ProjectMembership.objects.filter(
        member=member, status="active", member_role="member"
    ).order_by("-id")
    paginator = Paginator(membershipprojects, 6)
    page_number = request.GET.get('page')
    membershipprojects = paginator.get_page(page_number)
    return render(
        request,
        "projects/other_projects/membership_projects.html",
        {
            "indexhead": indexhead,
            "membershipprojects": membershipprojects,
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def myProjects(request):
    indexhead = "Projects / My Project(s)"
    placeholder = "search your project"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        keyword = request.POST.get('project_keyword')
        myProject = Project.objects.filter(created_by=member,project_title__icontains=keyword).order_by("-id")
    else:
        myProject = Project.objects.filter(created_by=member).order_by("-id")
    return render(
        request,
        "projects/my_projects/myproject.html",
        {
            "indexhead": indexhead,
            "myProject": myProject,
            "member": member,
            'placeholder':placeholder,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewMyproject(request, project_id):
    indexhead = "Projects / My Project Details"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    comments = ProjectComment.objects.filter(project=project).order_by("-id")
    projectRate = ProjectRate.objects.filter(
        project=project, star_rate__rated_by=member
    )
    rates = ProjectRate.objects.filter(project=project).order_by(
        "-star_rate__number_of_stars"
    )
    likes = ProjectLike.objects.filter(project=project).count()
    dislikes = ProjectDislike.objects.filter(project=project).count()
    total_rates = rates.count()
    total_comments = comments.count()
    hidesearch = "hide"
    project_id
    rate_data = project_rates(request,project_id=project_id)
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
            "member": member,
            "projectRate": projectRate,
            "total_rates": total_rates,
            "likes": likes,
            "dislikes": dislikes,
            "rates": rates,
            "notification": notification(request),
            "total_notification": total_notification(request),
            'rate_data':rate_data
        },
    )


@login_required(login_url="login")
def viewProject(request, project_id, message=None):
    indexhead = "Project Details"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    project_membership = ProjectMembership.objects.filter(
        member=member, project=project, project__project_visibility="private"
    ).exists()

    project_member = None
    if project_membership:
        project_member = ProjectMembership.objects.get(
            member=member, project=project, project__project_visibility="private"
        )
    comments = ProjectComment.objects.filter(project=project).order_by("-id")
    tags = enumerate(ProjectSector.objects.filter(project=project), start=1)
    likes = ProjectLike.objects.filter(project=project).count()
    dislikes = ProjectDislike.objects.filter(project=project).count()
    projectRate = ProjectRate.objects.filter(
        project=project, star_rate__rated_by=member
    )
    rates = ProjectRate.objects.filter(project=project).order_by(
        "-star_rate__number_of_stars"
    )

    total_rates = rates.count()
    total_comments = comments.count()
    rate_data = project_rates(request, project_id=project_id)
    print(rate_data)

    return render(
        request,
        "projects/other_projects/view_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project": project,
            "comments": comments,
            "tags": tags,
            "total_comments": total_comments,
            "member": member,
            "projectRate": projectRate,
            "message": message,
            "rates": rates,
            "likes": likes,
            "project_member": project_member,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "project_membership": project_membership,
            "rate_data": rate_data,
        }
    )


@login_required(login_url="login")
def projectMembers(request, project_id=None):
    indexhead = "Projects / Project-Members"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    project_member = enumerate(
        ProjectMembership.objects.filter(project=project)
        .exclude(status__in=["removed", "rejected", "invited"])
        .order_by("-id"),
        start=1,
    )
    placeholder = "search member"

    return render(
        request,
        "projects/my_projects/project_members.html",
        {
            "indexhead": indexhead,
            "project_member": project_member,
            "placeholder": placeholder,
            "project_id": project_id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def membershipRequest(request, project_id):
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)

    if not ProjectMembership.objects.filter(member=member, project=project).exists():
        projectmembership = ProjectMembership.objects.create(
            project=project, member=member, member_role="member", status="request"
        )
        projectmembership.save()
        if projectmembership:
            link = "request"
            activity = (
                "Dear "
                + str(
                    ProjectMembership.objects.get(
                        member=member, project=project
                    ).project.created_by
                )
                + " you have one new projectmembership request from "
                + str(member)
                + " on "
                + str(project.project_title)
                + " Project"
            )
            notify(
                request,
                affected_user=ProjectMembership.objects.get(
                    member=member, project=project
                ).project.created_by,
                activity=activity,
                link=link,
            )
            return redirect("projects:viewproject", project_id=project_id)
    return redirect("projects:viewproject", project_id=project_id)


@login_required(login_url="login")
def membershipApproval(request, membership_id, project_id):
    member = ProjectMembership.objects.filter(id=membership_id)
    membership = ProjectMembership.objects.get(id=membership_id)
    member.update(status="active")
    if member:
        link = "approved"
        activity = (
            "Dear "
            + str(membership.member)
            + " your request to join "
            + str(membership.project.project_title)
            + " has been accepted."
        )
        notify(request, affected_user=membership.member, activity=activity, link=link)
        return memberRequest(request, project_id=project_id)


@login_required(login_url="login")
def membershipRejection(request, membership_id, project_id):
    projectmembership = ProjectMembership.objects.get(id=membership_id)
    member = ProjectMembership.objects.filter(id=membership_id).update(
        status="rejected"
    )
    if member:
        link = "rejected"
        activity = (
            "You have been rejected  on "
            + str(projectmembership.project.project_title)
            + " project"
        )
        notify(
            request,
            affected_user=projectmembership.member,
            activity=activity,
            link=link,
        )
        return memberRequest(request, project_id=project_id)


@login_required(login_url="login")
def suspendMembership(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)

    if membership.member_role != "Admin":
        suspend = ProjectMembership.objects.filter(id=membership_id).update(
            status="suspended"
        )
        if suspend:
            link = "suspended"
            activity = (
                "You have been Suspended on "
                + str(membership.project.project_title)
                + " project"
            )
            notify(
                request, affected_user=membership.member, activity=activity, link=link
            )
            return projectMembers(request, project_id=membership.project.id)
    return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def removeMember(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)
    if membership.member_role != "Admin":
        remove = ProjectMembership.objects.filter(id=membership_id).delete()
        if remove:
            link = "removemember"
            activity = (
                "Dear "
                + str(membership.member)
                + " you have been removed from "
                + str(membership.project.project_title)
                + " membership"
            )
            notify(
                request, affected_user=membership.member, activity=activity, link=link
            )
            return projectMembers(request, project_id=membership.project.id)
    return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def incentives(request):
    indexhead = "Member Incentives"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    incentives = enumerate(
        ProjectMemberIncentive.objects.filter(member=member).order_by("-id"), start=1
    )
    return render(
        request,
        "user/incentives.html",
        {
            "indexhead": indexhead,
            "incentives": incentives,
            "member": member,
            "hidesearch": hidesearch,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def invitations(request):
    indexhead = "Project Membership Invitations:"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    invitations = enumerate(
        ProjectMembership.objects.filter(member=member, status="invited"), start=1
    )
    return render(
        request,
        "user/invitations.html",
        {
            "member": member,
            "indexhead": indexhead,
            "invitations": invitations,
            "hidesearch": hidesearch,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def acceptInvitation(request, request_id):
    member = Member.objects.get(user=request.user)
    projectmembership = ProjectMembership.objects.get(id=request_id)
    accept = ProjectMembership.objects.filter(id=request_id).update(status="active")

    if accept:
        link = "projectmembers"
        activity = (
            str(member)
            + " has been accepted "
            + str(projectmembership.project.project_title)
            + " invitation"
        )
        notify(
            request,
            affected_user=projectmembership.project.created_by,
            activity=activity,
            link=link,
        )
        return invitations(request)
    return invitations(request)


@login_required(login_url="login")
def rejectInvitation(request, request_id):
    reject = ProjectMembership.objects.filter(id=request_id).update(status="Rejected")
    if reject:
        return invitations(request)
    return invitations(request)


@login_required(login_url="login")
def activateMembership(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)
    activate = ProjectMembership.objects.filter(id=membership_id).update(
        status="active"
    )
    if activate:
        link = "activate"
        activity = (
            "Dear "
            + str(membership.member)
            + " your "
            + str(membership.project.project_title)
            + " membership has been activated"
        )
        notify(request, affected_user=membership.member, activity=activity, link=link)
        return projectMembers(request, project_id=membership.project.id)
    return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def memberRequest(request, project_id):
    indexhead = "Project / Member Requests"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    member_details = enumerate(
        ProjectMembership.objects.filter(project=project, status="request"), start=1
    )

    return render(
        request,
        "projects/my_projects/member_request.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "member": member,
            "project": project,
            "member_details": member_details,
            "project_id": project_id,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def projects(request, project_id=None, message=None, requestmessage=None):
    indexhead = "Projects"
    placeholder = "search project"
    member = Member.objects.get(user=request.user)

    if request.method == "POST":
        keyword = request.POST.get('project_keyword')
        projects = (
        Project.objects.filter(project_title__icontains=keyword)
            .order_by("-id")
            .exclude(is_invitational=True, is_discoverable=False)
        )

    else:
        projects = (
            Project.objects.all()
            .order_by("-id")
            .exclude(is_invitational=True, is_discoverable=False)
        )

    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)

    return render(
        request,
        "projects/other_projects/projects.html",
        {
            "indexhead": indexhead,
            "projects": projects,
            "member": member,
            "message": message,
            'placeholder':placeholder,
            "project_id": project_id,
            "requestmessage": requestmessage,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewPoint(request, project_id=None, viewpoint_id=None, message=None):
    indexhead = "Project - ViewPoint"
    hidesearch = "hide"

    member = Member.objects.get(user=request.user)
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(id=viewpoint.project.id)
    comments = ViewPointComment.objects.filter(viewpoint=viewpoint).order_by("-id")
    total_comments = comments.count()
    likes = ViewpointLike.objects.filter(view_point=viewpoint).count()
    dislikes = ViewpointDislike.objects.filter(view_point=viewpoint).count()

    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    viewpointRate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__rated_by=member
    )
    rates = ViewPointRate.objects.filter(view_point=viewpoint).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    project_id = project.id
    rate_data = viewpoint_rates(request,viewpoint_id=viewpoint_id)
    if viewpoint.created_by == member:
        creator = "me"
    else:
        creator = "not me"
    return render(
        request,
        "projects/viewpoints/viewpoint.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoint": viewpoint,
            "viewpoints": viewpoints,
            "project_id": project_id,
            "member": member,
            "project": project,
            "message": message,
            'rate_data':rate_data,
            "viewpointRate": viewpointRate,
            "rates": rates,
            "likes": likes,
            'creator':creator,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "comments": comments,
            "total_comments": total_comments,
            "message": message,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewpoints(request, project_id):

    indexhead = "Project - ViewPoint"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        member = Member.objects.get(user=request.user)
        hidesearch = "hide"
        filltering_project = ProjectMembership.objects.filter(
            member=member, status="active"
        )

        my_projects_id = []
        for _project in filltering_project:
            my_projects_id.append(_project.project.id)
    
        projects = Project.objects.filter(Q(id__in=my_projects_id) | Q(project_visibility="public")).order_by("-id")
        project_id = request.POST.get("project")
        project = Project.objects.get(id=project_id)
        viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")
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
                "member": member,
                "project": project,
                "projects": projects,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    else:
        project = Project.objects.get(id=project_id)
        if project.project_visibility == "private":

            if ProjectMembership.objects.filter(
                member=member, project=project
            ).exists():

                membership = ProjectMembership.objects.get(
                    member=member, project=project
                )

                if membership.status == "request":
                    requestmessage = "Sorry your Request to join this project is still on processing stage, we will notify you once your request being accepted or rejected"
                    return viewProject(
                        request, project_id=project_id, message=requestmessage
                    )
                if membership.status == "rejected":
                    requestmessage = "Sorry you can not access this project, your Request to join this project has been Rejected"
                    return viewProject(
                        request, project_id=project_id, message=requestmessage
                    )
                if membership.status == "removed":
                    requestmessage = "Sorry you can not access this project, you have been removed from this project"
                    return viewProject(
                        request, project_id=project_id, message=requestmessage
                    )
                if membership.status == "suspended":
                    requestmessage = "Sorry you can not access this project, your  project membership has been suspended"
                    return viewProject(
                        request, project_id=project_id, message=requestmessage
                    )
            hidesearch = "hide"

            filltering_project = ProjectMembership.objects.filter(
                member=member, status="active"
            )

            my_projects_id = []
            for _project in filltering_project:
                my_projects_id.append(_project.project.id)

            projects = Project.objects.filter(Q(id__in=my_projects_id) | Q(project_visibility="public")).order_by("-id")
            print(projects)
            viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")
            viewpoints = Viewpoint.objects.filter(project=project_id).order_by("-id")
            return render(
                request,
                "projects/viewpoints/viewpoints.html",
                {
                    "indexhead": indexhead,
                    "hidesearch": hidesearch,
                    "viewpoint": viewpoint,
                    "viewpoints": viewpoints,
                    "project_id": project_id,
                    "member": member,
                    "project": project,
                    "projects": projects,
                    "notification": notification(request),
                    "total_notification": total_notification(request),
                },
            )
        filltering_project = ProjectMembership.objects.filter(
            member=member, status="active"
        )

        my_projects_id = []
        for _project in filltering_project:
            my_projects_id.append(_project.project.id)

        projects = Project.objects.filter(Q(id__in=my_projects_id) | Q(project_visibility="public")).order_by("-id")
        print(projects)
        viewpoint = Viewpoint.objects.filter(project=project_id).order_by("-id")
        viewpoints = Viewpoint.objects.filter(project=project_id).order_by("-id")
        return render(
            request,
            "projects/viewpoints/viewpoints.html",
            {
                "indexhead": indexhead,
                "hidesearch": hidesearch,
                "viewpoint": viewpoint,
                "viewpoints": viewpoints,
                "project_id": project_id,
                "member": member,
                "project": project,
                "projects": projects,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )


@login_required(login_url="login")
def createViewpoint(request, project_id):
     # getting member who to create a viewpoint
    user_id = request.user.id
    member = Member.objects.get(user=user_id)
    project = Project.objects.get(id=project_id)
    if request.method == "POST":
        viewpoint_title = request.POST.get("viewpoint_title")
        links = request.POST.get("links")
        viewpoint_photo = request.FILES.get("viewpoint_photo")
        viewpoint_docs = request.FILES.get("viewpoint_docs")
        viewpoint_descriptions = request.POST.get("viewpoint_descriptions")
       

       

        if viewpoint_photo:

            viewpoint = Viewpoint.objects.create(
                project=project,
                created_by=member,
                viewpoint_name=viewpoint_title,
                viewpoint_links=links,
                viewpoint_photo=viewpoint_photo,
                viewpoint_docs=viewpoint_docs,
                description=viewpoint_descriptions,
            )
        else:
            viewpoint = Viewpoint.objects.create(
                project=project,
                created_by=member,
                viewpoint_name=viewpoint_title,
                viewpoint_links=links,
                viewpoint_docs=viewpoint_docs,
                description=viewpoint_descriptions,
            )
        viewpoint.save()
        if viewpoint:
            return redirect("projects:viewpoints", project_id=project_id)

    indexhead = "Project -ViewPoints"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/viewpoints/create_viewpoint.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project_id": project_id,
            "member": member,
            'project':project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def goals(request, project_id=None, viewpoint_id=None):
    indexhead = "Viewpoint-Goals"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        viewpoint = request.POST.get("viewpoint_id")
        goals = Goal.objects.filter(viewpoint=viewpoint)
        viewpoint = Viewpoint.objects.get(id=viewpoint)
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
                'viewpoint':viewpoint,
                "member": member,
                "project": project,
                "project_id": project.id,
                "notification": notification(request),
                "total_notification": total_notification(request),
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
            "member": member,
            "project": project,
            'viewpoint':viewpoint,
            "project_id": project.id,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewGoal(request, goal_id, message=None):
    indexhead = "Goal Description"
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    comments = GoalComment.objects.filter(goal=goal).order_by("-id")
    goalRate = GoalRate.objects.filter(goal=goal, star_rate__rated_by=member)
    rates = GoalRate.objects.filter(goal=goal).order_by("-star_rate__number_of_stars")
    total_rates = rates.count()
    total_comments = comments.count()
    likes = GoalLike.objects.filter(goal=goal).count()
    dislikes = GoalDislike.objects.filter(goal=goal).count()
    if request.method == "POST":
        goal = request.POST.get("goal")
        goal = Goal.objects.get(id=goal_id)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        goals = Goal.objects.filter(viewpoint=viewpoint).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        rate_data = goal_rates(request,goal_id=goal_id)
        if goal.created_by == member:
            creator = "me"
        else:
            creator = "not me"
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
                "comments": comments,
                'rate_data':rate_data,
                "goalRate": goalRate,
                "total_rates": total_rates,
                "total_comments": total_comments,
                "message": message,
                "rates": rates,
                'creator':creator,
                "likes": likes,
                "dislikes": dislikes,
                "goals": goals,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    goal = Goal.objects.get(id=goal_id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    goals = Goal.objects.filter(viewpoint=viewpoint).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    rate_data = goal_rates(request,goal_id=goal_id)
    if goal.created_by == member:
        creator = "me"
    else:
        creator = "not me"
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
            "comments": comments,
            "goalRate": goalRate,
            "likes": likes,
            'rate_data':rate_data,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "total_comments": total_comments,
            "rates": rates,
            "goals": goals,
            'creator':creator,
            "message": message,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createGoal(request, viewpoint_id):
    indexhead = "Create Goal"
    member = Member.objects.get(user=request.user)
    categories = Category.objects.all().order_by("category_name")
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(id=viewpoint.project.id)
    requirements = Requirement.objects.filter(project=project).order_by('name')
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == "POST":
        goal_name = request.POST.get("goal_title")
        description = request.POST.get("description")
        requirement = request.POST.get("requirement")
        created_by = Member.objects.get(user=request.user)
        viewpoint = viewpoint

        # then creating goal
        goal = Goal.objects.create(
            goal_name=goal_name,
            description=description,
            created_by=created_by,
            viewpoint=viewpoint,
            project=project,
        )
        goal.save()
        if goal:

            goals = Goal.objects.filter(viewpoint=viewpoint_id).order_by("-id")
            viewpoint = Viewpoint.objects.get(id=viewpoint_id)
            project = Project.objects.get(id=viewpoint.project.id)
            viewpointiees = Viewpoint.objects.filter(project=project.id).order_by("-id")

            viewpoint_id = viewpoint_id
            return redirect("projects:goals", viewpoint_id=viewpoint_id)

    return render(
        request,
        "projects/Goals/create_goal.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
            'requirements':requirements,
            "categories": categories,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def requirements(request, goal_id):
    indexhead = "Goal-Requirements"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        goal_id = request.POST.get("goal")
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
                'goal':goal,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
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
            'goal':goal,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewrequirement(request, requirement_id=None, message=None):
    indexhead = "Requirement Description"
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    comments = RequirementComment.objects.filter(requirement=requirement).order_by(
        "-id"
    )
    requirementRate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__rated_by=member
    )
    rates = RequirementRate.objects.filter(requirement=requirement).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = RequirementLike.objects.filter(requirement=requirement).count()
    dislikes = RequirementDislike.objects.filter(requirement=requirement).count()
    if request.POST.get("requirement"):
        requirement = request.POST.get("requirement")
        requirement = Requirement.objects.get(id=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        comments = RequirementComment.objects.filter(requirement=requirement).order_by(
            "-id"
        )
        requirementRate = RequirementRate.objects.filter(
            requirement=requirement, star_rate__rated_by=member
        )
        rates = RequirementRate.objects.filter(requirement=requirement).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        likes = RequirementLike.objects.filter(requirement=requirement).count()
        dislikes = RequirementDislike.objects.filter(requirement=requirement).count()
        rate_data = requirement_rates(request,requirement_id=requirement_id)
        if requirement.created_by == member:
           creator = "me"
        else:
           creator = "not me"
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
                'creator':creator,
                "rates": rates,
                "likes": likes,
                "dislikes": dislikes,
                'rate_data':rate_data,
                "total_rates": total_rates,
                "requirementRate": requirementRate,
                "comments": comments,
                "total_comments": total_comments,
                "requirements": requirements,
                "requirement": requirement,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    rate_data = requirement_rates(request,requirement_id=requirement_id)
    if requirement.created_by == member:
       creator = "me"
    else:
        creator = "not me"
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
            "rates": rates,
            "likes": likes,
            'creator':creator,
            'rate_data':rate_data,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "comments": comments,
            "total_comments": total_comments,
            "requirementRate": requirementRate,
            "requirements": requirements,
            "requirement": requirement,
            "message": message,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
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
    if request.method == "POST":
        requirement_title = request.POST.get("requirement_title")
        description = request.POST.get("requirement_descriptions")
        created_by = Member.objects.get(user=request.user)
        scenarios = request.POST.get_list('scenario')
        processes = request.POST.get_list('process')
        usecase = request.POST.get_list('usecase')


        # then creating requirement
      
        requirement = Requirement.objects.create(
            name=requirement_title,
            created_by=created_by,
            description=description,
            goal=goal,
            project=project,
            )
        requirement.save()
        # then adding requirement to scenario
        for _scenario in scenarios:
            _scenario = Scenario.objects.get(id=_scenario)
            _scenario.requirement.add(requirement)
        for _process in processes:
            _process = Process.objects.get(id=_process)
            _process.requirement.add(requirement)
        for _usecase in usecases:
            _usecase = UseCase.objects.get(id=usecase)
            _usecase.requirement.add(requirement)

        if requirement:

            return redirect("projects:requirements", goal_id=goal.id)

    return render(
        request,
        "projects/requirements/create_requirement.html",
        {
            "indexhead": indexhead,
            "goal_id": goal_id,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def scenarios(request, requirement_id):
    indexhead = "Requirement-Scenarios"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        requirement_id = request.POST.get("requirement")
        requirement = Requirement.objects.get(id=requirement_id)
        goal = Goal.objects.get(id=requirement.goal.id)
        requirements = Requirement.objects.filter(goal=goal).order_by('-id')
        scenarios = RequirementScenario.objects.filter(requirement__id=requirement_id).order_by('-id')
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
                'requirement':requirement,
                "viewpoints": viewpoints,
                "scenarios": scenarios,
                "goals": goals,
                "requirement_id": requirement_id,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    requirements = Requirement.objects.filter(goal=goal)
    scenarios = RequirementScenario.objects.filter(requirement__id=requirement_id).order_by('-id')
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
            "scenarios": scenarios,
            "viewpoints": viewpoints,
            'requirement':requirement,
            "goals": goals,
            "requirement_id": requirement_id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewscenario(request, scenario_id=None, message=None):
    indexhead = "Scenario Description"
    member = Member.objects.get(user=request.user)
    scenario = RequirementScenario.objects.get(id=scenario_id)
    comments = ScenarioComment.objects.filter(scenario=scenario.scenario).order_by("-id")
    scenarioRate = ScenarioRate.objects.filter(
        scenario=scenario.scenario, star_rate__rated_by=member
    )
    rates = ScenarioRate.objects.filter(scenario=scenario.scenario).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = ScenarioLike.objects.filter(scenario=scenario.scenario).count()
    dislikes = ScenarioDislike.objects.filter(scenario=scenario.scenario).count()

    if request.POST.get("scenario"):
        scenario_id = request.POST.get("scenario")
        scenarios = RequirementScenario.objects.filter(requirement=scenario.requirement)
        
        requirement = Requirement.objects.get(id=scenario.requirement.id)
        scenario = RequirementScenario.objects.get(id=scenario_id)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        comments = ScenarioComment.objects.filter(scenario=scenario.scenario).order_by("-id")
        scenarioRate = ScenarioRate.objects.filter(
            scenario=scenario.scenario, star_rate__rated_by=member
        )
        rates = ScenarioRate.objects.filter(scenario=scenario.scenario).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        likes = ScenarioLike.objects.filter(scenario=scenario.scenario).count()
        dislikes = ScenarioDislike.objects.filter(scenario=scenario.scenario).count()
        rate_data = scenario_rates(request,scenario_id=scenario.scenario.id)
        if scenario.scenario.created_by == member:
           creator = "me"
        else:
            creator = "not me"

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
                'creator':creator,
                "scenarios": scenarios,
                'requirement':scenario.requirement,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                "rates": rates,
                "likes": likes,
                'rate_data':rate_data,
                "dislikes": dislikes,
                "total_rates": total_rates,
                "comments": comments,
                "total_comments": total_comments,
                "scenarioRate": scenarioRate,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = RequirementScenario.objects.filter(requirement=scenario.requirement)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    rate_data = scenario_rates(request,scenario_id=scenario.scenario.id)
    if scenario.scenario.created_by == member:
       creator = "me"
    else:
        creator = "not me"
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
            "viewpoints": viewpoints,
            "scenarios": scenarios,
            'rate_data':rate_data,
            "requirements": requirements,
            'requirement':requirement,
            "requirement_id": requirement.id,
            "rates": rates,
            "likes": likes,
            'creator':creator,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "comments": comments,
            "total_comments": total_comments,
            "scenarioRate": scenarioRate,
            "message": message,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createScenario(request, requirement_id):
    indexhead = "Create Scenario"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    requirements = Requirement.objects.filter(goal=goal).order_by('-id')
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == "POST":
        scenario_title = request.POST.get("scenario_title")
        description = request.POST.get("scenario_descriptions")
        created_by = Member.objects.get(user=request.user)
        requirement_ = request.POST.getlist('requirement')

        # then creating requirement
    
        scenario = Scenario.objects.create(
            name=scenario_title,
            created_by=created_by,
            description=description,
            project=project,
        )
        scenario.save()

        # then adding Requirement
        if requirement_ != None or requirement_!= "":
            for require in requirement_:
                require = Requirement.objects.get(id=require)
                requirescenario = RequirementScenario.objects.create(requirement=require,scenario=scenario)
                requirescenario.save()
        else:
            require = Requirement.objects.get(id=requirement_id)
            requirescenario = RequirementScenario.objects.create(requirement=require,scenario=scenario)
            requirescenario.save()

        if scenario:
            return redirect("projects:scenarios", requirement_id=requirement.id)
    return render(
        request,
        "projects/scenario/create_scenario.html",
        {
            "indexhead": indexhead,
            "requirement": requirement,
            "viewpoints": viewpoints,
            'requirements':requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def processes(request, requirement_id):
    indexhead = "Scenario-Processes"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        requirement_id = request.POST.get("requirement")
        processes = RequirementProcess.objects.filter(requirement__id=requirement_id).order_by('-id')
        requirement = Requirement.objects.get(id=requirement_id)
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
                "scenarios": scenarios,
                "processes": processes,
                "goals": goals,
                "requirement_id": requirement.id,
                "requirement": requirement,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    requirements = Requirement.objects.filter(goal=goal)
    scenarios = Scenario.objects.filter(requirement_id=requirement.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    goals = Goal.objects.filter(viewpoint=viewpoint)
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    project_id = project.id
    processes = RequirementProcess.objects.filter(requirement__id=requirement_id).order_by('-id')
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            "scenarios": scenarios,
            "viewpoints": viewpoints,
            "requirement": requirement,
            "goals": goals,
            "processes": processes,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewprocess(request, process_id=None, message=None):
    indexhead = "Process Description"
    member = Member.objects.get(user=request.user)
    process = Process.objects.get(id=process_id)
    comments = ProcessComment.objects.filter(process=process).order_by("-id")
    processRate = ProcessRate.objects.filter(
        process=process, star_rate__rated_by=member
    )
    rates = ProcessRate.objects.filter(process=process).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = ProcessLike.objects.filter(process=process).count()
    dislikes = ProcessDislike.objects.filter(process=process).count()
    if request.POST.get("process"):
        process_id = request.POST.get("process")
        process = Process.objects.get(id=process_id)
        scenario = Scenario.objects.get(id=process.scenario.id)
        processes = Process.objects.filter(scenario=scenario).order_by("-id")
        requirement = Requirement.objects.get(id=scenario.requirement.id)
        scenarios = Scenario.objects.filter(requirement=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        project_id = project.id
        comments = ProcessComment.objects.filter(process=process).order_by("-id")
        processRate = ProcessRate.objects.filter(
            process=process, star_rate__rated_by=member
        )
        rates = ProcessRate.objects.filter(process=process).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        likes = ProcessLike.objects.filter(process=process).count()
        dislikes = ProcessDislike.objects.filter(process=process).count()
        rate_data = process_rates(request, process_id=process_id)
        if process.created_by == member:
           creator = "me"
        else:
            creator = "not me"
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
                "process": process,
                "scenarios": scenarios,
                "rates": rates,
                'creator':creator,
                "likes": likes,
                "dislikes": dislikes,
                "total_rates": total_rates,
                "processRate": processRate,
                "comments": comments,
                'rate_data':rate_data,
                "total_comments": total_comments,
                "processes": processes,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario).order_by("-id")
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    project_id = project.id
    rate_data = process_rates(request, process_id=process_id)
    if process.created_by == member:
        creator = "me"
    else:
        creator = "not me"
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
            "process": process,
            'rate_data':rate_data,
            'creator':creator,
            "viewpoints": viewpoints,
            "processes": processes,
            "scenarios": scenarios,
            "requirements": requirements,
            "requirement_id": requirement.id,
            "rates": rates,
            "likes": likes,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "processRate": processRate,
            "comments": comments,
            "total_comments": total_comments,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createProcess(request, requirement_id):
    indexhead = "Create Process"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    scenario = Scenario.objects.get(id=viewpoint.project.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project).order_by("-id")
    requirements = Requirement.objects.filter(goal=goal).order_by('-id')
    if request.method == "POST":
        process_title = request.POST.get("process_title")
        description = request.POST.get("process_descriptions")
        created_by = Member.objects.get(user=request.user)
        require = request.POST.getlist('requirement')

       
        process = Process.objects.create(
            process_name=process_title,
            created_by=created_by,
            description=description,
            project=project,
        )
        process.save()

        # adding requirement to process many to many process
        if require != None or require != "":
            for require in require:
                require = Requirement.objects.get(id=require)
                requireprocess = RequirementProcess.objects.create(requirement=require,process=process)
                requireprocess.save()

        else:
            require = Requirement.objects.get(id=requirement_id)
            requireprocess = RequirementProcess.objects.create(requirement=require,process=process)
            requireprocess.save()

        if process:
            return redirect("projects:processes", requirement_id=requirement_id)

    return render(
        request,
        "projects/process/create_process.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "project_id": project.id,
            'requirements':requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def usecases(request, requirement_id):
    indexhead = "Process-Usecases"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        requirement_id = request.POST.get("requirement")
        usecases = RequirementUsecase.objects.filter(requirement__id=requirement_id).order_by("-id")
        requirement = Requirement.objects.get(id=requirement_id)
        goal = Goal.objects.get(id=requirement.goal.id)
        requirements = Requirement.objects.filter(goal=goal).order_by('-id')
        requirements = Requirement.objects.filter(goal=goal)
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
                'requirement':requirement,
                "goals": goals,
                "usecases": usecases,
                "requirement_id": requirement.id,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )


    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    usecases = RequirementUsecase.objects.filter(requirement__id=requirement_id).order_by("-id")
    requirements = Requirement.objects.filter(goal=goal).order_by('-id')
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
            'requirement':requirement,
            "requirements": requirements,
            "scenarios": scenarios,
            "viewpoints": viewpoints,
            "goals": goals,
            "usecases": usecases,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewusecase(request, usecase_id=None, message=None):
    indexhead = "Usecase Description"
    member = Member.objects.get(user=request.user)
    usecase = UseCase.objects.get(id=usecase_id)
    comments = UseCaseComment.objects.filter(usecase=usecase).order_by("-id")
    usecaseRate = UseCaseRate.objects.filter(
        usecase=usecase, star_rate__rated_by=member
    )
    rates = UseCaseRate.objects.filter(usecase=usecase).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = UseCaseLike.objects.filter(use_case=usecase).count()
    dislikes = UseCaseDislike.objects.filter(use_case=usecase).count()
    if request.POST.get("usecase"):
        usecase_id = request.POST.get("usecase")
        usecase = UseCase.objects.get(id=usecase_id)
        process = Process.objects.get(id=usecase.process.id)
        scenario = Scenario.objects.get(id=process.scenario.id)
        processes = Process.objects.filter(scenario=scenario).order_by("-id")
        requirement = Requirement.objects.get(id=scenario.requirement.id)
        scenarios = Scenario.objects.filter(requirement=requirement)
        goal = Goal.objects.get(requirement=requirement)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        requirements = Requirement.objects.filter(goal=goal).order_by("-id")
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(project=project)
        usecases = UseCase.objects.filter(process=process).order_by("-id")
        likes = UseCaseLike.objects.filter(use_case=usecase).count()
        dislikes = UseCaseDislike.objects.filter(use_case=usecase).count()
        project_id = project.id
        comments = UseCaseComment.objects.filter(usecase=usecase).order_by("-id")
        usecaseRate = UseCaseRate.objects.filter(
            usecase=usecase, star_rate__rated_by=member
        )
        rates = UseCaseRate.objects.filter(usecase=usecase).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        rate_data = usecase_rates(request,usecase_id=usecase_id)
        if usecase.created_by == member:
            creator = "me"
        else:
            creator = "not me"
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
                "process": process,
                'creator':creator,
                "process_id": process.id,
                "scenarios": scenarios,
                "processes": processes,
                "usecase": usecase,
                "usecases": usecases,
                "usecase_id": usecase.id,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                "rates": rates,
                "likes": likes,
                'rate_data':rate_data,
                "dislikes": dislikes,
                "total_rates": total_rates,
                "usecaseRate": usecaseRate,
                "comments": comments,
                "total_comments": total_comments,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    process = Process.objects.get(id=usecase.process.id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario).order_by("-id")
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(requirement=requirement)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    requirements = Requirement.objects.filter(goal=goal).order_by("-id")
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=viewpoint.project.id)
    viewpoints = Viewpoint.objects.filter(project=project)
    usecases = UseCase.objects.filter(process=process).order_by("-id")
    project_id = project.id
    rate_data = usecase_rates(request,usecase_id=usecase_id)
    if usecase.created_by == member:
        creator = "me"
    else:
        creator = "not me"
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
            "process": process,
            "message": message,
            'creator':creator,
            'rate_data':rate_data,
            "viewpoints": viewpoints,
            "processes": processes,
            "scenarios": scenarios,
            "usecase": usecase,
            "usecases": usecases,
            "usecase_id": usecase_id,
            "process_id": process.id,
            "requirements": requirements,
            "requirement_id": requirement.id,
            "rates": rates,
            "likes": likes,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "usecaseRate": usecaseRate,
            "comments": comments,
            "total_comments": total_comments,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createUsecase(request, requirement_id):
    indexhead = "Create Usecase"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    viewpoint_id = viewpoint.id
    goals = Goal.objects.filter(viewpoint=viewpoint)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    requirements = Requirement.objects.filter(goal=goal).order_by('-id')
    if request.method == "POST":
        usecase_title = request.POST.get("usecase_title")
        description = request.POST.get("usecase_descriptions")
        created_by = Member.objects.get(user=request.user)
        require = request.POST.getlist('requirement')

        # then creating requirement
        
        usecase = UseCase.objects.create(
            usecase_name=usecase_title,
            created_by=created_by,
            description=description,
            project=project,
        )
        usecase.save()

        # Then adding requirement:
        if require != None or require != "":
            for require in require:
                require = Requirement.objects.get(id=require)
                requireusecase = RequirementUsecase.objects.create(
                    requirement=require,usecase=usecase
                )
                requireusecase.save()
        else:
            require = Requirement.objects.get(id=requirement_id)
            requireusecase = RequirementUsecase.objects.create(
                    requirement=require,usecase=usecase
                )
            requireusecase.save()


        if usecase:
            return redirect("projects:usecases", requirement_id=requirement)

    return render(
        request,
        "projects/usecase/create_usecase.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "requirement_id": requirement_id,
            "member": member,
            "project": project,
            'requirements':requirements,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# Rate


@login_required(login_url="login")
def projectRate(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if ProjectMembership.objects.filter(project=project,member=member, status="active").exists():
        if request.POST.get("rate") != None:

            if not ProjectRate.objects.filter(
                project=project, star_rate__rated_by=member
            ).exists():
                rate = StarRate.objects.create(
                    rated_by=member, number_of_stars=request.POST.get("rate")
                )
                rate.save()
                if rate:
                    project_rate = ProjectRate.objects.create(
                        project=project, star_rate=rate
                    )
                    project_rate.save()
                    if project_rate:
                        return redirect("projects:viewproject", project_id=project_id)
            message = (
                "sorry you have already rated this project you can not rate this again"
            )
            return redirect("projects:viewproject", project_id=project_id, message=message)
        message = "sorry you can not rate zero star, rate start from one star !!"
        return redirect("projects:viewproject", project_id=project_id, message=message)
    message = "sorry you can not Rate on this project now,you are not a active member of this project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def viewpointRate(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(viewpoint=viewpoint)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ViewPointRate.objects.filter(
            view_point=viewpoint, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                viewpoint_rate = ViewPointRate.objects.create(
                    view_point=viewpoint, star_rate=rate
                )
                viewpoint_rate.save()
                if viewpoint_rate:
                    project_id = viewpoint.project.id
                    return redirect(
                        "projects:viewpoint",
                        viewpoint_id=viewpoint_id
                    )

        message = "sorry you have already rated this Viewpoint you can not rate again"
        return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewpont", viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def goalRate(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not GoalRate.objects.filter(goal=goal, star_rate__rated_by=member).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                goal_rate = GoalRate.objects.create(goal=goal, star_rate=rate)
                goal_rate.save()
                if goal_rate:
                    return redirect("projects:viewgoal", goal_id=goal.id)

        message = "sorry you have already rated this Goal you can not rate it again"
        return redirect("projects:viewgoal", goal_id=goal.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewgoal", goal_id=goal.id)


@login_required(login_url="login")
def requirementRate(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not RequirementRate.objects.filter(
            requirement=requirement, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                requirement_rate = RequirementRate.objects.create(
                    requirement=requirement, star_rate=rate
                )
                requirement_rate.save()
                if requirement_rate:
                    return redirect(
                        "projects:viewrequirement", requirement_id=requirement.id
                    )

        message = (
            "sorry you have already rated this requirement you can not rate it again"
        )
        return redirect("projects:viewrequirement", requirement_id=requirement.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewrequirement", requirement_id=requirement.id)


@login_required(login_url="login")
def scenarioRate(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ScenarioRate.objects.filter(
            scenario=scenario.scenario, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                scenario_rate = ScenarioRate.objects.create(
                    scenario=scenario.scenario, star_rate=rate
                )
                scenario_rate.save()
                if scenario_rate:
                    return redirect("projects:viewscenario", scenario_id=scenario.id)

        message = "sorry you have already rated this Scenario you can not rate it again"
        return redirect("projects:viewscenario", scenario_id=scenario.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewscenario", scenario_id=scenario.id)


@login_required(login_url="login")
def processRate(request, process_id):
    process = Process.objects.get(id=process_id)
    # project = Project.objects.get(id=process.scenario.goal.requiremt.project.id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ProcessRate.objects.filter(
            process=process, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                process_rate = ProcessRate.objects.create(
                    process=process, star_rate=rate
                )
                process_rate.save()
                if process_rate:
                    return redirect("projects:viewprocess", process_id=process.id)

        message = "sorry you have already rated this process you can not rate it again"
        return redirect("projects:viewprocess", process_id=process.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewprocess", process_id=process.id)


@login_required(login_url="login")
def usecaseRate(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    # project = Project.objects.get(id=process.scenario.goal.requiremt.project.id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not UseCaseRate.objects.filter(
            usecase=usecase, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                usecase_rate = UseCaseRate.objects.create(
                    usecase=usecase, star_rate=rate
                )
                usecase_rate.save()
                if usecase_rate:
                    return redirect("projects:viewusecase", usecase_id=usecase.id)

        message = "sorry you have already rated this Usecase you can not rate it again"
        return redirect("projects:viewusecase", usecase_id=usecase.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewusecase", usecase_id=usecase.id)


# resources functions for all from project to usecase
@login_required(login_url="login")
def viewDocumentResource(request, resource_id):
    indexhead = "Project Resources:"
    hidesearch = "hide"
    resources = Repository.objects.filter(id=resource_id).order_by("-id")
    member = Member.objects.get(user=request.user)
    document = "document"
    return render(
        request,
        "projects/viewpoints/view_resource.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "resources": resources,
            "member": member,
            "document": document,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewImageResource(request, resource_id):
    indexhead = "Project Resources:"
    hidesearch = "hide"
    resources = Repository.objects.filter(id=resource_id).order_by("-id")
    member = Member.objects.get(user=request.user)
    image = "image"
    return render(
        request,
        "projects/viewpoints/view_resource.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "resources": resources,
            "member": member,
            "image": image,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewLinkResource(request, resource_id):
    indexhead = "Project Resources:"
    hidesearch = "hide"
    resources = Repository.objects.filter(id=resource_id).order_by("-id")
    member = Member.objects.get(user=request.user)
    link = "link"
    return render(
        request,
        "projects/viewpoints/view_resource.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "resources": resources,
            "member": member,
            "link": link,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def projectResources(request, project_id):
    indexhead = "Project Resources:"
    hidesearch = "hide"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if ProjectMembership.objects.filter(project=project,member=member,status="active").exists():
    
        resources = ProjectRepository.objects.filter(project=project).order_by("-id")
        project_id = project.id
        return render(
            request,
            "projects/viewpoints/resources.html",
            {
                "indexhead": indexhead,
                "hidesearch": hidesearch,
                "viewpoints": viewpoints,
                "project_id": project_id,
                "resources": resources,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    message = "Sorry you can not access Project Resources, you are not a active member of this Project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def viewpointResources(request, viewpoint_id):
    indexhead = "Viewpoint Resources:"
    hidesearch = "hide"
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    resources = ViewpointRepository.objects.filter(viewpoint=viewpoint).order_by("-id")
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=viewpoint.project.id)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoint": viewpoint,
            "viewpoints": viewpoints,
            "resources": resources,
            "viewpoint_id": viewpoint_id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def goalResources(request, goal_id):
    indexhead = "Goal Resources:"
    hidesearch = "hide"
    goal = Goal.objects.get(id=goal_id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = GoalRepository.objects.filter(goal=goal).order_by("-id")
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "resources": resources,
            "goal_id": goal.id,
            "goal": goal,
            "viewpoint": viewpoint,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def requirementResources(request, requirement_id):
    indexhead = "Requirement Resources:"
    hidesearch = "hide"
    requirement = Requirement.objects.get(id=requirement_id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = RequirementRepository.objects.filter(requirement=requirement).order_by(
        "-id"
    )
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "resources": resources,
            "requirement_id": requirement.id,
            "requirement": requirement,
            "viewpoint": viewpoint,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def scenarioResources(request, scenario_id):
    indexhead = "Scenario Resources:"
    hidesearch = "hide"
    scenario = RequirementScenario.objects.get(id=scenario_id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = ScenarioRepository.objects.filter(scenario=scenario.scenario).order_by("-id")
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "resources": resources,
            "requirement": requirement,
            "scenario_id": scenario.id,
            "scenario": scenario.scenario,
            "viewpoint": viewpoint,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def processResources(request, process_id):
    indexhead = "Process Resources:"
    hidesearch = "hide"
    process = Process.objects.get(id=process_id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = ProcessRepository.objects.filter(process=process).order_by("-id")
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "resources": resources,
            "requirement": requirement,
            "viewpoint": viewpoint,
            "process": process,
            "process_id": process.id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def usecaseResources(request, usecase_id):
    indexhead = "Usecase Resources:"
    hidesearch = "hide"
    usecase = UseCase.objects.get(id=usecase_id)
    process = Process.objects.get(id=usecase.process.id)
    scenario = Scenario.objects.get(id=process.scenario.id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = UsecaseRepository.objects.filter(usecase=usecase).order_by("-id")
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "resources": resources,
            "requirement": requirement,
            "usecase_id": usecase.id,
            "usecase": usecase,
            "viewpoint": viewpoint,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def addProjectResources(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            projectrepository = ProjectRepository.objects.create(
                project=project, repository=repository
            )
            projectrepository.save()
            if projectrepository:
                return redirect("projects:projectresources", project_id)
    return redirect("projects:projectresources", project_id)


@login_required(login_url="login")
def addViewpointResources(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            viewpointrepository = ViewpointRepository.objects.create(
                viewpoint=viewpoint, repository=repository
            )
            viewpointrepository.save()
            if viewpointrepository:
                return redirect("projects:viewpointresources", viewpoint_id)
    return redirect("projects:viewpontresources", viewpoint_id)


@login_required(login_url="login")
def addGoalResources(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            goalrepository = GoalRepository.objects.create(
                goal=goal, repository=repository
            )
            goalrepository.save()
            if goalrepository:
                return redirect("projects:goalresources", goal_id)
    return redirect("projects:goalresources", goal_id)


@login_required(login_url="login")
def addRequirementResources(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            requirementrepository = RequirementRepository.objects.create(
                requirement=requirement, repository=repository
            )
            requirementrepository.save()
            if requirementrepository:
                return redirect("projects:requirementresources", requirement_id)
    return redirect("projects:requirementresources", requirement_id)


@login_required(login_url="login")
def addScenarioResources(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        description = request.POST.get("description")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            scenariorepository = ScenarioRepository.objects.create(
                scenario=scenario.scenario, repository=repository
            )
            scenariorepository.save()
            if scenariorepository:
                return redirect("projects:scenarioresources", scenario_id)
    return redirect("projects:scenarioresources", scenario_id)


@login_required(login_url="login")
def addProcessResources(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            processrepository = ProcessRepository.objects.create(
                process=process, repository=repository
            )
            processrepository.save()
            if processrepository:
                return redirect("projects:processresources", process_id)
    return redirect("projects:processresources", process_id)


@login_required(login_url="login")
def addUsecaseResources(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        description = request.POST.get("description")
        repository = Repository.objects.create(
            added_by=member,
            image=image,
            links=links,
            docs=docs,
            description=description,
        )
        repository.save()
        if repository:
            usecaserepository = UsecaseRepository.objects.create(
                usecase=usecase, repository=repository
            )
            usecaserepository.save()
            if usecaserepository:
                return redirect("projects:usecaseresources", usecase_id)
    return redirect("projects:usecaseresources", usecase_id)


@login_required(login_url="login")
def goalComment(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        goal_comment = GoalComment.objects.create(comment=create_comment, goal=goal)
        goal_comment.save()
        if goal_comment:
            if goal.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(goal.created_by)
                    + " You have one new comment on "
                    + str(goal)
                    + " goal from "
                    + str(member)
                )
                notify(
                    request, affected_user=goal.created_by, activity=activity, link=link
                )
                return redirect("projects:viewgoal", goal_id=goal_id)
    return redirect("projects:viewgoal", goal_id=goal_id)


@login_required(login_url="login")
def requirementComment(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        requirement_comment = RequirementComment.objects.create(
            comment=create_comment, requirement=requirement
        )
        requirement_comment.save()
        if requirement_comment:
            if requirement.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(requirement.created_by)
                    + " You have one new comment on "
                    + str(requirement)
                    + " Requirement from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=requirement.created_by,
                    activity=activity,
                    link=link,
                )
                return redirect(
                    "projects:viewrequirement", requirement_id=requirement_id
                )
    return redirect("projects:viewrequirement", requirement_id=requirement_id)


@login_required(login_url="login")
def scenarioComment(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        scenario_comment = ScenarioComment.objects.create(
            comment=create_comment, scenario=scenario.scenario
        )
        scenario_comment.save()
        if scenario_comment:
            if scenario.scenario.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(scenario.created_by)
                    + " You have one new comment on "
                    + str(scenario.scenario)
                    + " Scenario from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=scenario.created_by,
                    activity=activity,
                    link=link,
                )
                return redirect("projects:viewscenario", scenario_id=scenario_id)
    return redirect("projects:viewscenario", scenario_id=scenario_id)


@login_required(login_url="login")
def processComment(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        process_comment = ProcessComment.objects.create(
            comment=create_comment, process=process
        )
        process_comment.save()
        if process_comment:
            if process.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(process.created_by)
                    + " You have one new comment on "
                    + str(process)
                    + " Process from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=process.created_by,
                    activity=activity,
                    link=link,
                )
                return redirect("projects:viewprocess", process_id=process_id)
    return redirect("projects:viewprocess", process_id=process_id)


@login_required(login_url="login")
def usecaseComment(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        usecase_comment = UseCaseComment.objects.create(
            comment=create_comment, usecase=create_comment
        )
        usecase_comment.save()
        if usecase_comment:
            if usecase.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(usecase.created_by)
                    + " You have one new comment on "
                    + str(usecase)
                    + " Use Case from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=usecase.created_by,
                    activity=activity,
                    link=link,
                )
                return redirect("projects:viewusecase", usecase_id=usecase_id)
    return redirect("projects:viewusecase", usecase_id=usecase_id)


@login_required(login_url="login")
def usecaseComment(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        create_comment = Comment.objects.create(comment=comment, commented_by=member)
        create_comment.save()
        usecase_comment = UseCaseComment.objects.create(
            comment=create_comment, usecase=usecase
        )
        usecase_comment.save()
        return redirect("projects:viewusecase", usecase_id=usecase_id)
    return redirect("projects:viewusecase", usecase_id=usecase_id)


# Notifcations at the top of pages
@login_required(login_url="login")
def notify(request, affected_user=None, activity=None, link=None):
    user = request.user
    create_activity = ActivityLog.objects.create(
        user=user,
        affected_user=affected_user,
        activity=activity,
        link=link,
        status="not seen",
    )
    create_activity.save()


@login_required(login_url="login")
def readNotifications(request):
    member = Member.objects.get(user=request.user)
    read_all = ActivityLog.objects.filter(affected_user=member).update(status="seen")

    return redirect("projects:profile")


def subscribe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subscribe = Subscriber.objects.create(
            fullname=name, email=email, message=message
        )
        subscribe.save()
        if subscribe:
            message = (
                "Thanks  "
                + name
                + " for being a part of CORES, your message has been sent"
            )
            return indexs(request, message=message)
    return indexs(request)


@login_required(login_url="login")
def search(request, placeholder):
    keyword = request.POST.get("seaarch")
    if placeholder == "search project":
        projects = Project.objects.filter(
            project_title__icontains=keyword, description__icontains=keyword
        )

    if placeholder == "search member":
        pass


# Like functions from project to usecase

# Like functions from project to usecase
@login_required(login_url="login")
def my_project_like(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)

    if not ProjectLike.objects.filter(project=project, like__liked_by=member).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            project_like = ProjectLike.objects.create(like=like, project=project)
            project_like.save()
            if project_like:
                return redirect("projects:viewmyproject", project_id=project_id)

        return redirect("projects:viewmyproject", project_id=project_id)
    unlike = ProjectLike.objects.filter(project=project, like__liked_by=member).delete()
    return redirect("projects:viewmyproject", project_id=project_id)


@login_required(login_url="login")
def project_like(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if ProjectMembership.objects.filter(project=project,member=member, status="active").exists():
        if not ProjectLike.objects.filter(project=project, like__liked_by=member).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:

                # then creating project_like
                project_like = ProjectLike.objects.create(like=like, project=project)
                project_like.save()
                if project_like:
                    return redirect("projects:viewproject", project_id=project_id)

            return redirect("projects:viewproject", project_id=project_id)
        unlike = ProjectLike.objects.filter(project=project, like__liked_by=member).delete()
        return redirect("projects:viewproject", project_id=project_id)
    message = "sorry you can not like on this project now,you are not a active member of this project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def viewpoint_like(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    member = Member.objects.get(user=request.user)

    if not ViewpointLike.objects.filter(
        view_point=viewpoint, like__liked_by=member
    ).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            viewpoint_like = ViewpointLike.objects.create(
                like=like, view_point=viewpoint
            )
            viewpoint_like.save()
            if viewpoint_like:
                return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)

        return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)
    unlike = ViewpointLike.objects.filter(
        view_point=viewpoint, like__liked_by=member
    ).delete()
    return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def goal_like(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if not GoalLike.objects.filter(goal=goal, like__liked_by=member).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            goal_like = GoalLike.objects.create(like=like, goal=goal)
            goal_like.save()
            if goal_like:
                return redirect("projects:viewgoal", goal_id=goal_id)

        return redirect("projects:viewgoal", goal_id=goal_id)
    unlike = GoalLike.objects.filter(goal=goal, like__liked_by=member).delete()
    return redirect("projects:viewgoal", goal_id=goal_id)


@login_required(login_url="login")
def requirement_like(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if not RequirementLike.objects.filter(
        requirement=requirement, like__liked_by=member
    ).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            requirement_like = RequirementLike.objects.create(
                like=like, requirement=requirement
            )
            requirement_like.save()
            if requirement_like:
                return redirect(
                    "projects:viewrequirement", requirement_id=requirement_id
                )

        return redirect("projects:viewrequirement", requirement_id=requirement_id)
    unlike = RequirementLike.objects.filter(
        requirement=requirement, like__liked_by=member
    ).delete()
    return redirect("projects:viewrequirement", requirement_id=requirement_id)


@login_required(login_url="login")
def scenario_like(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if not ScenarioLike.objects.filter(
        scenario=scenario.scenario, like__liked_by=member
    ).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            scenario_like = ScenarioLike.objects.create(like=like, scenario=scenario.scenario)
            scenario_like.save()
            if scenario_like:
                return redirect("projects:viewscenario", scenario_id=scenario_id)

        return redirect("projects:viewscenario", scenario_id=scenario_id)
    unlike = ScenarioLike.objects.filter(
        scenario=scenario.scenario, like__liked_by=member
    ).delete()
    return redirect("projects:viewscenario", scenario_id=scenario_id)


@login_required(login_url="login")
def process_like(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if not ProcessLike.objects.filter(process=process, like__liked_by=member).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            process_like = ProcessLike.objects.create(like=like, process=process)
            process_like.save()
            if process_like:
                return redirect("projects:viewprocess", process_id=process_id)

        return redirect("projects:viewprocess", process_id=process_id)
    unlike = ProcessLike.objects.filter(process=process, like__liked_by=member).delete()
    return redirect("projects:viewprocess", process_id=process_id)


@login_required(login_url="login")
def usecase_like(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if not UseCaseLike.objects.filter(use_case=usecase, like__liked_by=member).exists():
        like = Like.objects.create(like=True, liked_by=member)
        like.save()
        if like:

            # then creating project_like
            usecase_like = UseCaseLike.objects.create(like=like, use_case=usecase)
            usecase_like.save()
            if usecase_like:
                return redirect("projects:viewusecase", usecase_id=usecase_id)

        return redirect("projects:viewusecase", usecase_id=usecase_id)
    unlike = UseCaseLike.objects.filter(
        use_case=usecase, like__liked_by=member
    ).delete()
    return redirect("projects:viewusecase", usecase_id=usecase_id)


# Dislike functions from project to usecase
@login_required(login_url="login")
def my_project_dislike(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    
    if not ProjectDislike.objects.filter(
        project=project, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            project_dislike = ProjectDislike.objects.create(
                dislike=dislike, project=project
            )
            project_dislike.save()
            if project_dislike:
                return redirect("projects:viewmyproject", project_id=project_id)

        return redirect("projects:viewmyproject", project_id=project_id)
    unlike = ProjectDislike.objects.filter(
        project=project, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewmyproject", project_id=project_id)


@login_required(login_url="login")
def project_dislike(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if ProjectMembership.objects.filter(project=project,member=member, status="active").exists():
        if not ProjectDislike.objects.filter(
            project=project, dislike__disliked_by=member
        ).exists():
            dislike = Dislike.objects.create(dislike=True, disliked_by=member)
            dislike.save()
            if dislike:

                # then creating project_like
                project_dislike = ProjectDislike.objects.create(
                    dislike=dislike, project=project
                )
                project_dislike.save()
                if project_dislike:
                    return redirect("projects:viewproject", project_id=project_id)

            return redirect("projects:viewproject", project_id=project_id)
        unlike = ProjectDislike.objects.filter(
            project=project, dislike__disliked_by=member
        ).delete()
        return redirect("projects:viewproject", project_id=project_id)
    message = "sorry you can not dislike on this project now,you are not a active member of this project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def viewpoint_dislike(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    member = Member.objects.get(user=request.user)

    if not ViewpointDislike.objects.filter(
        view_point=viewpoint, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            viewpoint_dislike = ViewpointDislike.objects.create(
                dislike=dislike, view_point=viewpoint
            )
            viewpoint_dislike.save()
            if viewpoint_dislike:
                return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)

        return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)
    unlike = ViewpointDislike.objects.filter(
        view_point=viewpoint, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def goal_dislike(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if not GoalDislike.objects.filter(goal=goal, dislike__disliked_by=member).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            goal_dislike = GoalDislike.objects.create(dislike=dislike, goal=goal)
            goal_dislike.save()
            if goal_dislike:
                return redirect("projects:viewgoal", goal_id=goal_id)

        return redirect("projects:viewgoal", goal_id=goal_id)
    undislike = GoalDislike.objects.filter(
        goal=goal, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewgoal", goal_id=goal_id)


@login_required(login_url="login")
def requirement_dislike(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if not RequirementDislike.objects.filter(
        requirement=requirement, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            requirement_dislike = RequirementDislike.objects.create(
                dislike=dislike, requirement=requirement
            )
            requirement_dislike.save()
            if requirement_dislike:
                return redirect(
                    "projects:viewrequirement", requirement_id=requirement_id
                )

        return redirect("projects:viewrequirement", requirement_id=requirement_id)
    undislike = RequirementDislike.objects.filter(
        requirement=requirement, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewrequirement", requirement_id=requirement_id)


@login_required(login_url="login")
def scenario_dislike(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if not ScenarioDislike.objects.filter(
        scenario=scenario.scenario, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            scenario_dislike = ScenarioDislike.objects.create(
                dislike=dislike, scenario=scenario.scenario
            )
            scenario_dislike.save()
            if scenario_dislike:
                return redirect("projects:viewscenario", scenario_id=scenario_id)

        return redirect("projects:viewscenario", scenario_id=scenario_id)
    undislike = ScenarioDislike.objects.filter(
        scenario=scenario.scenario, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewscenario", scenario_id=scenario_id)


@login_required(login_url="login")
def process_dislike(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if not ProcessDislike.objects.filter(
        process=process, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_dislike
            process_dislike = ProcessDislike.objects.create(
                dislike=dislike, process=process
            )
            process_dislike.save()
            if process_dislike:
                return redirect("projects:viewprocess", process_id=process_id)

        return redirect("projects:viewprocess", process_id=process_id)
    undislike = ProcessDislike.objects.filter(
        process=process, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewprocess", process_id=process_id)


@login_required(login_url="login")
def usecase_dislike(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if not UseCaseDislike.objects.filter(
        use_case=usecase, dislike__disliked_by=member
    ).exists():
        dislike = Dislike.objects.create(dislike=True, disliked_by=member)
        dislike.save()
        if dislike:

            # then creating project_like
            usecase_dislike = UseCaseDislike.objects.create(
                dislike=dislike, use_case=usecase
            )
            usecase_dislike.save()
            if usecase_dislike:
                return redirect("projects:viewusecase", usecase_id=usecase_id)

        return redirect("projects:viewusecase", usecase_id=usecase_id)
    undislike = UseCaseDislike.objects.filter(
        use_case=usecase, dislike__disliked_by=member
    ).delete()
    return redirect("projects:viewusecase", usecase_id=usecase_id)


# global viewpoints to usecase
def general_goals(request, project_id):
    project = Project.objects.get(id=project_id)
    goals = Goal.objects.filter(project=project).order_by("-id")
    indexhead = "Project Goals"
    member = Member.objects.get(user=request.user)

    return render(
        request,
        "projects/Goals/goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "member": member,
            "project_id": project_id,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def general_requirements(request, project_id):
    indexhead = "Project Requirements"
    project = Project.objects.get(id=project_id)
    requirements = Requirement.objects.filter(project=project).order_by("-id")
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "requirements": requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def general_scenario(request, project_id):
    indexhead = "Project Scenarios"
    project = Project.objects.get(id=project_id)
    scenarios = RequirementScenario.objects.filter(requirement__project=project).order_by("-id")
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "member": member,
            "scenarios": scenarios,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def general_process(request, project_id):
    indexhead = "Project Process"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    processes = RequirementProcess.objects.filter(requirement__project=project).order_by("-id")
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "processes": processes,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def general_usecase(request, project_id):
    indexhead = "Project Use Cases"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    usecases = RequirementUsecase.objects.filter(requirement__project=project).order_by("-id")
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "usecases": usecases,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# project reports 
def my_project_reports(request,project_id):
    indexhead = "Project Reports"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    def user_reports(request, project_id):
        female_members = ProjectMembership.objects.filter(project=project, member__gender="Female").count()
        male_members = ProjectMembership.objects.filter(project=project, member__gender="Male").count()
        gender = [female_members,male_members]
        return gender
            

    def contribution_reports(request,project_id):

        viewpoints = Viewpoint.objects.filter(project=project).count()
        goals = Goal.objects.filter(project=project).count()
        requirements = Requirement.objects.filter(project=project).count()
        scenarios = Scenario.objects.filter(project=project).count()
        processes = Process.objects.filter(project=project).count()
        usecases = UseCase.objects.filter(project=project).count()
        contributions = [viewpoints,goals,requirements,scenarios,processes,usecases]
        return contributions

    return render(request,'projects/my_projects/general_reports.html',{
        'user_reports':user_reports(request,project_id=project_id),
        'contribution_reports':contribution_reports(request,project_id=project_id),
        'hidesearch':hidesearch,
        'project_id':project_id,
        'project':project,
        'member':member,
        'indexhead':indexhead

    })



def general_report(request):
    indexhead = "General Reports"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    def member_report(request):
        female = Member.objects.filter(gender="Female").count()
        male = Member.objects.filter(gender="Male").count()

        gender = [male,female]
        print(gender)
        return gender
    
    def Project_report(request):
        
        Invitational_projects = Project.objects.filter(is_invitational=True,is_discoverable=False).count()
        discoverable_projects = Project.objects.filter(is_discoverable=True,is_invitational=False).count()
        invitaional_and_discoverable = Project.objects.filter(is_invitational=True,is_discoverable=True).count()
        is_public = Project.objects.filter(project_visibility="public").count()
        my_projects = Project.objects.filter(created_by=member).count()

        projects = [Invitational_projects,discoverable_projects,invitaional_and_discoverable,is_public,my_projects]
        print(projects)
        return projects

       

    return render(request,'projects/general_reports.html',{
        'member_reports':member_report(request),
        'project_reports':Project_report(request),
        'hidesearch':hidesearch,
        'member':member,
        'indexhead':indexhead

    })



# Updating from Project to usecase
def update_viewpoint(request,viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    viewpoint_name = request.POST.get('viewpoint_name')
    viewpoint_photo = request.FILES.get('viewpoint_photo')
    description = request.POST.get('description')

    if viewpoint_photo == "" or viewpoint_photo == None:
        viewpoint_photo = viewpoint.viewpoint_photo

    
    # Then updating viewpoint
    update_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(
        viewpoint_name=viewpoint_name,
        viewpoint_photo=viewpoint_photo,
        description=description
    )
    if update_viewpoint:
        return redirect('projects:viewpoint', viewpoint_id=viewpoint_id)
    return redirect('projects:viewpoint', viewpoint_id=viewpoint_id)

def update_goal(request,goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal_name = request.POST.get('goal_name')
    description = request.POST.get('description')
    
    # Then updating goal
    update_goal = Goal.objects.filter(id=goal_id).update(
        goal_name=goal_name,
        description=description
    )
    if update_goal:
        return redirect('projects:viewgoal', goal_id=goal_id)
    return redirect('projects:viewgoal', goal_id=goal_id)

def update_requirement(request,requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    requirement_name = request.POST.get('requirement_name')
    description = request.POST.get('description')

    
    # Then updating requirement
    update_requirement = Requirement.objects.filter(id=requirement_id).update(
        name=requirement_name,
        description=description
    )
    if update_requirement:
        return redirect('projects:viewrequirement', requirement_id=requirement_id)
    return redirect('projects:viewrequirement', requirement_id=requirement_id)

def update_scenario(request,scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    scenario_name = request.POST.get('scenario_name')
    description = request.POST.get('description')
    
    # Then updating scenario
    update_scenario = Scenario.objects.filter(id=scenario_id).update(
        name=scenario_name,
        description=description
    )
    if update_scenario:
        return redirect('projects:viewscenario', scenario_id=scenario_id)
    return redirect('projects:viewscenario', scenario_id=scenario_id)

def update_process(request,process_id):
    process = Process.objects.get(id=process_id)
    process_name = request.POST.get('process_name')
    description = request.POST.get('description')
    
    # Then updating process
    update_process = Process.objects.filter(id=process_id).update(
        process_name=process_name,
        description=description
    )
    if update_process:
        return redirect('projects:viewprocess', process_id=process_id)
    return redirect('projects:viewprocess', process_id=process_id)

def update_usecase(request,usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    usecase_name = request.POST.get('usecase_name')
    description = request.POST.get('description')
    
    # Then updating usecase
    update_usecase = UseCase.objects.filter(id=usecase_id).update(
        usecase_name=usecase_name,
        description=description
    )
    if update_usecase:
        return redirect('projects:viewusecase', usecase_id=usecase_id)
    return redirect('projects:viewusecase', usecase_id=usecase_id)




#delete from viewpoint to usecase:
def delete_viewpoint(request,viewpoint_id):
    delete_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).delete()
    if delete_viewpoint:
        return redirect('projects:projects')

def delete_goal(request,goal_id):
    goal = Goal.objects.get(id=goal_id)
    delete_goal = Goal.objects.filter(id=goal_id).delete()
    if delete_goal:
        return redirect('projects:goals', viewpoint_id=goal.viewpoint.id)
    
def delete_requirement(request,requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    delete_requirement = Requirement.objects.filter(id=requirement_id).delete()
    if delete_requirement:
        return redirect('projects:requirements', goal_id=requirement.goal.id)

def delete_scenario(request,scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    delete_scenario = Scenario.objects.filter(id=scenario_id).delete()
    if delete_scenario:
        return redirect('projects:scenarios', requirement_id=scenario.requirement.id)

def delete_process(request,process_id):
    process = Process.objects.get(id=process_id)
    delete_process = Process.objects.filter(id=process_id).delete()
    if delete_process:
        return redirect('projects:processes',scenario_id=process.scenario.id)

def delete_usecase(request,usecase_id):
    usecase = UseCase.objects.get(id=usecase)
    delete_usecase = UseCase.objects.filter(id=usecase_id).delete()
    if delete_usecase:
        return redirect('projects:usecases', process_id=usecase.process.id)