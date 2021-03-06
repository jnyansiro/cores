from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from random import randint
import time
import datetime
import json
from datetime import datetime
from django.utils.timezone import now
from django.http import Http404
import urllib.request


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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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
        viewpoint=viewpoint, star_rate__number_of_stars=5
    ).count()
    fourstar_rate = ViewPointRate.objects.filter(
        viewpoint=viewpoint, star_rate__number_of_stars=4
    ).count()
    threestar_rate = ViewPointRate.objects.filter(
        viewpoint=viewpoint, star_rate__number_of_stars=3
    ).count()
    twostar_rate = ViewPointRate.objects.filter(
        viewpoint=viewpoint, star_rate__number_of_stars=2
    ).count()
    onestar_rate = ViewPointRate.objects.filter(
        viewpoint=viewpoint, star_rate__number_of_stars=1
    ).count()

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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
    fourstar_rate = UseCaseRate.objects.filter(
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

    if (
        fivestar_rate == 0
        and fourstar_rate == 0
        and threestar_rate == 0
        and twostar_rate == 0
        and onestar_rate == 0
    ):
        mean_fivestar_rate = 0.0
        mean_fourstar_rate = 0.0
        mean_threestar_rate = 0.0
        mean_twostar_rate = 0.0
        mean_onestar_rate = 0.0

    else:
        mean_fivestar_rate = (
            fivestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_fourstar_rate = (
            fourstar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_threestar_rate = (
            threestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_twostar_rate = (
            twostar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100
        mean_onestar_rate = (
            onestar_rate
            / (
                fivestar_rate
                + fourstar_rate
                + threestar_rate
                + twostar_rate
                + onestar_rate
            )
        ) * 100

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
    # getting total visitors
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    if not Visitor.objects.filter(ip_address=ip).exists():
        create_visitor = Visitor.objects.create(ip_address=ip)
        create_visitor.save()
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
    hidesearch = "hide"
    visitors = Visitor.objects.all().count()

    return render(
        request,
        "index.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "current_projects": current_projects,
            "total_projects": total_projects,
            "profile_update": profile_update,
            "member": member,
            "members": members,
            "visitors": visitors,
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

        if not Member.objects.filter(user=request.user).exists():
            member = Member.objects.create(
                user=request.user,
                first_name=request.user.username,
                middle_name=" ",
                surname=" ",
                email=request.user.email,
            )
            member.save()
            login_log = LoginLog.objects.create(user=request.user)
            login_log.save()
            if "next_page" in request.session:
                path = request.session["next_page"]
                return redirect(path)
            return redirect("projects:profile")
        login_log = LoginLog.objects.create(user=request.user)
        login_log.save()
        if "next_page" in request.session:
            path = request.session["next_page"]
            return redirect(path)
        return redirect("index")

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                login_log = LoginLog.objects.create(user=request.user)
                login_log.save()
                if request.GET.get("path"):
                    return redirect(request.GET.get("path"))
                return redirect("index")
            message = "sorry your account is inactive communicate with your Admin"
            return render(request, "login.html", {"message": message})
        message = "Soory you have entered incorrect credentials"
        return render(request, "login.html", {"message": message})
    if request.GET.get("next") != None:
        request.session["next_page"] = request.GET.get("next")
        return render(request, "login.html", {"path": request.GET.get("next")})

    return render(request, "login.html")


# user logout
def logout(request):

    # builtin function for session destroy

    log = LoginLog.objects.filter(user=request.user).order_by("-id")[0]
    logout_log = LoginLog.objects.filter(user=request.user, id=log.id).update(
        logout_time=datetime.now()
    )
    auth_logout(request)
    if "next_page" in request.session:
        del request.session["next_page"]
    return redirect("login")


def recovery(request):

    if request.method == "POST":
        generated_key = request.POST.get("key")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        user_reset = ResetPassword.objects.filter(generated_key=generated_key).order_by(
            "-id"
        )[0]
        if password == password1:

            if user_reset.status == "active":
                user_account = User.objects.get(id=user_reset.user.id)
                user_account.set_password(password)
                user_account.save()
                update_session_auth_hash(request, user_account)

                if user_account:
                    ResetPassword.objects.filter(generated_key=generated_key).update(
                        status="expired"
                    )
                    message = "Your password has been successfull Reseted, now you can login with new password"
                    return render(request, "login.html", {"reg_message": message},)

                message1 = "Sorry failed to reset password try again"
                return render(request, "password_reset.html", {"message1": message1},)
            message1 = "Your entered key has been expired go and generate again"
            return render(request, "password_reset.html", {"message1": message1})
        message1 = "Password did not match, please enter correctly"
        return render(request, "password_reset.html", {"message1": message1})
    return render(request, "password_reset.html", {})


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
            if User.objects.filter(email=email).exists():
                message = (
                    "sorry there is existing Member with that Email ("
                    + email
                    + "), One email can be used only by one Member"
                )
                return render(request, "registration.html", {"message": message})
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

                        if "next_page" in request.session:
                            next_page = request.session["next_page"]
                            return redirect(next_page)
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
        email = request.POST.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            random_number = randint(10000, 99999)
            create_entry = ResetPassword.objects.create(
                user=user, generated_key=random_number, status="active"
            )
            create_entry.save()
            print(random_number)
            message = (
                "Dear "
                + user.username
                + " You can reset your account password by Using this key: "
                + str(random_number)
                + ""
            )

            # then sending email
            send_email = send_mail(
                "CORES PASSWORD REST KEY",
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            print(send_email)
            if send_email:
                result = "password Reset key has been sent to " + email
                return render(request, "password_reset.html", {"message": result})
            result = "sorry failed to send a Key try again"
            return render(request, "password_recover.html", {"message1": result})
        result = "sorry there is no account with this email address"
        return render(request, "password_recover.html", {"message1": result})
    return render(request, "password_recover.html", {})


def pagenotfound(request, exception=None):

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
        country = request.POST.get("country")

        # getting member who create of project
        member = Member.objects.get(user=request.user.id)
        if datetime.strptime(due_date, "%Y-%m-%d") > datetime.now():

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
                    country=country,
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
                    country=country,
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

            # create default viewpoints
            default_viewpoints = DefaultViewpoint.objects.all()
            num = 0
            for default_viewpoint in default_viewpoints:
                num = num + 1
                number = "V" + str(num)
                viewpoint = Viewpoint.objects.create(
                    project=project,
                    viewpoint_name=default_viewpoint.viewpoint_name,
                    viewpoint_photo=default_viewpoint.viewpoint_photo,
                    description=default_viewpoint.description,
                    created_by=member,
                    number=number,
                    status="accepted",
                )
                viewpoint.save()

            if project:
                project_membership = ProjectMembership.objects.create(
                    project=project, member=member, member_role="Admin", status="active"
                )
                project_membership.save()
                return redirect("projects:myprojects")

        indexhead = "Project / Create-Project"
        message = "Due date should be later days"
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
                "message": message,
                "incentives": incentives,
                "member": member,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

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
    if request.method != "POST":
        member_details = enumerate(
            Member.objects.exclude(id__in=ids).order_by("-id"), start=1
        )
    else:
        name = request.POST.get("project_keyword")
        member_details = enumerate(
            Member.objects.filter(
                Q(first_name__icontains=name)
                | Q(middle_name__icontains=name)
                | Q(surname__icontains=name)
            )
            .exclude(id__in=ids)
            .order_by("-id"),
            start=1,
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
def viewMemberDetails(request, member_id=None):
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

        if date_of_birth == None:
            message = "Date of Birth should not be Null or None"
            member_details = Member.objects.get(user=request.user)
            indexhead = "Profile"
            hidesearch = "hide"

            return render(
                request,
                "user/profile.html",
                {
                    "member_details": member_details,
                    "indexhead": indexhead,
                    "member": member,
                    "message": message,
                    "hidesearch": hidesearch,
                    "notification": notification(request),
                    "total_notification": total_notification(request),
                },
            )
        if datetime.strptime(str(date_of_birth), "%Y-%m-%d") > datetime.now():
            message = "Birth date should be less than this year"
            member_details = Member.objects.get(user=request.user)
            indexhead = "Profile"
            hidesearch = "hide"

            return render(
                request,
                "user/profile.html",
                {
                    "member_details": member_details,
                    "indexhead": indexhead,
                    "member": member,
                    "message": message,
                    "hidesearch": hidesearch,
                    "notification": notification(request),
                    "total_notification": total_notification(request),
                },
            )

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
    if request.method == "POST":
        project_title = request.POST.get("project_title")
        if not request.POST.get("project_photo"):
            project_photo = project.project_photo
        else:
            project_photo = request.POST.get("project_photo")
        description = request.POST.get("project_descriptions")

        if not request.POST.get("due_date"):
            due_date = project.due_date
        else:
            due_date = request.POST.get("due_date")
        if not request.POST.get("visibility"):
            visibility = project.project_visibility
        else:
            visibility = request.POST.get("visibility")
        update_project = Project.objects.filter(id=project_id)
        update_project.update(
            project_title=project_title,
            project_photo=project_photo,
            description=description,
            project_visibility=visibility,
            due_date=due_date,
        )
        if "Invitational" in request.POST.getlist("participation"):
            update_project.update(is_invitational=True)

        if "Discoverable" in request.POST.getlist("participation"):
            update_project.update(is_discoverable=True)

        if request.POST.get("visibility") == "private":
            update_project.update(is_public=False)

        if request.POST.get("visibility") == "public":
            update_project.update(is_public=True)
            update_project.update(is_invitational=False)
            update_project.update(is_discoverable=False)

        return redirect("projects:viewmyproject", project_id=project_id)
    print("sectors")
    return render(
        request,
        "projects/my_projects/edit_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "sectors": sectors,
            "project": project,
            "project_id": project.id,
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
    if (
        ProjectMembership.objects.filter(
            project=project, member=member, status="active"
        ).exists()
        or project.project_visibility == "public"
    ):

        if request.method == "POST":
            comment = request.POST.get("comment")

            #    then creating comment then ProjectComment
            if project.created_by == member:
                comment_data = Comment.objects.create(
                    comment=comment, commented_by=member, status="accepted"
                )
            else:
                comment_data = Comment.objects.create(
                    comment=comment, commented_by=member
                )
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
                    return redirect("projects:viewmyproject", project_id=project_id)
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
        viewpoint = Viewpoint.objects.get(id=viewpoint_id)
        #    then creating comment then ProjectComment
        if viewpoint.project.created_by == member:
            comment_data = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            comment_data = Comment.objects.create(comment=comment, commented_by=member)
        comment_data.save()
        if comment_data:

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
    incentives = ProjectIncentive.objects.filter(project=project)
    return render(
        request,
        "projects/my_projects/project_incentive.html",
        {
            "project_incentives": project_incentives,
            "incentive_types": incentive_types,
            "project_members": project_members,
            "incentives": incentives,
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
    incentive = request.POST.get("incentives")
    description = request.POST.get("description")
    new_incentive = Incentive.objects.get(id=incentive)
    project_incentive = ProjectIncentive.objects.create(
        project=project, incentive=new_incentive, description=description
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
def remove_project_incentive(request, project_incentive_id):
    remove = ProjectIncentive.objects.filter(id=project_incentive_id).delete()
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def membershipProjects(request):
    indexhead = "Projects / Membership Project(s)"
    placeholder = "search membership project"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        keyword = request.POST.get("project_keyword")
        membershipprojects = ProjectMembership.objects.filter(
            Q(
                member=member,
                status="active",
                member_role="member",
                project__project_title__icontains=keyword,
            )
            | Q(
                member=member,
                status="active",
                member_role="member",
                project__description__icontains=keyword,
            )
        ).order_by("-id")
    else:
        membershipprojects = ProjectMembership.objects.filter(
            member=member, status="active", member_role="member"
        ).order_by("-id")
    paginator = Paginator(membershipprojects, 6)
    page_number = request.GET.get("page")
    membershipprojects = paginator.get_page(page_number)
    return render(
        request,
        "projects/other_projects/membership_projects.html",
        {
            "indexhead": indexhead,
            "membershipprojects": membershipprojects,
            "member": member,
            "placeholder": placeholder,
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
        keyword = request.POST.get("project_keyword")
        myProject = Project.objects.filter(
            Q(created_by=member, project_title__icontains=keyword)
            | Q(created_by=member, description__icontains=keyword)
        ).order_by("-id")
    else:
        myProject = Project.objects.filter(created_by=member).order_by("-id")
    return render(
        request,
        "projects/my_projects/myproject.html",
        {
            "indexhead": indexhead,
            "myProject": myProject,
            "member": member,
            "placeholder": placeholder,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewMyproject(request, project_id):
    indexhead = "Projects / My Project Details"
    project = Project.objects.get(id=project_id)
    stakeholders = Stakeholder.objects.filter(project=project).order_by("name")
    member = Member.objects.get(user=request.user)
    comments = ProjectComment.objects.filter(
        Q(project=project, comment__status="accepted")
        | Q(project=project, comment__commented_by=member)
    ).order_by("id")
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
    rate_data = project_rates(request, project_id=project_id)
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
            "url": short_url("https://www.cores.africa/invited"
            + "?invitation_id="
            + str(project.id)),
            "rates": rates,
            "incentives": ProjectIncentive.objects.filter(project=project),
            "stakeholders": stakeholders,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "rate_data": rate_data,
        },
    )


@login_required(login_url="login")
def viewProject(request, project_id, message=None, message1=None):
    indexhead = "Project Details"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    stakeholders = Stakeholder.objects.filter(project=project).order_by("name")
    project_membership = ProjectMembership.objects.filter(
        member=member, project=project, project__project_visibility="private"
    ).exists()

    project_member = None
    if project_membership:
        project_member = ProjectMembership.objects.get(
            member=member, project=project, project__project_visibility="private"
        )
    comments = ProjectComment.objects.filter(
        Q(project=project, comment__status="accepted")
        | Q(project=project, comment__commented_by=member)
    ).order_by("id")
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
            "message1": message1,
            "rates": rates,
            "url": short_url("https://www.cores.africa/invited"
            + "?invitation_id="
            + str(project.id)),
            "likes": likes,
            "incentives": ProjectIncentive.objects.filter(project=project),
            "stakeholders": stakeholders,
            "project_member": project_member,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "project_membership": project_membership,
            "rate_data": rate_data,
        },
    )


@login_required(login_url="login")
def projectMembers(request, project_id=None):
    indexhead = "Projects / Project-Members"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)

    if request.method == "POST":
        name = request.POST.get("project_keyword")
        project_member = (
            ProjectMembership.objects.filter(
                Q(project=project, member__first_name__icontains=name)
                | Q(project=project, member__middle_name__icontains=name)
                | Q(project=project, member__surname__icontains=name)
            )
            .exclude(status__in=["removed", "rejected", "invited"])
            .order_by("-id")
        )
    else:
        project_member = (
            ProjectMembership.objects.filter(project=project)
            .exclude(status__in=["removed", "rejected", "invited"])
            .order_by("-id")
        )
    project_member = enumerate(project_member, start=1)
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
    placeholder = "search by name"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        name = request.POST.get("project_keyword")
        member_details = ProjectMembership.objects.filter(
            Q(project=project, status="request", member__first_name__icontains=name)
            | Q(project=project, status="request", member__middle_name__icontains=name)
            | Q(project=project, status="request", member__surname__icontains=name)
        )
    else:
        member_details = ProjectMembership.objects.filter(
            project=project, status="request"
        )
    member_details = enumerate(member_details, start=1)

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
            "placeholder": placeholder,
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
        keyword = request.POST.get("project_keyword")
        projects = (
            Project.objects.filter(
                Q(project_title__icontains=keyword)
                | Q(description__icontains=keyword)
                | Q(project_visibility__icontains=keyword)
            )
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
    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(
        request,
        "projects/other_projects/projects.html",
        {
            "indexhead": indexhead,
            "projects": projects,
            "member": member,
            "message": message,
            "placeholder": placeholder,
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
    comments = ViewPointComment.objects.filter(
        Q(viewpoint=viewpoint, comment__status="accepted")
        | Q(viewpoint=viewpoint, comment__commented_by=member)
    ).order_by("id")
    total_comments = comments.count()
    likes = ViewpointLike.objects.filter(viewpoint=viewpoint).count()
    dislikes = ViewpointDislike.objects.filter(viewpoint=viewpoint).count()

    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    viewpointRate = ViewPointRate.objects.filter(
        viewpoint=viewpoint, star_rate__rated_by=member
    )
    rates = ViewPointRate.objects.filter(viewpoint=viewpoint).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    project_id = project.id
    rate_data = viewpoint_rates(request, viewpoint_id=viewpoint.id)
    if viewpoint.created_by == member or viewpoint.project.created_by == member:
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
            "rate_data": rate_data,
            "viewpointRate": viewpointRate,
            "rates": rates,
            "likes": likes,
            "creator": creator,
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

        projects = Project.objects.filter(
            Q(id__in=my_projects_id) | Q(project_visibility="public")
        ).order_by("-id")
        project_id = request.POST.get("project")
        project = Project.objects.get(id=project_id)
        viewpoint = Viewpoint.objects.filter(project=project).order_by("-id")
        viewpoints = Viewpoint.objects.filter(
            Q(project=project, status="accepted")
            | Q(project=project, created_by=member)
        ).order_by("id")
        paginate = Paginator(viewpoints, 6)
        page_number = request.GET.get("page")
        viewpoints = paginate.get_page(page_number)
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
                if membership.status == "active":
                    filltering_project = ProjectMembership.objects.filter(
                        member=member, status="active"
                    )
                    viewpoints = Viewpoint.objects.filter(
                        Q(project=project, status="accepted")
                        | Q(project=project, created_by=member)
                    ).order_by("id")
                    my_projects_id = []
                    for _project in filltering_project:
                        my_projects_id.append(_project.project.id)

                    projects = Project.objects.filter(
                        Q(id__in=my_projects_id) | Q(project_visibility="public")
                    ).order_by("-id")
                    paginator = Paginator(viewpoints, 6)
                    view_page_number = request.GET.get("page")
                    viewpoints = paginator.get_page(view_page_number)
                    return render(
                        request,
                        "projects/viewpoints/viewpoints.html",
                        {
                            "indexhead": indexhead,
                            "hidesearch": 1,
                            "viewpoints": viewpoints,
                            "project_id": project_id,
                            "member": member,
                            "project": project,
                            "projects": projects,
                            "notification": notification(request),
                            "total_notification": total_notification(request),
                        },
                    )

            message = "join"
            return viewProject(request, project_id=project_id, message1=message)
        filltering_project = ProjectMembership.objects.filter(
            member=member, status="active"
        )

        my_projects_id = []
        for _project in filltering_project:
            my_projects_id.append(_project.project.id)

        projects = Project.objects.filter(
            Q(id__in=my_projects_id) | Q(project_visibility="public")
        ).order_by("-id")
        print(projects)
        viewpoint = Viewpoint.objects.filter(project__id=project_id).order_by("-id")
        viewpoints = Viewpoint.objects.filter(
            Q(project=project, status="accepted")
            | Q(project=project, created_by=member)
        ).order_by("id")
        paginator = Paginator(viewpoints, 6)
        view_page_number = request.GET.get("page")
        viewpoints = paginator.get_page(view_page_number)
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

        # creating viewpoint number
        viewpoint_list = Viewpoint.objects.filter(project=project)
        if viewpoint_list:
            viewpoint_list = viewpoint_list.order_by("-id")[0]
            if viewpoint_list.number != None:
                interger = viewpoint_list.number[1:]
                number = "V" + str(int(interger) + 1)
            else:
                num = 0
                for viewpoint_list1 in Viewpoint.objects.filter(
                    project=project
                ).order_by("id"):
                    num = num + 1
                    number = "V" + str(num)
                    Viewpoint.objects.filter(id=viewpoint_list1.id).update(
                        number=number
                    )

                viewpoint_list2 = Viewpoint.objects.filter(project=project).order_by(
                    "-id"
                )[0]
                interger = viewpoint_list2.number[1:]
                number = "V" + str(int(interger) + 1)

        else:
            number = "V1"
        if viewpoint_photo:
            if project.created_by == member:

                viewpoint = Viewpoint.objects.create(
                    project=project,
                    created_by=member,
                    viewpoint_name=viewpoint_title,
                    viewpoint_links=links,
                    viewpoint_photo=viewpoint_photo,
                    viewpoint_docs=viewpoint_docs,
                    description=viewpoint_descriptions,
                    status="accepted",
                    number=number,
                )
            else:
                viewpoint = Viewpoint.objects.create(
                    project=project,
                    created_by=member,
                    viewpoint_name=viewpoint_title,
                    viewpoint_links=links,
                    viewpoint_photo=viewpoint_photo,
                    viewpoint_docs=viewpoint_docs,
                    description=viewpoint_descriptions,
                    number=number,
                )
        else:
            if project.created_by == member:
                viewpoint = Viewpoint.objects.create(
                    project=project,
                    created_by=member,
                    viewpoint_name=viewpoint_title,
                    viewpoint_links=links,
                    viewpoint_docs=viewpoint_docs,
                    description=viewpoint_descriptions,
                    number=number,
                    status="accepted",
                )
            else:
                viewpoint = Viewpoint.objects.create(
                    project=project,
                    created_by=member,
                    viewpoint_name=viewpoint_title,
                    viewpoint_links=links,
                    viewpoint_docs=viewpoint_docs,
                    number=number,
                    description=viewpoint_descriptions,
                )
        viewpoint.save()
        if viewpoint:
            return redirect("projects:viewpoints", project_id=project_id)

    indexhead = "Project -ViewPoints"
    hidesearch = "hide"
    num = 0
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/viewpoints/create_viewpoint.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project_id": project_id,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def goals(request, project_id=None, viewpoint_id=None):
    indexhead = "Viewpoint-Goals"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        view = request.POST.get("viewpoint_id")
        viewpoint = Viewpoint.objects.get(id=view)
        goals = (
            ViewpointGoal.objects.filter(
                Q(viewpoint=viewpoint, goal__status="accepted")
                | Q(viewpoint=viewpoint, goal__created_by=member)
            )
            .order_by("goal__id")
            .distinct("goal__id")
        )
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints = Viewpoint.objects.filter(
            Q(project=project, status="accepted")
            | Q(project=project, created_by=member)
        ).order_by("id")

        viewpoint_id = viewpoint_id
        paginate = Paginator(goals, 10)
        page_number = request.GET.get("page")
        goals = paginate.get_page(page_number)
        return render(
            request,
            "projects/Goals/goals.html",
            {
                "indexhead": indexhead,
                "goals": goals,
                "viewpoints": viewpoints,
                "viewpoint_id": viewpoint_id,
                "viewpoint": viewpoint,
                "member": member,
                "project": project,
                "hidesearch": 1,
                "project_id": project.id,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    goals = (
        ViewpointGoal.objects.filter(
            Q(viewpoint=viewpoint, goal__status="accepted")
            | Q(viewpoint=viewpoint, goal__created_by=member)
        )
        .order_by("goal__id")
        .distinct("goal__id")
    )
    project = Project.objects.get(id=viewpoint.project.id)
    viewpointiees = Viewpoint.objects.filter(project=project).order_by("-id")
    viewpoints = Viewpoint.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("id")
    viewpoint_id = viewpoint_id
    paginate = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginate.get_page(page_number)
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
            "viewpoint": viewpoint,
            "project_id": project.id,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewGoal(request, goal_id, message=None):
    indexhead = "Goal Description"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)

    if request.method == "POST":
        goal = request.POST.get("goal")
        goal = ViewpointGoal.objects.get(id=goal)

        goals_to_exclude_now = GoalRelationship.objects.filter(origin_goal=goal.goal)
        goal_ids_to_exclude = []
        for goal_to_exclude in goals_to_exclude_now:
            goal_ids_to_exclude.append(goal_to_exclude.related_goal)
        goal_ids_to_exclude.append(goal.goal.id)
        related_goals = Goal.objects.filter(project=goal.goal.project).exclude(
            id__in=goal_ids_to_exclude
        )
        goals_decomposed = GoalDecomposition.objects.filter(original_goal=goal.goal)
        decomposed_goals_id = []
        for goal_decomposed_id in goals_decomposed:
            decomposed_goals_id.append(goal_decomposed_id.decomposed_goal)
        decomposed_goals_id.append(goal.goal.id)
        decomposed_goals = Goal.objects.filter(project=goal.goal.project).exclude(
            id__in=decomposed_goals_id
        )
        all_goals = Goal.objects.filter(
            project=goal.goal.project, status="accepted"
        ).exclude(id=goal.goal.id)
        viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
        goals = (
            ViewpointGoal.objects.filter(
                Q(viewpoint=viewpoint, goal__status="accepted")
                | Q(viewpoint=viewpoint, goal__created_by=member)
            )
            .order_by("-goal__id")
            .distinct("goal__id")
        )
        viewpoint_id = viewpoint.id
        project = Project.objects.get(id=viewpoint.project.id)
        viewpoints_to_exclude = ViewpointGoal.objects.filter(goal=goal.goal)
        viewpoint_ids_to_exclude = []
        for viewpoint_to_exclude in viewpoints_to_exclude:
            viewpoint_ids_to_exclude.append(viewpoint_to_exclude.viewpoint.id)
        viewpoints = Viewpoint.objects.filter(
            Q(project=project, status="accepted")
        ).exclude(id__in=viewpoint_ids_to_exclude)
        project_id = project.id
        comments = GoalComment.objects.filter(
            Q(goal=goal.goal, comment__status="accepted")
            | Q(goal=goal.goal, comment__commented_by=member)
        ).order_by("id")
        rate_data = goal_rates(request, goal_id=goal.goal.id)
        if (
            goal.goal.created_by == member
            or goal.viewpoint.project.created_by == member
        ):
            creator = "me"
        else:
            creator = "not me"
        comments = GoalComment.objects.filter(
            Q(goal=goal.goal, comment__status="accepted")
            | Q(goal=goal.goal, comment__commented_by=member)
        ).order_by("id")
        goalRate = GoalRate.objects.filter(goal=goal.goal, star_rate__rated_by=member)
        rates = GoalRate.objects.filter(goal=goal.goal).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        likes = GoalLike.objects.filter(goal=goal.goal).count()
        dislikes = GoalDislike.objects.filter(goal=goal.goal).count()
        requirement_ids = []
        requirements_to_exclude = RequirementGoal.objects.filter(goal=goal.goal)
        for requirement in requirements_to_exclude:
            requirement_ids.append(requirement.requirement.id)

        requirements = Requirement.objects.filter(project=project).exclude(
            id__in=requirement_ids
        )

        requirementss = (
            RequirementGoal.objects.filter(goal=goal.goal)
            .order_by("requirement__id")
            .distinct("requirement__id")
        )
        viewpointss = (
            ViewpointGoal.objects.filter(goal=goal.goal)
            .order_by("viewpoint__id")
            .distinct("viewpoint__id")
        )

        ids = []
        for goal_id in GoalRelationship.objects.filter(origin_goal=goal.goal):
            ids.append(goal_id.related_goal)
        goalss = Goal.objects.filter(id__in=ids)

        goal_ids = []
        for goal_ in GoalDecomposition.objects.filter(original_goal=goal.goal):
            goal_ids.append(goal_.decomposed_goal)

        goalsss = Goal.objects.filter(id__in=goal_ids)

        return render(
            request,
            "projects/Goals/view_goal.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "viewpoint_id": viewpoint_id,
                "requirements": requirements,
                "viewpointss": viewpointss,
                "requirementss": requirementss,
                "goalss": goalss,
                "goalsss": goalsss,
                "project_id": project_id,
                "goal_id": goal_id,
                "all_goals": all_goals,
                "and_goals": and_goals(request, goal.goal),
                "or_goals": or_goals(request, goal.goal),
                "linear_goals": linear_goals(request, goal.goal),
                "conflict_goals": conflict_goals(request, goal.goal),
                "require_goals": require_goals(request, goal.goal),
                "contribute_goals": contribute_goals(request, goal.goal),
                "viewpoints": viewpoints,
                "related_goals": related_goals,
                "decomposed_goals": decomposed_goals,
                "comments": comments,
                "rate_data": rate_data,
                "goalRate": goalRate,
                "total_rates": total_rates,
                "total_comments": total_comments,
                "message": message,
                "rates": rates,
                "hidesearch": hidesearch,
                "creator": creator,
                "likes": likes,
                "dislikes": dislikes,
                "goals": goals,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    goal = ViewpointGoal.objects.get(id=goal_id)
    goals_to_exclude_now = GoalRelationship.objects.filter(origin_goal=goal.goal)
    goal_ids_to_exclude = []
    for goal_to_exclude in goals_to_exclude_now:
        goal_ids_to_exclude.append(goal_to_exclude.related_goal)
    goal_ids_to_exclude.append(goal.goal.id)
    related_goals = Goal.objects.filter(project=goal.goal.project).exclude(
        id__in=goal_ids_to_exclude
    )
    goals_decomposed = GoalDecomposition.objects.filter(original_goal=goal.goal)
    decomposed_goals_id = []
    for goal_decomposed_id in goals_decomposed:
        decomposed_goals_id.append(goal_decomposed_id.decomposed_goal)
    decomposed_goals_id.append(goal.goal.id)
    decomposed_goals = Goal.objects.filter(project=goal.goal.project).exclude(
        id__in=decomposed_goals_id
    )
    all_goals = Goal.objects.filter(
        project=goal.goal.project, status="accepted"
    ).exclude(id=goal.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    goals = (
        ViewpointGoal.objects.filter(
            Q(viewpoint=viewpoint, goal__status="accepted")
            | Q(viewpoint=viewpoint, goal__created_by=member)
        )
        .order_by("-goal__id")
        .distinct("goal__id")
    )
    viewpoint_id = viewpoint.id
    project = Project.objects.get(id=goal.goal.project.id)
    viewpoints_to_exclude = ViewpointGoal.objects.filter(goal=goal.goal)
    viewpoint_ids_to_exclude = []
    for viewpoint_to_exclude in viewpoints_to_exclude:
        viewpoint_ids_to_exclude.append(viewpoint_to_exclude.viewpoint.id)
    viewpoints = Viewpoint.objects.filter(
        Q(project=project, status="accepted")
    ).exclude(id__in=viewpoint_ids_to_exclude)
    project_id = project.id
    rate_data = goal_rates(request, goal_id=goal.goal.id)
    if goal.goal.created_by == member:
        creator = "me"
    else:
        creator = "not me"

    comments = GoalComment.objects.filter(
        Q(goal=goal.goal, comment__status="accepted")
        | Q(goal=goal.goal, comment__commented_by=member)
    ).order_by("id")
    goalRate = GoalRate.objects.filter(goal=goal.goal, star_rate__rated_by=member)
    rates = GoalRate.objects.filter(goal=goal.goal).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = GoalLike.objects.filter(goal=goal.goal).count()
    dislikes = GoalDislike.objects.filter(goal=goal.goal).count()
    requirement_ids = []
    requirements_to_exclude = RequirementGoal.objects.filter(goal=goal.goal)
    for requirement in requirements_to_exclude:
        requirement_ids.append(requirement.requirement.id)

    requirements = Requirement.objects.filter(project=project).exclude(
        id__in=requirement_ids
    )

    requirementss = (
        RequirementGoal.objects.filter(goal=goal.goal)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    viewpointss = (
        ViewpointGoal.objects.filter(goal=goal.goal)
        .order_by("viewpoint__id")
        .distinct("viewpoint__id")
    )

    ids = []
    for goal_id in GoalRelationship.objects.filter(origin_goal=goal.goal):
        ids.append(goal_id.related_goal)
    goalss = Goal.objects.filter(id__in=ids)

    goal_ids = []
    for goal_ in GoalDecomposition.objects.filter(original_goal=goal.goal):
        goal_ids.append(goal_.decomposed_goal)

    goalsss = Goal.objects.filter(id__in=goal_ids)
    return render(
        request,
        "projects/Goals/view_goal.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            "viewpoint_id": viewpoint_id,
            "viewpointss": viewpointss,
            "requirementss": requirementss,
            "goalss": goalss,
            "goalsss": goalsss,
            "project_id": project_id,
            "goal_id": goal_id,
            "viewpoints": viewpoints,
            "requirements": requirements,
            "comments": comments,
            "goalRate": goalRate,
            "all_goals": all_goals,
            "and_goals": and_goals(request, goal.goal),
            "or_goals": or_goals(request, goal.goal),
            "linear_goals": linear_goals(request, goal.goal),
            "conflict_goals": conflict_goals(request, goal.goal),
            "require_goals": require_goals(request, goal.goal),
            "contribute_goals": contribute_goals(request, goal.goal),
            "related_goals": related_goals,
            "decomposed_goals": decomposed_goals,
            "likes": likes,
            "rate_data": rate_data,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "total_comments": total_comments,
            "rates": rates,
            "goals": goals,
            "hidesearch": hidesearch,
            "creator": creator,
            "message": message,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createGoal(request, project_id):
    indexhead = "Create Goal"
    member = Member.objects.get(user=request.user)
    categories = Category.objects.all().order_by("category_name")
    project = Project.objects.get(id=project_id)
    requirements = Requirement.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("name")
    viewpoints = (
        Viewpoint.objects.filter(
            Q(project=project, status="accepted")
            | Q(project=project, created_by=member)
        )
        .order_by("-id")
        .distinct("id")
    )
    if request.method == "POST":
        goal_name = request.POST.get("goal_title")
        description = request.POST.get("description")
        requirement = request.POST.get("requirement")
        created_by = Member.objects.get(user=request.user)
        goal_type = request.POST.get("goal_type")

        # creating goal number

        goal_list = Goal.objects.filter(project=project)
        if goal_list:
            goal_list = goal_list.order_by("-id")[0]
            if goal_list.number != None:
                interger = goal_list.number[1:]
                number = "G" + str(int(interger) + 1)
            else:
                num = 0
                for goal_list1 in Goal.objects.filter(project=project).order_by("id"):
                    num = num + 1
                    number = "G" + str(num)
                    Goal.objects.filter(id=goal_list1.id).update(number=number)

                goal_list2 = Goal.objects.filter(project=project).order_by("-id")[0]
                interger = goal_list2.number[1:]
                number = "G" + str(int(interger) + 1)

        else:
            number = "G1"

        # then creating goal
        if project.created_by == member:
            goal = Goal.objects.create(
                goal_name=goal_name,
                description=description,
                created_by=created_by,
                project=project,
                number=number,
                goal_type=goal_type,
                status="accepted",
            )
        else:
            goal = Goal.objects.create(
                goal_name=goal_name,
                description=description,
                created_by=created_by,
                number=number,
                goal_type=goal_type,
                project=project,
            )
        goal.save()
        if goal:
            for viewpoint_id in request.POST.getlist("viewpoint"):
                viewpoint = Viewpoint.objects.get(id=viewpoint_id)
                create_viewpoint_goal = ViewpointGoal.objects.create(
                    viewpoint=viewpoint, goal=goal
                )
                create_viewpoint_goal.save()
            return redirect("projects:projectgoals", project_id)

    return render(
        request,
        "projects/Goals/create_goal.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
            "requirements": requirements,
            "categories": categories,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": 1,
        },
    )


@login_required(login_url="login")
def requirements(request, goal_id):
    indexhead = "Goal-Requirements"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        goal_id = request.POST.get("goal")
        goal = RequirementGoal.objects.get(id=goal_id)
        requirements = (
            RequirementGoal.objects.filter(
                Q(goal=goal.goal, requirement__status="accepted")
                | Q(goal=goal.goal, requirement__created_by=member)
            )
            .order_by("requirement__id")
            .distinct("requirement__id")
        )
        project = Project.objects.get(id=goal.goal.project.id)
        project_id = project.id
        paginate = Paginator(requirements, 10)
        page_number = request.GET.get("page")
        requirements = paginate.get_page(page_number)
        return render(
            request,
            "projects/requirements/requirements.html",
            {
                "indexhead": indexhead,
                "goal_id": goal.id,
                "project_id": project_id,
                "requirements": requirements,
                "goal": goal,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    goal = Goal.objects.get(id=goal_id)
    requirements = (
        RequirementGoal.objects.filter(
            Q(goal=goal, requirement__status="accepted")
            | Q(goal=goal, requirement__created_by=member)
        )
        .order_by("requirement__id")
        .distinct("requirement__id")
    )

    project = Project.objects.get(id=goal.project.id)
    project_id = project.id
    paginate = Paginator(requirements, 10)
    page_number = request.GET.get("page")
    requirements = paginate.get_page(page_number)
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            "goal": goal,
            "member": member,
            "project": project,
            "hidesearch": hidesearch,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def requirementgoals(request, requirement_id=None):
    indexhead = "Associated Requirement Goals"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    goals = (
        RequirementGoal.objects.filter(requirement=requirement)
        .order_by("-requirement__id")
        .distinct("requirement__id")
    )
    project = Project.objects.get(id=requirement.project.id)
    goal_list = []
    for goal in goals:
        goal_list.append(goal.goal)

    goals = (
        ViewpointGoal.objects.filter(goal__in=goal_list)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    project_id = project.id
    paginate = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginate.get_page(page_number)
    return render(
        request,
        "projects/Goals/goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "member": member,
            "project_id": project_id,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewrequirement(request, requirement_id=None, message=None):
    indexhead = "Requirement Description"
    requirement = RequirementGoal.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)

    if request.POST.get("requirement"):
        requirement = request.POST.get("requirement")
        requirement = RequirementGoal.objects.get(id=requirement)
        requirements = (
            RequirementGoal.objects.filter(
                Q(goal=requirement.goal, requirement__status="accepted")
                | Q(goal=requirement.goal, requirement__created_by=member)
            )
            .order_by("-requirement__id")
            .distinct("requirement__id")
        )
        project = Project.objects.get(id=requirement.requirement.project.id)

        project_id = project.id
        comments = RequirementComment.objects.filter(
            Q(requirement=requirement.requirement, comment__status="accepted")
            | Q(requirement=requirement.requirement, comment__commented_by=member)
        ).order_by("id")
        requirementRate = RequirementRate.objects.filter(
            requirement=requirement.requirement, star_rate__rated_by=member
        )
        rates = RequirementRate.objects.filter(
            requirement=requirement.requirement
        ).order_by("-star_rate__number_of_stars")
        total_rates = rates.count()
        total_comments = comments.count()
        likes = RequirementLike.objects.filter(
            requirement=requirement.requirement
        ).count()
        dislikes = RequirementDislike.objects.filter(
            requirement=requirement.requirement
        ).count()
        RequirementComment.objects.filter(
            Q(requirement=requirement.requirement, comment__status="accepted")
            | Q(requirement=requirement.requirement, comment__commented_by=member)
        ).order_by("-id")
        requirementRate = RequirementRate.objects.filter(
            requirement=requirement.requirement, star_rate__rated_by=member
        )
        rates = RequirementRate.objects.filter(
            requirement=requirement.requirement
        ).order_by("-star_rate__number_of_stars")
        total_rates = rates.count()
        total_comments = comments.count()
        likes = RequirementLike.objects.filter(
            requirement=requirement.requirement
        ).count()
        dislikes = RequirementDislike.objects.filter(
            requirement=requirement.requirement
        ).count()
        rate_data = requirement_rates(
            request, requirement_id=requirement.requirement.id
        )
        if (
            requirement.requirement.created_by == member
            or requirement.requirement.project.created_by == member
        ):
            creator = "me"
        else:
            creator = "not me"
        goal = requirement.goal
        stakeholders = RequirementStakeholder.objects.filter(
            requirement=requirement.requirement
        )
        goal_list = []
        for goal_ in RequirementGoal.objects.filter(
            requirement=requirement.requirement
        ):
            goal_list.append(goal_.goal.id)
        goals = Goal.objects.filter(project=project).exclude(id__in=goal_list)

        scenario_list = []
        scenario_to_exclude = RequirementScenario.objects.filter(
            requirement=requirement.requirement
        )
        for scenario in scenario_to_exclude:
            scenario_list.append(scenario.scenario.id)
        scenarios = Scenario.objects.filter(project=project).exclude(
            id__in=scenario_list
        )

        process_list = []
        for process in RequirementProcess.objects.filter(
            requirement=requirement.requirement
        ):
            process_list.append(process.process.id)
        processes = Process.objects.filter(project=project).exclude(id__in=process_list)

        usecase_list = []
        for usecase in RequirementUsecase.objects.filter(
            requirement=requirement.requirement
        ):
            usecase_list.append(usecase.usecase.id)
        usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)

        goalss = RequirementGoal.objects.filter(requirement=requirement.requirement)
        scenarioss = RequirementScenario.objects.filter(
            requirement=requirement.requirement
        )
        processess = RequirementProcess.objects.filter(
            requirement=requirement.requirement
        )
        usecasess = RequirementUsecase.objects.filter(
            requirement=requirement.requirement
        )

        return render(
            request,
            "projects/requirements/view_requirement.html",
            {
                "indexhead": indexhead,
                "goal": goal,
                "goals": goals,
                "project_id": project_id,
                "goal_id": goal.id,
                "scenarios": scenarios,
                "processes": processes,
                "usecases": usecases,
                "usecasess": usecasess,
                "processess": processess,
                "goalss": goalss,
                "scenarioss": scenarioss,
                "creator": creator,
                "rates": rates,
                "likes": likes,
                "dislikes": dislikes,
                "stakeholders": stakeholders,
                "rate_data": rate_data,
                "total_rates": total_rates,
                "requirementRate": requirementRate,
                "comments": comments,
                "total_comments": total_comments,
                "requirements": requirements,
                "requirement": requirement,
                "member": member,
                "project": project,
                "hidesearch": 1,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    goal = requirement.goal
    requirements = (
        RequirementGoal.objects.filter(requirement__project=goal.project)
        .order_by("-requirement__id")
        .distinct("requirement__id")
    )
    project = Project.objects.get(id=goal.project.id)
    viewpoints = Viewpoint.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    )
    project_id = project.id
    rate_data = requirement_rates(request, requirement_id=requirement.requirement.id)
    if requirement.requirement.created_by == member:
        creator = "me"
    else:
        creator = "not me"
    stakeholders = RequirementStakeholder.objects.filter(
        requirement=requirement.requirement
    )
    comments = RequirementComment.objects.filter(
        Q(requirement=requirement.requirement, comment__status="accepted")
        | Q(requirement=requirement.requirement, comment__commented_by=member)
    ).order_by("id")
    requirementRate = RequirementRate.objects.filter(
        requirement=requirement.requirement, star_rate__rated_by=member
    )
    rates = RequirementRate.objects.filter(
        requirement=requirement.requirement
    ).order_by("-star_rate__number_of_stars")
    total_rates = rates.count()
    total_comments = comments.count()
    likes = RequirementLike.objects.filter(requirement=requirement.requirement).count()
    dislikes = RequirementDislike.objects.filter(
        requirement=requirement.requirement
    ).count()
    goal_list = []
    for goal_ in RequirementGoal.objects.filter(requirement=requirement.requirement):
        goal_list.append(goal_.goal.id)
    goals = Goal.objects.filter(project=project).exclude(id__in=goal_list)

    scenario_list = []
    scenario_to_exclude = RequirementScenario.objects.filter(
        requirement=requirement.requirement
    )
    for scenario in scenario_to_exclude:
        scenario_list.append(scenario.scenario.id)
    scenarios = Scenario.objects.filter(project=project).exclude(id__in=scenario_list)

    process_list = []
    for process in RequirementProcess.objects.filter(
        requirement=requirement.requirement
    ):
        process_list.append(process.process.id)
    processes = Process.objects.filter(project=project).exclude(id__in=process_list)

    usecase_list = []
    for usecase in RequirementUsecase.objects.filter(
        requirement=requirement.requirement
    ):
        usecase_list.append(usecase.usecase.id)
    usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)
    goalss = RequirementGoal.objects.filter(requirement=requirement.requirement)
    scenarioss = RequirementScenario.objects.filter(requirement=requirement.requirement)
    processess = RequirementProcess.objects.filter(requirement=requirement.requirement)
    usecasess = RequirementUsecase.objects.filter(requirement=requirement.requirement)

    return render(
        request,
        "projects/requirements/view_requirement.html",
        {
            "indexhead": indexhead,
            "goal": goal,
            "project_id": project_id,
            "goal_id": goal.id,
            "viewpoints": viewpoints,
            "usecasess": usecasess,
            "processess": processess,
            "goalss": goalss,
            "scenarioss": scenarioss,
            "scenarios": scenarios,
            "processes": processes,
            "usecases": usecases,
            "rates": rates,
            "likes": likes,
            "goals": goals,
            "creator": creator,
            "rate_data": rate_data,
            "stakeholders": stakeholders,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "comments": comments,
            "total_comments": total_comments,
            "requirementRate": requirementRate,
            "requirements": requirements,
            "requirement": requirement,
            "message": message,
            "member": member,
            "hidesearch": 1,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createRequirement(request, project_id):
    hidesearch = "hide"
    indexhead = "Create Requirement"
    member = Member.objects.get(user=request.user)

    project = Project.objects.get(id=project_id)
    project_id = project.id
    goals = Goal.objects.filter(project=project, status="accepted").order_by(
        "goal_name"
    )
    stakeholders = Stakeholder.objects.filter(project=project)

    if request.method == "POST":
        requirement_title = request.POST.get("requirement_title")
        description = request.POST.get("requirement_descriptions")
        created_by = Member.objects.get(user=request.user)
        scenarios = request.POST.getlist("scenario")
        processes = request.POST.getlist("process")
        usecase = request.POST.getlist("usecase")

        # creating requirement number
        requirement_list = Requirement.objects.filter(project=project)
        if requirement_list:
            requirement_list = requirement_list.order_by("-id")[0]
            if requirement_list.number != None:
                interger = requirement_list.number[1:]
                number = "R" + str(int(interger) + 1)
            else:
                num = 0
                for requirement_list1 in Requirement.objects.filter(
                    project=project
                ).order_by("id"):
                    num = num + 1
                    number = "R" + str(num)
                    Requirement.objects.filter(id=requirement_list1.id).update(
                        number=number
                    )

                requirement_list2 = Requirement.objects.filter(
                    project=project
                ).order_by("-id")[0]
                interger = requirement_list2.number[1:]
                number = "R" + str(int(interger) + 1)

        else:
            number = "R1"

        # then creating requirement

        goal_ids = request.POST.getlist("goal")
        stakeholder_ids = request.POST.getlist("stakeholder")

        if project.created_by == member:
            requirement = Requirement.objects.create(
                name=requirement_title,
                created_by=created_by,
                description=description,
                project=project,
                number=number,
                status="accepted",
            )
        else:
            requirement = Requirement.objects.create(
                name=requirement_title,
                created_by=created_by,
                description=description,
                number=number,
                project=project,
            )
        requirement.save()
        if goal_ids:
            for goal_id in goal_ids:
                goal = Goal.objects.get(id=goal_id)
                create_requirement_goal = RequirementGoal.objects.create(
                    goal=goal, requirement=requirement
                )
                create_requirement_goal.save()

            for stakeholder_id in stakeholder_ids:
                stakeholder = Stakeholder.objects.get(id=stakeholder_id)
                create_requirement_stakeholder = RequirementStakeholder.objects.create(
                    requirement=requirement, stakeholder=stakeholder
                )
                create_requirement_stakeholder.save()
            return redirect("projects:projectrequirements", project_id=project.id)
        message = "please select atleast One Goal"
        return render(
            request,
            "projects/requirements/create_requirement.html",
            {
                "indexhead": indexhead,
                "viewpoints": viewpoints,
                "member": member,
                "message": message,
                "goals": goals,
                "project": project,
                "stakeholders": stakeholders,
                "hidesearch": hidesearch,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    return render(
        request,
        "projects/requirements/create_requirement.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "member": member,
            "goals": goals,
            "stakeholders": stakeholders,
            "hidesearch": hidesearch,
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
        requirements = Requirement.objects.filter(
            Q(project=requirement.project, status="accepted")
            | Q(project=requirement.project, created_by=member)
        ).order_by("id")
        scenarios = (
            RequirementScenario.objects.filter(
                Q(requirement__id=requirement_id, scenario__status="accepted")
                | Q(requirement__id=requirement_id, scenario__created_by=member)
            )
            .order_by("scenario__id")
            .distinct("scenario__id")
        )
        project = Project.objects.get(id=requirement.project.id)
        project_id = project.id
        paginate = Paginator(scenarios, 10)
        page_number = request.GET.get("page")
        scenarios = paginate.get_page(page_number)
        return render(
            request,
            "projects/scenario/scenarios.html",
            {
                "indexhead": indexhead,
                "project_id": project_id,
                "requirements": requirements,
                "requirement": requirement,
                "scenarios": scenarios,
                "requirement_id": requirement_id,
                "member": member,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    requirement = Requirement.objects.get(id=requirement_id)
    project = Project.objects.get(id=requirement.project.id)
    scenarios = (
        RequirementScenario.objects.filter(
            scenario__project=project, requirement=requirement
        )
        .order_by("scenario__id")
        .distinct("scenario__id")
    )
    requirements = Requirement.objects.filter(project=project, status="accepted")

    project_id = project.id
    paginate = Paginator(scenarios, 10)
    page_number = request.GET.get("page")
    scenarios = paginate.get_page(page_number)
    return render(
        request,
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "requirements": requirements,
            "scenarios": scenarios,
            "requirement": requirement,
            "requirement_id": requirement_id,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewscenario(request, scenario_id=None, message=None):
    indexhead = "Scenario Description"

    member = Member.objects.get(user=request.user)

    if request.POST.get("scenario"):
        scenario_id = request.POST.get("scenario")
        scenario = RequirementScenario.objects.get(id=scenario_id)
        project = Project.objects.get(id=scenario.scenario.project.id)
        scenarios = (
            RequirementScenario.objects.filter(
                requirement=scenario.requirement, scenario__status="accepted"
            )
            .order_by("scenario__id")
            .distinct("scenario_id")
        )
        requirement_list = []
        for requirement in RequirementScenario.objects.filter(
            scenario=scenario.scenario
        ):
            requirement_list.append(requirement.requirement.id)
        requirements = Requirement.objects.filter(project=project).exclude(
            id__in=requirement_list
        )

        requirement_list = []
        for requirement in RequirementScenario.objects.filter(
            scenario=scenario.scenario
        ):
            requirement_list.append(requirement.requirement.id)
        requirements = Requirement.objects.filter(project=project).exclude(
            id__in=requirement_list
        )

        process_list = []
        for process in ScenarioProcess.objects.filter(scenario=scenario.scenario):
            process_list.append(process.process.id)

        processes = Process.objects.filter(project=project).exclude(id__in=process_list)

        usecase_list = []
        for usecase in ScenarioUsecase.objects.filter(scenario=scenario.scenario):
            usecase_list.append(usecase.usecase.id)

        usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)

        project_id = project.id
        comments = ScenarioComment.objects.filter(
            Q(scenario=scenario.scenario, comment__status="ccepted")
            | Q(scenario=scenario.scenario, comment__commented_by=member)
        ).order_by("id")
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
        rate_data = scenario_rates(request, scenario_id=scenario.scenario.id)
        if (
            scenario.scenario.created_by == member
            or scenario.scenario.project.created_by == member
        ):
            creator = "me"
        else:
            creator = "not me"
        stakeholders = ScenarioStakeholder.objects.filter(scenario=scenario.scenario)
        requirementss = RequirementScenario.objects.filter(scenario=scenario.scenario)
        processess = ScenarioProcess.objects.filter(scenario=scenario.scenario)
        usecasess = ScenarioUsecase.objects.filter(scenario=scenario.scenario)
        return render(
            request,
            "projects/scenario/view_scenario.html",
            {
                "indexhead": indexhead,
                "scenario": scenario,
                "requirementss": requirementss,
                "processess": processess,
                "usecasess": usecasess,
                "project_id": project_id,
                "stakeholders": stakeholders,
                "creator": creator,
                "scenarios": scenarios,
                "processes": processes,
                "usecases": usecases,
                "requirement": scenario.requirement,
                "requirements": requirements,
                "requirement_id": requirement.id,
                "rates": rates,
                "likes": likes,
                "hidesearch": 1,
                "rate_data": rate_data,
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
    scenario = RequirementScenario.objects.get(id=scenario_id)
    project = Project.objects.get(id=scenario.scenario.project.id)
    scenarios = (
        RequirementScenario.objects.filter(
            scenario__project=project, scenario__status="accepted"
        )
        .order_by("scenario__id")
        .distinct("scenario__id")
    )
    requirement_list = []
    for requirement in RequirementScenario.objects.filter(scenario=scenario.scenario):
        requirement_list.append(requirement.requirement.id)
    requirements = Requirement.objects.filter(project=project).exclude(
        id__in=requirement_list
    )

    process_list = []
    for process in ScenarioProcess.objects.filter(scenario=scenario.scenario):
        process_list.append(process.process.id)

    processes = Process.objects.filter(project=project).exclude(id__in=process_list)

    usecase_list = []
    for usecase in ScenarioUsecase.objects.filter(scenario=scenario.scenario):
        usecase_list.append(usecase.usecase.id)

    usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)

    project_id = project.id
    rate_data = scenario_rates(request, scenario_id=scenario.scenario.id)
    if scenario.scenario.created_by == member:
        creator = "me"
    else:
        creator = "not me"

    comments = ScenarioComment.objects.filter(
        Q(scenario=scenario.scenario, comment__status="ccepted")
        | Q(scenario=scenario.scenario, comment__commented_by=member)
    ).order_by("id")
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
    stakeholders = ScenarioStakeholder.objects.filter(scenario=scenario.scenario)
    requirementss = RequirementScenario.objects.filter(scenario=scenario.scenario)
    processess = ScenarioProcess.objects.filter(scenario=scenario.scenario)
    usecasess = ScenarioUsecase.objects.filter(scenario=scenario.scenario)
    return render(
        request,
        "projects/scenario/view_scenario.html",
        {
            "indexhead": indexhead,
            "requirementss": requirementss,
            "processess": processess,
            "usecasess": usecasess,
            "scenario": scenario,
            "processes": processes,
            "usecases": usecases,
            "stakeholders": stakeholders,
            "project_id": project_id,
            "scenarios": scenarios,
            "rate_data": rate_data,
            "requirements": requirements,
            "requirement": requirement,
            "rates": rates,
            "likes": likes,
            "hidesearch": 1,
            "creator": creator,
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
def createScenario(request, project_id):
    indexhead = "Create Scenario"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    requirements = Requirement.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("-id")
    if request.method == "POST":
        scenario_title = request.POST.get("scenario_title")
        description = request.POST.get("scenario_descriptions")
        created_by = Member.objects.get(user=request.user)
        requirement_ = request.POST.getlist("requirement")

        # creating scenario number
        scenario_list = Scenario.objects.filter(project=project)
        if scenario_list:
            scenario_list = scenario_list.order_by("-id")[0]
            if scenario_list.number != None:
                interger = scenario_list.number[1:]
                number = "S" + str(int(interger) + 1)
            else:
                num = 0
                for scenario_list1 in Scenario.objects.filter(project=project).order_by(
                    "id"
                ):
                    num = num + 1
                    number = "S" + str(num)
                    Scenario.objects.filter(id=scenario_list1.id).update(number=number)

                scenario_list2 = Scenario.objects.filter(project=project).order_by(
                    "-id"
                )[0]
                interger = scenario_list2.number[1:]
                number = "S" + str(int(interger) + 1)

        else:
            number = "S1"

        # then creating requirement
        if project.created_by == member:

            scenario = Scenario.objects.create(
                name=scenario_title,
                created_by=created_by,
                description=description,
                project=project,
                number=number,
                status="accepted",
            )
        else:
            scenario = Scenario.objects.create(
                name=scenario_title,
                created_by=created_by,
                description=description,
                number=number,
                project=project,
            )
        scenario.save()

        # then adding Requirement

        for require in requirement_:
            require = Requirement.objects.get(id=require)
            requirescenario = RequirementScenario.objects.create(
                requirement=require, scenario=scenario
            )
            requirescenario.save()
        for stakeholder_id in request.POST.getlist("stakeholder"):
            stakeholder = Stakeholder.objects.get(id=stakeholder_id)
            scenario_stakeholder = ScenarioStakeholder.objects.create(
                stakeholder=stakeholder, scenario=scenario
            )
            scenario_stakeholder.save()

        if scenario:
            return redirect("projects:projectscenarios", project_id=project.id)
    stakeholders = Stakeholder.objects.filter(project=project).order_by("name")
    return render(
        request,
        "projects/scenario/create_scenario.html",
        {
            "indexhead": indexhead,
            "requirements": requirements,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "stakeholders": stakeholders,
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
        requirement = Requirement.objects.get(id=requirement_id)
        processes = (
            RequirementProcess.objects.filter(
                Q(requirement=requirement, process__status="accepted")
                | Q(requirement=requirement, process__created_by=member)
            )
            .exclude(process_id__in=Process.objects.filter(status="deleted"))
            .order_by("process__id")
            .distinct("process__id")
        )

        project = Project.objects.get(id=requirement.project.id)

        project_id = project.id
        paginate = Paginator(processes, 10)
        page_number = request.GET.get("page")
        processes = paginate.get_page(page_number)
        return render(
            request,
            "projects/process/process.html",
            {
                "indexhead": indexhead,
                "project_id": project_id,
                "processes": processes,
                "requirement_id": requirement.id,
                "requirement": requirement,
                "member": member,
                "hideseach": 1,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )

    requirement = Requirement.objects.get(id=requirement_id)
    project = Project.objects.get(id=requirement.project.id)
    project_id = project.id
    processes = (
        RequirementProcess.objects.filter(
            Q(requirement=requirement, process__status="accepted")
            | Q(requirement=requirement, process__created_by=member)
        )
        .exclude(process_id__in=Process.objects.filter(status="deleted"))
        .order_by("process__id")
        .distinct("process__id")
    )
    paginate = Paginator(processes, 10)
    page_number = request.GET.get("page")
    processes = paginate.get_page(page_number)
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "requirement": requirement,
            "processes": processes,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
            "hideseach": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewprocess(request, process_id=None, message=None):
    indexhead = "Process Description"
    member = Member.objects.get(user=request.user)

    if request.method == "POST":
        processid = request.POST.get("process")
        process = RequirementProcess.objects.get(id=processid)
        processes = (
            RequirementProcess.objects.filter(
                Q(requirement=process.requirement, process__status="accepted")
                | Q(requirement=process.requirement, process__created_by=member)
            )
            .order_by("-process__id")
            .distinct("process__id")
        )
        requirement = Requirement.objects.get(id=process.requirement.id)
        project = Project.objects.get(id=process.process.project.id)
        project_id = project.id
        comments = ProcessComment.objects.filter(
            Q(process=process.process, comment__status="accepted")
            | Q(process=process.process, comment__commented_by=member)
        ).order_by("id")
        processRate = ProcessRate.objects.filter(
            process=process.process, star_rate__rated_by=member
        )
        rates = ProcessRate.objects.filter(process=process.process).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        likes = ProcessLike.objects.filter(process=process.process).count()
        dislikes = ProcessDislike.objects.filter(process=process.process).count()
        rate_data = process_rates(request, process_id=process.process.id)
        if process.process.created_by == member or project.created_by == member:
            creator = "me"
        else:
            creator = "not me"

        requirement_list = []
        for requirement in RequirementProcess.objects.filter(process=process.process):
            requirement_list.append(requirement.requirement.id)
        requirements = Requirement.objects.filter(project=project).exclude(
            id__in=requirement_list
        )

        scenario_list = []
        for scenario in ScenarioProcess.objects.filter(process=process.process):
            scenario_list.append(scenario.scenario.id)
        scenarios = Scenario.objects.filter(project=project).exclude(
            id__in=scenario_list
        )

        usecase_list = []
        for usecase in ProcessUsecase.objects.filter(process=process.process):
            usecase_list.append(usecase.usecase.id)
        usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)

        stakeholders = ProcessStakeholder.objects.filter(process=process.process)
        requirementss = RequirementProcess.objects.filter(process=process.process)
        scenarioss = ScenarioProcess.objects.filter(process=process.process)
        usecasess = ProcessUsecase.objects.filter(process=process.process)
        return render(
            request,
            "projects/process/view_process.html",
            {
                "indexhead": indexhead,
                "project_id": project_id,
                "process": process,
                "requirementss": requirementss,
                "scenarioss": scenarioss,
                "usecasess": usecasess,
                "usecases": usecases,
                "requirements": requirements,
                "scenarios": scenarios,
                "stakeholders": stakeholders,
                "rates": rates,
                "creator": creator,
                "likes": likes,
                "dislikes": dislikes,
                "total_rates": total_rates,
                "processRate": processRate,
                "comments": comments,
                "rate_data": rate_data,
                "total_comments": total_comments,
                "processes": processes,
                "member": member,
                "hidesearch": 1,
                "project": project,
                "notification": notification(request),
                "total_notification": total_notification(request),
            },
        )
    print("failed to chip in")
    process = RequirementProcess.objects.get(id=process_id)
    comments = ProcessComment.objects.filter(
        Q(process=process.process, comment__status="accepted")
        | Q(process=process.process, comment__commented_by=member)
    ).order_by("id")
    processRate = ProcessRate.objects.filter(
        process=process.process, star_rate__rated_by=member
    )
    rates = ProcessRate.objects.filter(process=process.process).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = ProcessLike.objects.filter(process=process.process).count()
    dislikes = ProcessDislike.objects.filter(process=process.process).count()
    project = Project.objects.get(id=process.process.project.id)
    processes = (
        RequirementProcess.objects.filter(
            process__project=project, process__status="accepted"
        )
        .order_by("-process__id")
        .distinct("process__id")
    )
    project_id = project.id
    rate_data = process_rates(request, process_id=process.process.id)
    if process.process.created_by == member or project.created_by == member:
        creator = "me"
    else:
        creator = "not me"

    requirement_list = []
    for requirement in RequirementProcess.objects.filter(process=process.process):
        requirement_list.append(requirement.requirement.id)
    requirements = Requirement.objects.filter(project=project).exclude(
        id__in=requirement_list
    )

    scenario_list = []
    for scenario in ScenarioProcess.objects.filter(process=process.process):
        scenario_list.append(scenario.scenario.id)
    scenarios = Scenario.objects.filter(project=project).exclude(id__in=scenario_list)

    usecase_list = []
    for usecase in ProcessUsecase.objects.filter(process=process.process):
        usecase_list.append(usecase.usecase.id)
    usecases = UseCase.objects.filter(project=project).exclude(id__in=usecase_list)
    stakeholders = ProcessStakeholder.objects.filter(process=process.process)
    stakeholders = ProcessStakeholder.objects.filter(process=process.process)
    requirementss = RequirementProcess.objects.filter(process=process.process)
    scenarioss = ScenarioProcess.objects.filter(process=process.process)
    usecasess = ProcessUsecase.objects.filter(process=process.process)
    return render(
        request,
        "projects/process/view_process.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "process": process,
            "requirementss": requirementss,
            "scenarioss": scenarioss,
            "usecasess": usecasess,
            "rate_data": rate_data,
            "stakeholders": stakeholders,
            "creator": creator,
            "processes": processes,
            "usecases": usecases,
            "requirements": requirements,
            "scenarios": scenarios,
            "rates": rates,
            "likes": likes,
            "dislikes": dislikes,
            "total_rates": total_rates,
            "processRate": processRate,
            "comments": comments,
            "total_comments": total_comments,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def createProcess(request, project_id):
    indexhead = "Create Process"
    member = Member.objects.get(user=request.user)

    project = Project.objects.get(id=project_id)
    requirements = Requirement.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("-id")
    if request.method == "POST":
        process_title = request.POST.get("process_title")
        description = request.POST.get("process_descriptions")
        created_by = Member.objects.get(user=request.user)
        require = request.POST.getlist("requirement")

        # creating process number
        process_list = Process.objects.filter(project=project)
        if process_list:
            process_list = process_list.order_by("-id")[0]
            if process_list.number != None:
                interger = process_list.number[1:]
                number = "P" + str(int(interger) + 1)
            else:
                num = 0
                for process_list1 in Process.objects.filter(project=project).order_by(
                    "id"
                ):
                    num = num + 1
                    number = "P" + str(num)
                    Process.objects.filter(id=process_list1.id).update(number=number)

                process_list2 = Process.objects.filter(project=project).order_by("-id")[
                    0
                ]
                interger = process_list2.number[1:]
                number = "P" + str(int(interger) + 1)

        else:
            number = "P1"

        if project.created_by == member:
            process = Process.objects.create(
                process_name=process_title,
                created_by=created_by,
                description=description,
                project=project,
                number=number,
                status="accepted",
            )
        else:
            process = Process.objects.create(
                process_name=process_title,
                created_by=created_by,
                description=description,
                number=number,
                project=project,
            )
        process.save()

        # adding requirement to process many to many process

        for require in require:

            require = Requirement.objects.get(id=require)
            requireprocess = RequirementProcess.objects.create(
                requirement=require, process=process
            )
            requireprocess.save()
        for stakeholder_id in request.POST.getlist("stakeholder"):
            stakeholder = Stakeholder.objects.get(id=stakeholder_id)
            create_process_stakeholder = ProcessStakeholder.objects.create(
                process=process, stakeholder=stakeholder
            )
            create_process_stakeholder.save()

        if process:
            return redirect("projects:projectprocesses", project_id=project_id)
        else:
            HttpResponse("failed to create")
    stakeholders = Stakeholder.objects.filter(project=project).order_by("name")
    return render(
        request,
        "projects/process/create_process.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "requirements": requirements,
            "member": member,
            "hidesearch": 1,
            "stakeholders": stakeholders,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def usecases(request, requirement_id):
    indexhead = "Associated Requirement Use cases"
    member = Member.objects.get(user=request.user)
    requirement = Requirement.objects.get(id=requirement_id)
    project = Project.objects.get(id=requirement.project.id)
    usecases = (
        RequirementUsecase.objects.filter(
            Q(requirement__id=requirement_id, usecase__status="accepted")
            | Q(requirement__id=requirement_id, usecase__created_by=member)
        )
        .exclude(
            usecase_id__in=UseCase.objects.filter(
                Q(status="deleted") | Q(status="blocked") | Q(status="rejected")
            )
        )
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    requirements = Requirement.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("id")
    project_id = project.id
    paginate = Paginator(usecases, 10)
    page_number = request.GET.get("page")
    usecases = paginate.get_page(page_number)
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "requirement": requirement,
            "scenarios": scenarios,
            "goals": goals,
            "usecases": usecases,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def viewusecase(request, usecase_id=None, message=None):
    indexhead = "Usecase Description"
    member = Member.objects.get(user=request.user)

    if request.POST.get("usecase"):
        usecase_id = request.POST.get("usecase")
        usecase = RequirementUsecase.objects.get(id=usecase_id)
        project = Project.objects.get(id=usecase.usecase.project.id)
        usecases = (
            RequirementUsecase.objects.filter(
                requirement__project=project, usecase__status="accepted"
            )
            .order_by("-usecase__id")
            .distinct("usecase__id")
        )
        likes = UseCaseLike.objects.filter(use_case=usecase.usecase).count()
        dislikes = UseCaseDislike.objects.filter(use_case=usecase.usecase).count()
        project_id = project.id
        comments = UseCaseComment.objects.filter(
            Q(usecase=usecase.usecase, comment__status="accepted")
            | Q(usecase=usecase.usecase, comment__commented_by=member)
        ).order_by("id")
        usecaseRate = UseCaseRate.objects.filter(
            usecase=usecase.usecase, star_rate__rated_by=member
        )
        rates = UseCaseRate.objects.filter(usecase=usecase.usecase).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
        rate_data = usecase_rates(request, usecase_id=usecase.usecase.id)
        if (
            usecase.usecase.created_by == member
            or usecase.usecase.project.created_by == member
        ):
            creator = "me"
        else:
            creator = "not me"
        requirement_list = []
        for requirement in RequirementUsecase.objects.filter(usecase=usecase.usecase):
            requirement_list.append(requirement.requirement.id)

        requirements = Requirement.objects.filter(project=project).exclude(
            id__in=requirement_list
        )

        scenario_list = []
        for scenario in ScenarioUsecase.objects.filter(usecase=usecase.usecase):
            scenario_list.append(scenario.scenario.id)

        scenarios = Scenario.objects.filter(project=project).exclude(
            id__in=scenario_list
        )

        process_list = []
        for process in ProcessUsecase.objects.filter(usecase=usecase.usecase):
            process_list.append(process.process.id)
        processes = Process.objects.filter(project=project).exclude(id__in=process_list)

        stakeholders = UsecaseStakeholder.objects.filter(usecase=usecase.usecase)
        requirementss = RequirementUsecase.objects.filter(usecase=usecase.usecase)
        scenarioss = ScenarioUsecase.objects.filter(usecase=usecase.usecase)
        processess = ProcessUsecase.objects.filter(usecase=usecase.usecase)
        return render(
            request,
            "projects/usecase/view_usecase.html",
            {
                "indexhead": indexhead,
                "project_id": project_id,
                "creator": creator,
                "usecase": usecase,
                "processes": processes,
                "requirementss": requirementss,
                "scenarioss": scenarioss,
                "processess": processess,
                "scenarios": scenarios,
                "requirements": requirements,
                "stakeholders": stakeholders,
                "usecases": usecases,
                "usecase_id": usecase.id,
                "rates": rates,
                "likes": likes,
                "hidesearch": 1,
                "rate_data": rate_data,
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
    usecase = RequirementUsecase.objects.get(id=usecase_id)
    project = Project.objects.get(id=usecase.usecase.project.id)
    usecases = (
        RequirementUsecase.objects.filter(
            requirement__project=project, usecase__status="accepted"
        )
        .order_by("-usecase__id")
        .distinct("usecase__id")
    )
    project_id = project.id
    rate_data = usecase_rates(request, usecase_id=usecase.usecase.id)
    if usecase.usecase.created_by == member:
        creator = "me"
    else:
        creator = "not me"
    comments = UseCaseComment.objects.filter(
        Q(usecase=usecase.usecase, comment__status="accepted")
        | Q(usecase=usecase.usecase, comment__commented_by=member)
    ).order_by("id")
    usecaseRate = UseCaseRate.objects.filter(
        usecase=usecase.usecase, star_rate__rated_by=member
    )
    rates = UseCaseRate.objects.filter(usecase=usecase.usecase).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    likes = UseCaseLike.objects.filter(use_case=usecase.usecase).count()
    dislikes = UseCaseDislike.objects.filter(use_case=usecase.usecase).count()

    stakeholders = UsecaseStakeholder.objects.filter(usecase=usecase.usecase)

    requirement_list = []
    for requirement in RequirementUsecase.objects.filter(usecase=usecase.usecase):
        requirement_list.append(requirement.requirement.id)

    requirements = Requirement.objects.filter(project=project).exclude(
        id__in=requirement_list
    )

    scenario_list = []
    for scenario in ScenarioUsecase.objects.filter(usecase=usecase.usecase):
        scenario_list.append(scenario.scenario.id)

    scenarios = Scenario.objects.filter(project=project).exclude(id__in=scenario_list)

    process_list = []
    for process in ProcessUsecase.objects.filter(usecase=usecase.usecase):
        process_list.append(process.process.id)
    processes = Process.objects.filter(project=project).exclude(id__in=process_list)
    requirementss = RequirementUsecase.objects.filter(usecase=usecase.usecase)
    scenarioss = ScenarioUsecase.objects.filter(usecase=usecase.usecase)
    processess = ProcessUsecase.objects.filter(usecase=usecase.usecase)
    return render(
        request,
        "projects/usecase/view_usecase.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "stakeholders": stakeholders,
            "processes": processes,
            "requirementss": requirementss,
            "scenarioss": scenarioss,
            "processess": processess,
            "scenarios": scenarios,
            "requirements": requirements,
            "creator": creator,
            "rate_data": rate_data,
            "usecase": usecase,
            "usecases": usecases,
            "usecase_id": usecase_id,
            "rates": rates,
            "likes": likes,
            "hidesearch": 1,
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
def createUsecase(request, project_id):
    indexhead = "Create Usecase"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    project_id = project.id
    stakeholders = Stakeholder.objects.filter(project=project).order_by("name")

    requirements = Requirement.objects.filter(
        Q(project=project, status="accepted") | Q(project=project, created_by=member)
    ).order_by("-id")
    if request.method == "POST":
        usecase_title = request.POST.get("usecase_title")
        description = request.POST.get("usecase_descriptions")
        created_by = Member.objects.get(user=request.user)
        require = request.POST.getlist("requirement")

        # creating usecase number
        usecase_list = UseCase.objects.filter(project=project)
        if usecase_list:
            usecase_list = usecase_list.order_by("-id")[0]
            if usecase_list.number != None:
                interger = usecase_list.number[1:]
                number = "U" + str(int(interger) + 1)
            else:
                num = 0
                for usecase_list1 in UseCase.objects.filter(project=project).order_by(
                    "id"
                ):
                    num = num + 1
                    number = "U" + str(num)
                    UseCase.objects.filter(id=usecase_list1.id).update(number=number)

                usecase_list2 = UseCase.objects.filter(project=project).order_by("-id")[
                    0
                ]
                interger = usecase_list2.number[1:]
                number = "U" + str(int(interger) + 1)

        else:
            number = "U1"

        # then creating requirement
        if project.created_by == member:
            usecase = UseCase.objects.create(
                usecase_name=usecase_title,
                created_by=created_by,
                description=description,
                project=project,
                number=number,
                status="accepted",
            )
        else:
            usecase = UseCase.objects.create(
                usecase_name=usecase_title,
                created_by=created_by,
                description=description,
                number=number,
                project=project,
            )
        usecase.save()

        # Then adding requirement:

        for require in require:
            require = Requirement.objects.get(id=require)
            requireusecase = RequirementUsecase.objects.create(
                requirement=require, usecase=usecase
            )
            requireusecase.save()
        for stakeholder_id in request.POST.getlist("stakeholder"):
            stakeholder = Stakeholder.objects.get(id=stakeholder_id)
            create_usecase_stakeholder = UsecaseStakeholder.objects.create(
                stakeholder=stakeholder, usecase=usecase
            )
            create_usecase_stakeholder.save()

        if usecase:
            return redirect("projects:projectusecases", project_id=project_id)

    return render(
        request,
        "projects/usecase/create_usecase.html",
        {
            "indexhead": indexhead,
            "member": member,
            "project": project,
            "requirements": requirements,
            "hidesearch": 1,
            "stakeholders": stakeholders,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# Rate


@login_required(login_url="login")
def projectRate(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if (
        ProjectMembership.objects.filter(
            project=project, member=member, status="active"
        ).exists()
        or project.project_visibility == "public"
    ):
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
                        if project.created_by == member:
                            return redirect(
                                "projects:viewmyproject", project_id=project_id
                            )
                        return redirect(request.META["HTTP_REFERER"])

            return redirect(request.META["HTTP_REFERER"])
        message = "sorry you can not rate zero star, rate start from one star !!"
        return viewProject(request, project_id=project_id, message=message)
    message = "sorry you can not Rate on this project now,you are not a active member of this project"
    return viewProject(request, project_id=project_id, message=message)


@login_required(login_url="login")
def viewpointRate(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    project = Project.objects.get(viewpoint=viewpoint)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ViewPointRate.objects.filter(
            viewpoint=viewpoint, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                viewpoint_rate = ViewPointRate.objects.create(
                    viewpoint=viewpoint, star_rate=rate
                )
                viewpoint_rate.save()
                if viewpoint_rate:
                    project_id = viewpoint.project.id
                    return redirect(request.META["HTTP_REFERER"])

        message = "sorry you have already rated this Viewpoint you can not rate again"
        return redirect(request.META["HTTP_REFERER"])
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
                    return redirect(request.META["HTTP_REFERER"])

        message = "sorry you have already rated this Goal you can not rate it again"
        return redirect("projects:viewgoal", goal_id=goal.id)
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect(request.META["HTTP_REFERER"])


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
                    return redirect(request.META["HTTP_REFERER"])

        return redirect(request.META["HTTP_REFERER"])

    return redirect(request.META["HTTP_REFERER"])


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
                    return redirect(request.META["HTTP_REFERER"])

        message = "sorry you have already rated this Scenario you can not rate it again"
        return redirect(request.META["HTTP_REFERER"])
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewscenario", scenario_id=scenario.id)


@login_required(login_url="login")
def processRate(request, process_id):
    process = RequirementProcess.objects.get(id=process_id)
    # project = Project.objects.get(id=process.scenario.goal.requiremt.project.id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ProcessRate.objects.filter(
            process=process.process, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                process_rate = ProcessRate.objects.create(
                    process=process.process, star_rate=rate
                )
                process_rate.save()
                if process_rate:
                    return redirect(request.META["HTTP_REFERER"])

        message = "sorry you have already rated this process you can not rate it again"
        return redirect(request.META["HTTP_REFERER"])
    message = "sorry you can not rate zero star, rate start from one star !!"
    return redirect("projects:viewprocess", process_id=process.id)


@login_required(login_url="login")
def usecaseRate(request, usecase_id):
    usecase = RequirementUsecase.objects.get(id=usecase_id)
    # project = Project.objects.get(id=process.scenario.goal.requiremt.project.id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not UseCaseRate.objects.filter(
            usecase=usecase.usecase, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                usecase_rate = UseCaseRate.objects.create(
                    usecase=usecase.usecase, star_rate=rate
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
    if (
        ProjectMembership.objects.filter(
            project=project, member=member, status="active"
        ).exists()
        or project.project_visibility == "public"
    ):

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
    project = Project.objects.get(id=goal.project.id)
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
    project = Project.objects.get(id=requirement.project.id)
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
            "resources": resources,
            "requirement_id": requirement.id,
            "requirement": requirement,
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
    project = Project.objects.get(id=scenario.scenario.project.id)
    resources = ScenarioRepository.objects.filter(scenario=scenario.scenario).order_by(
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
            "resources": resources,
            "scenario_id": scenario.id,
            "scenario": scenario.scenario,
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
    process = RequirementProcess.objects.get(id=process_id)
    project = Project.objects.get(id=process.process.project.id)
    resources = ProcessRepository.objects.filter(process=process.process).order_by(
        "-id"
    )
    member = Member.objects.get(user=request.user)
    project_id = project.id
    return render(
        request,
        "projects/viewpoints/resources.html",
        {
            "indexhead": indexhead,
            "resources": resources,
            "process": process.process,
            "process_id": process.id,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def usecaseResources(request, usecase_id):
    indexhead = "Usecase Resources:"
    hidesearch = "hide"
    usecase = RequirementUsecase.objects.get(id=usecase_id)
    project = Project.objects.get(id=usecase.usecase.project.id)
    resources = UsecaseRepository.objects.filter(usecase=usecase.usecase).order_by(
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
            "resources": resources,
            "usecase_id": usecase.id,
            "usecase": usecase.usecase,
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
    process = RequirementProcess.objects.get(id=process_id)
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
                process=process.process, repository=repository
            )
            processrepository.save()
            if processrepository:
                return redirect("projects:processresources", process_id)
    return redirect("projects:processresources", process_id)


@login_required(login_url="login")
def addUsecaseResources(request, usecase_id):
    usecase = RequirementUsecase.objects.get(id=usecase_id)
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
                usecase=usecase.usecase, repository=repository
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
        if goal.project.created_by == member:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member
            )
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
                return redirect(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def requirementComment(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if requirement.project.created_by == member:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member
            )
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
                return redirect(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def scenarioComment(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if scenario.scenario.project.created_by == member:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member
            )
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
    process = RequirementProcess.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if process.process.project.created_by == member:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member
            )
        create_comment.save()
        process_comment = ProcessComment.objects.create(
            comment=create_comment, process=process.process
        )
        process_comment.save()
        if process_comment:
            if process.process.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(process.created_by)
                    + " You have one new comment on "
                    + str(process.process)
                    + " Process from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=process.process.created_by,
                    activity=activity,
                    link=link,
                )
                return redirect("projects:viewprocess", process_id=process_id)
    return redirect("projects:viewprocess", process_id=process_id)


@login_required(login_url="login")
def usecaseComment(request, usecase_id):
    usecase = RequirementUsecase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get("comment")
        if usecase.usecase.project.created_by == member:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member, status="accepted"
            )
        else:
            create_comment = Comment.objects.create(
                comment=comment, commented_by=member
            )
        create_comment.save()
        usecase_comment = UseCaseComment.objects.create(
            comment=create_comment, usecase=usecase.usecase
        )
        usecase_comment.save()
        if usecase_comment:
            if usecase.usecase.created_by != member:
                link = "commented"
                activity = (
                    "Dear "
                    + str(usecase.usecase.created_by)
                    + " You have one new comment on "
                    + str(usecase.usecase)
                    + " Use Case from "
                    + str(member)
                )
                notify(
                    request,
                    affected_user=usecase.usecase.created_by,
                    activity=activity,
                    link=link,
                )
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

    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def deleteNotifications(request):
    member = Member.objects.get(user=request.user)
    read_all = ActivityLog.objects.filter(affected_user=member).delete()

    return redirect(request.META["HTTP_REFERER"])


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


# global viewpoints to usecase
@login_required(login_url="login")
def general_goals(request, project_id):
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    goals = (
        ViewpointGoal.objects.filter(
            Q(goal__project=project, goal__status="accepted")
            | Q(goal__project=project, goal__created_by=member)
        )
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginate.get_page(page_number)
    indexhead = "Project Goals"

    return render(
        request,
        "projects/Goals/goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "member": member,
            "project_id": project_id,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def general_requirements(request, project_id):
    indexhead = "Project Requirements"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    requirements = (
        RequirementGoal.objects.filter(
            Q(requirement__project=project, requirement__status="accepted")
            | Q(requirement__project=project, requirement__created_by=member)
        )
        .order_by("requirement__id", "requirement")
        .distinct("requirement__id", "requirement")
    )
    paginate = Paginator(requirements, 10)
    page_number = request.GET.get("page")
    requirements = paginate.get_page(page_number)
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
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def general_scenario(request, project_id):
    indexhead = "Project Scenarios"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    scenarios = (
        RequirementScenario.objects.filter(
            Q(requirement__project=project, scenario__status="accepted")
            | Q(requirement__project=project, scenario__created_by=member)
        )
        .exclude(
            scenario_id__in=Scenario.objects.filter(
                Q(status="deleted") | Q(status="blocked") | Q(status="rejected")
            )
        )
        .order_by("scenario__id")
        .distinct("scenario__id")
    )
    paginate = Paginator(scenarios, 10)
    page_number = request.GET.get("page")
    scenarios = paginate.get_page(page_number)
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
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def general_process(request, project_id):
    indexhead = "Project Process"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    processes = (
        RequirementProcess.objects.filter(
            Q(requirement__project=project, process__status="accepted")
            | Q(requirement__project=project, process__created_by=member)
        )
        .exclude(
            process_id__in=Process.objects.filter(
                Q(status="deleted") | Q(status="blocked") | Q(status="rejected")
            )
        )
        .order_by("process__id")
        .distinct("process__id")
    )
    paginate = Paginator(processes, 10)
    page_number = request.GET.get("page")
    processes = paginate.get_page(page_number)
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "processes": processes,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


@login_required(login_url="login")
def general_usecase(request, project_id):
    indexhead = "Project Use Cases"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    usecases = (
        RequirementUsecase.objects.filter(
            Q(requirement__project=project, usecase__status="accepted")
            | Q(requirement__project=project, usecase__created_by=member)
        )
        .exclude(
            usecase_id__in=UseCase.objects.filter(
                Q(status="deleted") | Q(status="blocked") | Q(status="rejected")
            )
        )
        .order_by("usecase__id", "usecase")
        .distinct("usecase__id", "usecase")
    )
    paginate = Paginator(usecases, 10)
    page_number = request.GET.get("page")
    usecases = paginate.get_page(page_number)
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "project_id": project_id,
            "usecases": usecases,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


# project reports
@login_required(login_url="login")
def my_project_reports(request, project_id):
    indexhead = "Project Reports"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)

    def user_reports(request, project_id):
        female_members = ProjectMembership.objects.filter(
            project=project, member__gender="Female"
        ).count()
        male_members = ProjectMembership.objects.filter(
            project=project, member__gender="Male"
        ).count()
        gender = [female_members, male_members]
        return gender

    def contribution_reports(request, project_id):

        viewpoints = Viewpoint.objects.filter(project=project).count()
        goals = Goal.objects.filter(project=project).count()
        requirements = Requirement.objects.filter(project=project).count()
        scenarios = Scenario.objects.filter(project=project).count()
        processes = Process.objects.filter(project=project).count()
        usecases = UseCase.objects.filter(project=project).count()
        contributions = [
            viewpoints,
            goals,
            requirements,
            scenarios,
            processes,
            usecases,
        ]
        return contributions

    def viewpoint_contributions(request, project_id):
        accepted_viewpoints = Viewpoint.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_viewpoints = Viewpoint.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        pending_viewpoints = Viewpoint.objects.filter(
            project__id=project_id, status="pending"
        ).count()
        allviewpoints = [accepted_viewpoints, rejected_viewpoints, pending_viewpoints]
        return allviewpoints

    def goals_contributions(request, project_id):
        accepted_goals = Goal.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_goals = Goal.objects.filter(
            project__id=project_id, status="rejected"
        ).count()
        all_goals = [accepted_goals, rejected_goals]
        return all_goals

    def requirement_contributions(request, project_id):
        accepted_requirements = Requirement.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_requirements = Requirement.objects.filter(
            project__id=project_id, status="rejected"
        ).count()
        all_requirements = [accepted_requirements, rejected_requirements]
        return all_requirements

    def scenario_contributions(request, project_id):
        accepted_scenarios = Scenario.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_scenarios = Scenario.objects.filter(
            project__id=project_id, status="rejected"
        ).count()
        all_scenarios = [accepted_scenarios, rejected_scenarios]
        return all_scenarios

    def process_contributions(request, project_id):
        accepted_process = Process.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_process = Process.objects.filter(
            project__id=project_id, status="rejected"
        ).count()
        pending_process = Process.objects.filter(
            project__id=project_id, status="pending"
        ).count()
        all_process = [accepted_process, rejected_process, pending_process]
        return all_process

    def usecase_contributions(request, project_id):
        accepted_usecase = UseCase.objects.filter(
            project__id=project_id, status="accepted"
        ).count()
        rejected_usecase = UseCase.objects.filter(
            project__id=project_id, status="rejected"
        ).count()
        pending_usecase = UseCase.objects.filter(
            project__id=project_id, status="pending"
        ).count()
        all_usecases = [accepted_usecase, rejected_usecase, pending_usecase]
        return all_usecases

    return render(
        request,
        "projects/my_projects/general_reports.html",
        {
            "user_reports": user_reports(request, project_id=project_id),
            "contribution_reports": contribution_reports(
                request, project_id=project_id
            ),
            "all_viewpoints": viewpoint_contributions(request, project_id),
            "all_goals": goal_contributions(request, project_id),
            "all_requirements": requirement_contributions(request, project_id),
            "all_scenarios": scenario_contributions(request, project_id),
            "all_process": process_contributions(request, project_id),
            "all_usecases": usecase_contributions(request, project_id),
            "hidesearch": hidesearch,
            "project_id": project_id,
            "project": project,
            "member": member,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def general_report(request):
    indexhead = "General Reports"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)

    def member_report(request):
        female = Member.objects.filter(gender="Female").count()
        male = Member.objects.filter(gender="Male").count()

        gender = [male, female]
        print(gender)
        return gender

    def Project_report(request):

        Invitational_projects = Project.objects.filter(
            is_invitational=True, is_discoverable=False
        ).count()
        discoverable_projects = Project.objects.filter(
            is_discoverable=True, is_invitational=False
        ).count()
        invitaional_and_discoverable = Project.objects.filter(
            is_invitational=True, is_discoverable=True
        ).count()
        is_public = Project.objects.filter(project_visibility="public").count()
        my_projects = Project.objects.filter(created_by=member).count()

        projects = [
            Invitational_projects,
            discoverable_projects,
            invitaional_and_discoverable,
            is_public,
            my_projects,
        ]
        print(projects)
        return projects

    return render(
        request,
        "projects/general_reports.html",
        {
            "member_reports": member_report(request),
            "project_reports": Project_report(request),
            "hidesearch": hidesearch,
            "member": member,
            "indexhead": indexhead,
        },
    )


# Updating from Project to usecase
@login_required(login_url="login")
def update_viewpoint(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    viewpoint_name = request.POST.get("viewpoint_name")
    viewpoint_photo = request.FILES.get("viewpoint_photo")
    description = request.POST.get("description")

    if viewpoint_photo == "" or viewpoint_photo == None:
        viewpoint_photo = viewpoint.viewpoint_photo

    # Then updating viewpoint
    update_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(
        viewpoint_name=viewpoint_name,
        viewpoint_photo=viewpoint_photo,
        description=description,
    )
    if update_viewpoint:
        return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)
    return redirect("projects:viewpoint", viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def update_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    goal_name = request.POST.get("goal_name")
    description = request.POST.get("description")

    # Then updating goal
    update_goal = Goal.objects.filter(id=goal_id).update(
        goal_name=goal_name, description=description
    )
    if update_goal:
        return redirect(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def update_requirement(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    requirement_name = request.POST.get("requirement_name")
    description = request.POST.get("description")

    # Then updating requirement
    update_requirement = Requirement.objects.filter(id=requirement_id).update(
        name=requirement_name, description=description
    )
    if update_requirement:
        return redirect(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def update_scenario(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    scenario_name = request.POST.get("scenario_name")
    description = request.POST.get("description")

    # Then updating scenario
    update_scenario = Scenario.objects.filter(id=scenario.scenario.id).update(
        name=scenario_name, description=description
    )
    if update_scenario:
        return redirect("projects:viewscenario", scenario_id=scenario_id)
    return redirect("projects:viewscenario", scenario_id=scenario_id)


@login_required(login_url="login")
def update_process(request, process_id):
    process = RequirementProcess.objects.get(id=process_id)
    process_name = request.POST.get("process_name")
    description = request.POST.get("description")

    # Then updating process
    update_process = Process.objects.filter(id=process.process.id).update(
        process_name=process_name, description=description
    )
    if update_process:
        return redirect(request.META["HTTP_REFERER"])
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def update_usecase(request, usecase_id):
    usecase = RequirementUsecase.objects.get(id=usecase_id)
    usecase_name = request.POST.get("usecase_name")
    description = request.POST.get("description")

    # Then updating usecase
    update_usecase = UseCase.objects.filter(id=usecase.usecase.id).update(
        usecase_name=usecase_name, description=description
    )
    if update_usecase:
        return redirect("projects:viewusecase", usecase_id=usecase_id)
    return redirect("projects:viewusecase", usecase_id=usecase_id)


# delete from viewpoint to usecase:
@login_required(login_url="login")
def delete_viewpoint(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    delete_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).delete()
    if delete_viewpoint:
        return redirect("projects:viewpoints", project_id=viewpoint.project.id)


@login_required(login_url="login")
def delete_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)

    delete_goal = Goal.objects.filter(id=goal_id).delete()

    if delete_goal:
        return redirect("projects:projectgoals", project_id=goal.project.id)


@login_required(login_url="login")
def delete_requirement(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    delete_requirement = Requirement.objects.filter(id=requirement_id).delete()
    if delete_requirement:
        return redirect(
            "projects:projectrequirements", project_id=requirement.project.id
        )


@login_required(login_url="login")
def delete_scenario(request, scenario_id):
    scenario = RequirementScenario.objects.get(id=scenario_id)
    delete_scenario = Scenario.objects.filter(id=scenario.scenario.id).delete()
    if delete_scenario:
        return redirect(
            "projects:projectscenarios", project_id=scenario.scenario.project.id
        )


@login_required(login_url="login")
def delete_process(request, process_id):
    process = RequirementProcess.objects.get(id=process_id)
    delete_process = Process.objects.filter(id=process.process.id).delete()
    if delete_process:
        return redirect(
            "projects:projectprocesses", project_id=process.process.project.id
        )


@login_required(login_url="login")
def delete_usecase(request, usecase_id):
    usecase = RequirementUsecase.objects.get(id=usecase_id)

    delete_usecase = UseCase.objects.filter(id=usecase.usecase.id).delete()
    if delete_usecase:
        return redirect(
            "projects:projectusecases", project_id=usecase.usecase.project.id
        )


# Contribution approval, rejections and blocks
@login_required(login_url="login")
def project_contributions(request, project_id):
    indexhead = "Project Comments Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    comments = ProjectComment.objects.filter(
        project=project, comment__status="pending"
    ).order_by("id")
    paginator = Paginator(comments, 10)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)

    return render(
        request,
        "projects/my_projects/project_contributions.html",
        {
            "project": project,
            "project_id": project.id,
            "member": member,
            "project_comments": comments,
            "total_comments": ProjectComment.objects.filter(
                project=project, comment__status="pending"
            ).count(),
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def viewpoint_contributions(request, project_id):
    indexhead = "Viewpoint Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    viewpoints = Viewpoint.objects.filter(project=project, status="pending").order_by(
        "id"
    )
    paginator = Paginator(viewpoints, 10)
    page_number = request.GET.get("page")
    viewpoints = paginator.get_page(page_number)

    comments = ViewPointComment.objects.filter(
        viewpoint__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)

    return render(
        request,
        "projects/my_projects/viewpoint_contributions.html",
        {
            "viewpoints": viewpoints,
            "project": project,
            "project_id": project.id,
            "viewpoint_comments": comments,
            "total_comments": ViewPointComment.objects.filter(
                viewpoint__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "total_viewpoints": Viewpoint.objects.filter(
                project=project, status="pending"
            ).count(),
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def goal_contributions(request, project_id):
    indexhead = "Goals Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    goals = Goal.objects.filter(project=project, status="pending").order_by("id")
    paginator = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginator.get_page(page_number)

    comments = GoalComment.objects.filter(
        goal__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)
    return render(
        request,
        "projects/my_projects/goal_contributions.html",
        {
            "goals": goals,
            "total_goals": Goal.objects.filter(
                project=project, status="pending"
            ).count(),
            "project": project,
            "project_id": project.id,
            "goal_comments": comments,
            "total_comments": GoalComment.objects.filter(
                goal__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def requirement_contributions(request, project_id):
    indexhead = "Requirement Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    requirements = Requirement.objects.filter(
        project=project, status="pending"
    ).order_by("id")
    paginator = Paginator(requirements, 10)
    page_number = request.GET.get("page")
    requirements = paginator.get_page(page_number)

    comments = RequirementComment.objects.filter(
        requirement__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)
    return render(
        request,
        "projects/my_projects/requirement_contributions.html",
        {
            "requirements": requirements,
            "total_requirements": Requirement.objects.filter(
                project=project, status="pending"
            ).count(),
            "project": project,
            "project_id": project.id,
            "requirement_comments": comments,
            "total_comments": RequirementComment.objects.filter(
                requirement__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def scenario_contributions(request, project_id):
    indexhead = "Scenario Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    scenarios = RequirementScenario.objects.filter(
        requirement__project=project, scenario__status="pending"
    ).order_by("id")
    paginator = Paginator(scenarios, 10)
    page_number = request.GET.get("page")
    scenarios = paginator.get_page(page_number)

    comments = ScenarioComment.objects.filter(
        scenario__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)
    return render(
        request,
        "projects/my_projects/scenerio_contributions.html",
        {
            "scenarios": scenarios,
            "total_scenarios": RequirementScenario.objects.filter(
                requirement__project=project, scenario__status="pending"
            ).count(),
            "project": project,
            "project_id": project.id,
            "scenario_comments": comments,
            "total_comments": ScenarioComment.objects.filter(
                scenario__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def process_contributions(request, project_id):
    indexhead = "Process Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    processes = RequirementProcess.objects.filter(
        requirement__project=project, process__status="pending"
    ).order_by("id")
    paginator = Paginator(processes, 10)
    page_number = request.GET.get("page")
    processes = paginator.get_page(page_number)

    comments = ProcessComment.objects.filter(
        process__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)
    return render(
        request,
        "projects/my_projects/process_contributios.html",
        {
            "processes": processes,
            "total_processes": RequirementProcess.objects.filter(
                requirement__project=project, process__status="pending"
            ).count(),
            "project": project,
            "project_id": project.id,
            "process_comments": comments,
            "total_comments": ProcessComment.objects.filter(
                process__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


@login_required(login_url="login")
def usecase_contributions(request, project_id):
    indexhead = "Use Case Contribution Requests"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    usecases = RequirementUsecase.objects.filter(
        requirement__project=project, usecase__status="pending"
    ).order_by("id")
    paginator = Paginator(usecases, 10)
    page_number = request.GET.get("page")
    usecases = paginator.get_page(page_number)

    comments = UseCaseComment.objects.filter(
        usecase__project=project, comment__status="pending"
    ).order_by("id")
    paginate = Paginator(comments, 10)
    comment_page_number = request.GET.get("page")
    comments = paginate.get_page(comment_page_number)
    return render(
        request,
        "projects/my_projects/usecase_contributions.html",
        {
            "usecases": usecases,
            "total_usecases": RequirementUsecase.objects.filter(
                requirement__project=project, usecase__status="pending"
            ).count(),
            "project": project,
            "project_id": project.id,
            "usecase_comments": comments,
            "total_comments": UseCaseComment.objects.filter(
                usecase__project=project, comment__status="pending"
            ).count(),
            "member": member,
            "notification": notification(request),
            "total_notification": total_notification(request),
            "hidesearch": hidesearch,
            "indexhead": indexhead,
        },
    )


#  Approving contributions


@login_required(login_url="login")
def approve_viewpoint(request, viewpoint_id):
    if request.method == "POST":
        viewpoint_ids = request.getlist("viewpoint_id")
        for viewpoint_new_id in viewpoint_ids:
            viewpoint = Viewpoint.objects.get(id=viewpoint_new_id)
            update_viewpoint = Viewpoint.objects.filter(id=viewpoint_new_id).update(
                status="accepted"
            )
        return redirect(
            "projects:viewpointcontributions", project_id=viewpoint.project.id
        )

    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    approve = Viewpoint.objects.filter(id=viewpoint_id).update(status="accepted")
    return redirect("projects:viewpointcontributions", project_id=viewpoint.project.id)


# bulk approval


def bulk_approve_viewpoint(request):

    if "approve" in request.POST:
        viewpoints_id = request.POST.getlist("viewpoint")
        for viewpoint_id in viewpoints_id:
            update_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(
                status="accepted"
            )
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        viewpoints_id = request.POST.getlist("viewpoint")
        for viewpoint_id in viewpoints_id:
            update_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(
                status="rejected"
            )
        return redirect(request.META["HTTP_REFERER"])


def bulk_approve_goal(request):

    if "approve" in request.POST:
        goals_id = request.POST.getlist("goal")
        for goal_id in goals_id:
            update_goal = Goal.objects.filter(id=goal_id).update(status="accepted")
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        goals_id = request.POST.getlist("goal")
        for goal_id in goals_id:
            update_goal = Goal.objects.filter(id=goal_id).update(status="rejected")
        return redirect(request.META["HTTP_REFERER"])


def bulk_approve_requirement(request):

    if "approve" in request.POST:
        requirements_id = request.POST.getlist("requirement")
        for requirement_id in requirements_id:
            update = Requirement.objects.filter(id=requirement_id).update(
                status="accepted"
            )
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        requirements_id = request.POST.getlist("requirement")
        for requirement_id in requirements_id:
            update = Requirement.objects.filter(id=requirement_id).update(
                status="rejected"
            )
        return redirect(request.META["HTTP_REFERER"])


def bulk_approve_scenario(request):

    if "approve" in request.POST:
        scenarios_id = request.POST.getlist("scenario")
        for scenario_id in scenarios_id:
            update = Scenario.objects.filter(id=scenario_id).update(status="accepted")
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        scenarios_id = request.POST.getlist("scenario")
        for scenario_id in scenarios_id:
            update = Scenario.objects.filter(id=scenario_id).update(status="rejected")
        return redirect(request.META["HTTP_REFERER"])


def bulk_approve_process(request):

    if "approve" in request.POST:
        processes_id = request.POST.getlist("process")
        for process_id in processes_id:
            update = Process.objects.filter(id=process_id).update(status="accepted")
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        processes_id = request.POST.getlist("process")
        for process_id in processes_id:
            update = Process.objects.filter(id=process_id).update(status="rejected")
        return redirect(request.META["HTTP_REFERER"])


def bulk_approve_usecase(request):

    if "approve" in request.POST:
        usecases_id = request.POST.getlist("usecase")
        for usecase_id in usecases_id:
            update = UseCase.objects.filter(id=usecase_id).update(status="accepted")
        return redirect(request.META["HTTP_REFERER"])

    if "reject" in request.POST:
        usecases_id = request.POST.getlist("usecase")
        for usecase_id in usecases_id:
            update = UseCase.objects.filter(id=usecase_id).update(status="rejected")
        return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def approve_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    approve_goal = Goal.objects.filter(id=goal_id).update(status="accepted")
    return redirect("projects:goalcontributions", project_id=goal.project.id)


@login_required(login_url="login")
def approve_requirement(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    approve_requirement = Requirement.objects.filter(id=requirement_id).update(
        status="accepted"
    )
    return redirect(
        "projects:requirementcontributions", project_id=requirement.project.id
    )


@login_required(login_url="login")
def approve_scenario(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    approve_scenario = Scenario.objects.filter(id=scenario_id).update(status="accepted")
    return redirect("projects:scenariocontributions", project_id=scenario.project.id)


@login_required(login_url="login")
def approve_process(request, process_id):
    process = Process.objects.get(id=process_id)
    approve_process = Process.objects.filter(id=process_id).update(status="accepted")
    return redirect("projects:processcontributions", project_id=process.project.id)


@login_required(login_url="login")
def approve_usecase(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    approve_usecase = UseCase.objects.filter(id=usecase_id).update(status="accepted")
    return redirect("projects:usecasecontributions", project_id=usecase.project.id)


@login_required(login_url="login")
def approve_project_comment(request, comment_id):
    project_comment = ProjectComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:projectcontributions", project_id=project_comment.project.id
    )


def bulk_approve_project_comments(request):
    comments_id = request.POST.getlist("comment")
    if "approve" in request.POST:
        for comment_id in comments_id:
            approve_comment = Comment.objects.filter(id=comment_id).update(
                status="accepted"
            )
        return redirect(request.META["HTTP_REFERER"])
    if "reject" in request.POST:
        for comment_id in comments_id:
            reject_comment = Comment.objects.filter(id=comment_id).update(
                status="rejected"
            )
        return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def approve_viewpoint_comment(request, comment_id):
    viewpoint_comment = ViewPointComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:viewpointcontributions",
        project_id=viewpoint_comment.viewpoint.project.id,
    )


@login_required(login_url="login")
def approve_goal_comment(request, comment_id):
    goal_comment = GoalComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:goalcontributions", project_id=goal_comment.goal.project.id
    )


@login_required(login_url="login")
def approve_requirement_comment(request, comment_id):
    requirement_comment = RequirementComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:requirementcontributions",
        project_id=requirement_comment.requirement.project.id,
    )


@login_required(login_url="login")
def approve_scenario_comment(request, comment_id):
    scenario_comment = ScenarioComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:scenariocontributions",
        project_id=scenario_comment.scenario.project.id,
    )


@login_required(login_url="login")
def approve_process_comment(request, comment_id):
    process_comment = ProcessComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:processcontributions", project_id=process_comment.process.project.id
    )


@login_required(login_url="login")
def approve_usecase_comment(request, comment_id):
    usecase_comment = UseCaseComment.objects.get(comment__id=comment_id)
    approve_comment = Comment.objects.filter(id=comment_id).update(status="accepted")
    return redirect(
        "projects:usecasecontributions", project_id=usecase_comment.usecase.project.id
    )


# Rejecting contributions
@login_required(login_url="login")
def reject_viewpoint(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    reject_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(
        status="rejected"
    )
    return redirect("projects:viewpointcontributions", project_id=viewpoint.project.id)


@login_required(login_url="login")
def reject_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    reject_goal = Goal.objects.filter(id=goal_id).update(status="rejected")
    return redirect("projects:goalcontributions", project_id=goal.project.id)


@login_required(login_url="login")
def reject_requirement(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    reject_requirement = Requirement.objects.filter(id=requirement_id).update(
        status="rejected"
    )
    return redirect(
        "projects:requirementcontributions", project_id=requirement.project.id
    )


@login_required(login_url="login")
def reject_scenario(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    reject_scenario = Scenario.objects.filter(id=scenario_id).update(status="rejected")
    return redirect("projects:scenariocontributions", project_id=scenario.project.id)


@login_required(login_url="login")
def reject_process(request, process_id):
    process = Process.objects.get(id=process_id)
    reject_process = Process.objects.filter(id=process_id).update(status="rejected")
    return redirect("projects:processcontributions", project_id=process.project.id)


@login_required(login_url="login")
def reject_usecase(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    reject_usecase = UseCase.objects.filter(id=usecase_id).update(status="rejected")
    return redirect("projects:usecasecontributions", project_id=usecase.project.id)


@login_required(login_url="login")
def reject_project_comment(request, comment_id):
    project_comment = ProjectComment.objects.get(comment__id=comment_id)
    reject_comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:projectcontributions", project_id=project_comment.project.id
    )


@login_required(login_url="login")
def reject_viewpoint_comment(request, comment_id):
    viewpoint_comment = ViewPointComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:viewpointcontributions",
        project_id=viewpoint_comment.viewpoint.project.id,
    )


@login_required(login_url="login")
def reject_goal_comment(request, comment_id):
    goal_comment = GoalComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:goalcontributions", project_id=goal_comment.goal.project.id
    )


@login_required(login_url="login")
def reject_requirement_comment(request, comment_id):
    requirement_comment = RequirementComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:requirementcontributions",
        project_id=requirement_comment.requirement.project.id,
    )


@login_required(login_url="login")
def reject_scenario_comment(request, comment_id):
    scenario_comment = ScenarioComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:scenariocontributions",
        project_id=scenario_comment.scenario.project.id,
    )


@login_required(login_url="login")
def reject_process_comment(request, comment_id):
    process_comment = ProcessComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:processcontributions", project_id=process_comment.process.project.id
    )


@login_required(login_url="login")
def reject_usecase_comment(request, comment_id):
    usecase_comment = UseCaseComment.objects.get(comment__id=comment_id)
    comment = Comment.objects.filter(id=comment_id).update(status="rejected")
    return redirect(
        "projects:usecasecontributions", project_id=usecase_comment.usecase.project.id
    )


# Block contributions
@login_required(login_url="login")
def block_viewpoint(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    block_viewpoint = Viewpoint.objects.filter(id=viewpoint_id).update(status="blocked")
    return redirect("projects:projectcontributions", project_id=viewpoint.project.id)


@login_required(login_url="login")
def block_goal(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    block_goal = Goal.objects.filter(id=goal_id).update(status="blocked")
    return redirect("projects:projectcontributions", project_id=goal.project.id)


@login_required(login_url="login")
def block_requirement(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    block_requirement = Requirement.objects.filter(id=requirement_id).update(
        status="blocked"
    )
    return redirect("projects:projectcontributions", project_id=requirement.project.id)


@login_required(login_url="login")
def block_scenario(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    block_scenario = Scenario.objects.filter(id=scenario_id).update(status="blocked")
    return redirect("projects:projectcontributions", project_id=scenario.project.id)


@login_required(login_url="login")
def block_process(request, process_id):
    process = Process.objects.get(id=process_id)
    block_process = Process.objects.filter(id=process_id).update(status="blocked")
    return redirect("projects:projectcontributions", project_id=process.project.id)


@login_required(login_url="login")
def block_usecase(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    block_usecase = UseCase.objects.filter(id=usecase_id).update(status="blocked")
    return redirect("projects:projectcontributions", project_id=usecase.project.id)


# decomose goals
@login_required(login_url="login")
def decompose_goal(request):
    original_goal_id = request.POST.get("original_goal")
    original_goal = Goal.objects.get(id=original_goal_id)
    decomposition_operator = request.POST.get("operator")
    decompose_to_goals = request.POST.getlist("decomposed_goal")
    for goal in decompose_to_goals:
        goal_decomposition = GoalDecomposition.objects.create(
            original_goal=original_goal,
            decomposition_operator=decomposition_operator,
            decomposed_goal=goal,
        )
        goal_decomposition.save()
    return redirect(request.META["HTTP_REFERER"])


# relate goals
@login_required(login_url="login")
def relate_goal(request):
    original_goal_id = request.POST.get("original_goal")
    original_goal = Goal.objects.get(id=original_goal_id)
    relationship_type = request.POST.get("relationship_type")
    relate_to = request.POST.getlist("related_goal")
    for goal in relate_to:
        relate_goal = GoalRelationship.objects.create(
            origin_goal=original_goal,
            relation_type=relationship_type,
            related_goal=int(goal),
        )
        relate_goal.save()
    return redirect(request.META["HTTP_REFERER"])


def related_goals(request, goal_id):
    member = Member.objects.get(user=request.user)
    hidesearch = "hide"
    type_ = "Related"
    indexhead = "Related Goals"
    original_goal = Goal.objects.get(id=goal_id)
    if request.POST.get("operator"):
        related_goals_id = GoalRelationship.objects.filter(
            relation_type=request.POST.get("operator"), origin_goal=original_goal
        )
    else:
        related_goals_id = GoalRelationship.objects.filter(origin_goal=original_goal)
    goal_ids = []
    for goal_id in related_goals_id:
        goal_ids.append(goal_id.related_goal)

    goals = (
        ViewpointGoal.objects.filter(goal__id__in=goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginate.get_page(page_number)
    return render(
        request,
        "projects/Goals/decomposed_and_related_goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "type": type_,
            "member": member,
            "goal": original_goal,
            "goal_id": original_goal.id,
            "hidesearch": hidesearch,
            "project": original_goal.project,
            "project_id": original_goal.project.id,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def decomposed_goals(request, goal_id):
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    type_ = "Decomposed"
    indexhead = "Decomposed Goals"
    original_goal = Goal.objects.get(id=goal_id)
    if request.POST.get("operator"):
        related_goals_id = GoalDecomposition.objects.filter(
            decomposition_operator=request.POST.get("operator"),
            original_goal=original_goal,
        )
    else:

        related_goals_id = GoalDecomposition.objects.filter(original_goal=original_goal)
    goal_ids = []
    for goal_id in related_goals_id:
        goal_ids.append(goal_id.decomposed_goal)

    goals = (
        ViewpointGoal.objects.filter(goal__id__in=goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(goals, 10)
    page_number = request.GET.get("page")
    goals = paginate.get_page(page_number)
    return render(
        request,
        "projects/Goals/decomposed_and_related_goals.html",
        {
            "indexhead": indexhead,
            "goals": goals,
            "goal": original_goal,
            "type": type_,
            "member": member,
            "goal_id": original_goal.id,
            "hidesearch": hidesearch,
            "project": original_goal.project,
            "project_id": original_goal.project.id,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def associate_viewpoints(request, goal_id):
    indexhead = "Associated Viewpoints"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    goal = Goal.objects.get(id=goal_id)
    print(goal.id)
    viewpoints = ViewpointGoal.objects.filter(goal=goal)
    print(viewpoints)
    viewpoint_ids = []
    for viewpoint in viewpoints:
        viewpoint_ids.append(viewpoint.viewpoint.id)
    print(viewpoint_ids)
    viewpoints = Viewpoint.objects.filter(id__in=viewpoint_ids).order_by("id")
    paginator = Paginator(viewpoints, 6)
    pagenumber = request.GET.get("page")
    viewpoints = paginator.get_page(pagenumber)
    return render(
        request,
        "projects/viewpoints/viewpoints.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "viewpoints": viewpoints,
            "project_id": goal.project.id,
            "member": member,
            "goal_id": goal_id,
            "project": goal.project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def scenario_requirement(request, scenario_id):
    indexhead = "Scenario Associated Requirements"
    hidesearch = 1
    scenario = Scenario.objects.get(id=scenario_id)
    requirements = (
        RequirementScenario.objects.filter(scenario=scenario)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    requirement_list = []
    for requirement in requirements:
        requirement_list.append(requirement.requirement)

    requirements = (
        RequirementGoal.objects.filter(requirement__in=requirement_list)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    project = Project.objects.get(id=scenario.project.id)
    member = Member.objects.get(user=request.user)
    paginator = Paginator(requirements, 10)
    pagenumber = request.GET.get("page")
    requirements = paginator.get_page(pagenumber)
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project_id": project.id,
            "requirements": requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def process_requirements(request, process_id):
    indexhead = "Process Associated Requirements"
    hidesearch = 1
    process = Process.objects.get(id=process_id)
    requirements = (
        RequirementProcess.objects.filter(process=process)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    project = Project.objects.get(id=process.project.id)
    requirement_list = []
    for requirement in requirements:
        requirement_list.append(requirement.requirement)

    requirements = (
        RequirementGoal.objects.filter(requirement__in=requirement_list)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    member = Member.objects.get(user=request.user)
    paginate = Paginator(requirements, 10)
    page_number = request.GET.get("page")
    requiremenrs = paginate.get_page(page_number)
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project_id": project.id,
            "requirements": requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def usecase_requirements(request, usecase_id):
    indexhead = "Use case Associated Requirements"
    hidesearch = 1
    usecase = UseCase.objects.get(id=usecase_id)
    requirements = (
        RequirementUsecase.objects.filter(usecase=usecase)
        .order_by("-usecase__id")
        .distinct("usecase__id")
    )
    project = Project.objects.get(id=usecase.project.id)
    requirement_list = []
    for requirement in requirements:
        requirement_list.append(requirement.requirement)

    requirements = (
        RequirementGoal.objects.filter(requirement__in=requirement_list)
        .order_by("requirement__id")
        .distinct("requirement__id")
    )
    member = Member.objects.get(user=request.user)
    paginate = Paginator(requirements, 10)
    page_number = request.GET.get("page")
    requirements = paginate.get_page(page_number)
    return render(
        request,
        "projects/requirements/requirements.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project_id": project.id,
            "requirements": requirements,
            "member": member,
            "project": project,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def add_stakeholder(request, project_id):
    project = Project.objects.get(id=project_id)
    stakeholder = request.POST.get("stakeholder")
    member = Member.objects.get(user=request.user)
    create_stakeholder = Stakeholder.objects.create(
        project=project, name=stakeholder, created_by=member
    )
    create_stakeholder.save()
    return redirect(request.META["HTTP_REFERER"])


def delete_stakeholder(request, stakeholder_id):
    Stakeholder.objects.filter(id=stakeholder_id).delete()
    return redirect(request.META["HTTP_REFERER"])


@login_required(login_url="login")
def like(request, module_id=None):
    # module_id stand for ids from project to usecase ids
    # index is identifier of modules
    context = list()
    info = list()
    index = int(request.GET.get("index"))
    print(index)
    # for project like
    if index == 0:
        project = Project.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ProjectLike.objects.filter(
            project=project, like__liked_by=member
        ).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                project_like = ProjectLike.objects.create(like=like, project=project)
                project_like.save()

                if project_like:
                    if ProjectDislike.objects.filter(
                        project=project, dislike__disliked_by=member
                    ).exists():
                        ProjectDislike.objects.filter(
                            project=project, dislike__disliked_by=member
                        ).delete()
                    total_likes = ProjectLike.objects.filter(project=project).count()
                    total_dislikes = ProjectDislike.objects.filter(
                        project=project
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = ProjectLike.objects.filter(project=project).count()
                    total_dislikes = ProjectDislike.objects.filter(
                        project=project
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ProjectLike.objects.filter(project=project).count()
                total_dislikes = ProjectDislike.objects.filter(project=project).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = ProjectLike.objects.filter(
                project=project, like__liked_by=member
            ).delete()
            total_likes = ProjectLike.objects.filter(project=project).count()
            total_dislikes = ProjectDislike.objects.filter(project=project).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }

    #  for viewpoint like
    elif index == 1:
        viewpoint = Viewpoint.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ViewpointLike.objects.filter(
            viewpoint=viewpoint, like__liked_by=member
        ).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                viewpoint_like = ViewpointLike.objects.create(
                    like=like, viewpoint=viewpoint
                )
                viewpoint_like.save()
                if ViewpointDislike.objects.filter(
                    viewpoint=viewpoint, dislike__disliked_by=member
                ).exists():
                    ViewpointDislike.objects.filter(
                        viewpoint=viewpoint, dislike__disliked_by=member
                    ).delete()
                if viewpoint_like:
                    total_likes = ViewpointLike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    total_dislikes = ViewpointDislike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = ViewpointLike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    total_dislikes = ViewpointDislike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ViewpointLike.objects.filter(viewpoint=viewpoint).count()
                total_dislikes = ViewpointDislike.objects.filter(
                    viewpoint=viewpoint
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = ViewpointLike.objects.filter(
                viewpoint=viewpoint, like__liked_by=member
            ).delete()
            total_likes = ViewpointLike.objects.filter(viewpoint=viewpoint).count()
            total_dislikes = ViewpointDislike.objects.filter(
                viewpoint=viewpoint
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }
    # for goal like
    elif index == 2:
        goal = Goal.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not GoalLike.objects.filter(goal=goal, like__liked_by=member).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                goal_like = GoalLike.objects.create(like=like, goal=goal)
                goal_like.save()
                if GoalDislike.objects.filter(
                    goal=goal, dislike__disliked_by=member
                ).exists():
                    GoalDislike.objects.filter(
                        goal=goal, dislike__disliked_by=member
                    ).delete()
                if goal_like:
                    total_likes = GoalLike.objects.filter(goal=goal).count()
                    total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = GoalLike.objects.filter(goal=goal).count()
                    total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = GoalLike.objects.filter(goal=goal).count()
                total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = GoalLike.objects.filter(goal=goal, like__liked_by=member).delete()
            total_likes = GoalLike.objects.filter(goal=goal).count()
            total_dislikes = GoalDislike.objects.filter(goal=goal).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }
    # for requirement like
    elif index == 3:
        requirement = Requirement.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

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
                if RequirementDislike.objects.filter(
                    requirement=requirement, dislike__disliked_by=member
                ).exists():
                    RequirementDislike.objects.filter(
                        requirement=requirement, dislike__disliked_by=member
                    ).delete()
                if requirement_like:
                    total_likes = RequirementLike.objects.filter(
                        requirement=requirement
                    ).count()
                    total_dislikes = RequirementDislike.objects.filter(
                        requirement=requirement
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = RequirementLike.objects.filter(
                        requirement=requirement
                    ).count()
                    total_dislikes = RequirementDislike.objects.filter(
                        requirement=requirement
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = RequirementLike.objects.filter(
                    requirement=requirement
                ).count()
                total_dislikes = RequirementDislike.objects.filter(
                    requirement=requirement
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = RequirementLike.objects.filter(
                requirement=requirement, like__liked_by=member
            ).delete()
            total_likes = RequirementLike.objects.filter(
                requirement=requirement
            ).count()
            total_dislikes = RequirementDislike.objects.filter(
                requirement=requirement
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }

    #    for scenario like
    elif index == 4:
        scenario = RequirementScenario.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ScenarioLike.objects.filter(
            scenario=scenario.scenario, like__liked_by=member
        ).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                scenario_like = ScenarioLike.objects.create(
                    like=like, scenario=scenario.scenario
                )
                scenario_like.save()
                if ScenarioDislike.objects.filter(
                    scenario=scenario.scenario, dislike__disliked_by=member
                ).exists():
                    ScenarioDislike.objects.filter(
                        scenario=scenario.scenario, dislike__disliked_by=member
                    ).delete()
                if scenario_like:
                    total_likes = ScenarioLike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    total_dislikes = ScenarioDislike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = ScenarioLike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    total_dislikes = ScenarioDislike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }

            else:
                total_likes = ScenarioLike.objects.filter(
                    scenario=scenario.scenario
                ).count()
                total_dislikes = ScenarioDislike.objects.filter(
                    scenario=scenario.scenario
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:

            unlike = ScenarioLike.objects.filter(
                scenario=scenario.scenario, like__liked_by=member
            ).delete()
            total_likes = ScenarioLike.objects.filter(
                scenario=scenario.scenario
            ).count()
            total_dislikes = ScenarioDislike.objects.filter(
                scenario=scenario.scenario
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }

    #  for process like
    elif index == 5:
        process = RequirementProcess.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ProcessLike.objects.filter(
            process=process.process, like__liked_by=member
        ).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                process_like = ProcessLike.objects.create(
                    like=like, process=process.process
                )
                process_like.save()
                if ProcessDislike.objects.filter(
                    process=process.process, dislike__disliked_by=member
                ).exists():
                    ProcessDislike.objects.filter(
                        process=process.process, dislike__disliked_by=member
                    ).delete()
                if process_like:
                    total_likes = ProcessLike.objects.filter(
                        process=process.process
                    ).count()
                    total_dislikes = ProcessDislike.objects.filter(
                        process=process.process
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = ProcessLike.objects.filter(
                        process=process.process
                    ).count()
                    total_dislikes = ProcessDislike.objects.filter(
                        process=process.process
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ProcessLike.objects.filter(
                    process=process.process
                ).count()
                total_dislikes = ProcessDislike.objects.filter(
                    process=process.process
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = ProcessLike.objects.filter(
                process=process.process, like__liked_by=member
            ).delete()
            total_likes = ProcessLike.objects.filter(process=process.process).count()
            total_dislikes = ProcessDislike.objects.filter(
                process=process.process
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }

    #  for usecase like
    elif index == 6:
        usecase = RequirementUsecase.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not UseCaseLike.objects.filter(
            use_case=usecase.usecase, like__liked_by=member
        ).exists():
            like = Like.objects.create(like=True, liked_by=member)
            like.save()
            if like:
                # then creating project_like
                usecase_like = UseCaseLike.objects.create(
                    like=like, use_case=usecase.usecase
                )
                usecase_like.save()
                if UseCaseDislike.objects.filter(
                    use_case=usecase.usecase, dislike__disliked_by=member
                ).exists():
                    UseCaseDislike.objects.filter(
                        use_case=usecase.usecase, dislike__disliked_by=member
                    ).delete()
                if usecase_like:
                    total_likes = UseCaseLike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    total_dislikes = UseCaseDislike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly liked!",
                    }
                else:
                    total_likes = UseCaseLike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    total_dislikes = UseCaseDislike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to like!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = UseCaseLike.objects.filter(
                    use_case=usecase.usecase
                ).count()
                total_dislikes = UseCaseDislike.objects.filter(
                    use_case=usecase.usecase
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your like!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            unlike = UseCaseLike.objects.filter(
                use_case=usecase.usecase, like__liked_by=member
            ).delete()
            total_likes = UseCaseLike.objects.filter(use_case=usecase.usecase).count()
            total_dislikes = UseCaseDislike.objects.filter(
                use_case=usecase.usecase
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly unliked!",
            }
    context.append(info)
    return JsonResponse(context, safe=False)


# general dislikes
@login_required(login_url="login")
def dislike(request, module_id=None):
    # module_id stand for ids from project to usecase ids
    # index is identifier of modules
    index = int(request.GET.get("index"))
    # for project like
    if index == 0:
        project = Project.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

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
                    if ProjectLike.objects.filter(
                        project=project, like__liked_by=member
                    ).exists():
                        ProjectLike.objects.filter(
                            project=project, like__liked_by=member
                        ).delete()
                    total_likes = ProjectLike.objects.filter(project=project).count()
                    total_dislikes = ProjectDislike.objects.filter(
                        project=project
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = ProjectLike.objects.filter(project=project).count()
                    total_dislikes = ProjectDislike.objects.filter(
                        project=project
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ProjectLike.objects.filter(project=project).count()
                total_dislikes = ProjectDislike.objects.filter(project=project).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            undislike = ProjectDislike.objects.filter(
                project=project, dislike__disliked_by=member
            ).delete()
            total_likes = ProjectLike.objects.filter(project=project).count()
            total_dislikes = ProjectDislike.objects.filter(project=project).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }

    #  for viewpoint like
    elif index == 1:
        viewpoint = Viewpoint.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ViewpointDislike.objects.filter(
            viewpoint=viewpoint, dislike__disliked_by=member
        ).exists():
            dislike = Dislike.objects.create(dislike=True, disliked_by=member)
            dislike.save()
            if dislike:
                # then creating project_like
                viewpoint_dislike = ViewpointDislike.objects.create(
                    dislike=dislike, viewpoint=viewpoint
                )
                viewpoint_dislike.save()
                if ViewpointLike.objects.filter(
                    viewpoint=viewpoint, like__liked_by=member
                ).exists():
                    ViewpointLike.objects.filter(
                        viewpoint=viewpoint, like__liked_by=member
                    ).delete()
                if viewpoint_dislike:
                    total_likes = ViewpointLike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    total_dislikes = ViewpointDislike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = ViewpointLike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    total_dislikes = ViewpointDislike.objects.filter(
                        viewpoint=viewpoint
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ViewpointLike.objects.filter(viewpoint=viewpoint).count()
                total_dislikes = ViewpointDislike.objects.filter(
                    viewpoint=viewpoint
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            undislike = ViewpointDislike.objects.filter(
                viewpoint=viewpoint, dislike__disliked_by=member
            ).delete()
            total_likes = ViewpointLike.objects.filter(viewpoint=viewpoint).count()
            total_dislikes = ViewpointDislike.objects.filter(
                viewpoint=viewpoint
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }
    # for goal like
    elif index == 2:
        goal = Goal.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not GoalDislike.objects.filter(
            goal=goal, dislike__disliked_by=member
        ).exists():
            dislike = Dislike.objects.create(dislike=True, disliked_by=member)
            dislike.save()
            if dislike:
                # then creating project_like
                goal_dislike = GoalDislike.objects.create(dislike=dislike, goal=goal)
                goal_dislike.save()
                if GoalLike.objects.filter(goal=goal, like__liked_by=member).exists():
                    GoalLike.objects.filter(goal=goal, like__liked_by=member).delete()
                if goal_dislike:
                    total_likes = GoalLike.objects.filter(goal=goal).count()
                    total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = GoalLike.objects.filter(goal=goal).count()
                    total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = GoalLike.objects.filter(goal=goal).count()
                total_dislikes = GoalDislike.objects.filter(goal=goal).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            undislike = GoalDislike.objects.filter(
                goal=goal, dislike__disliked_by=member
            ).delete()
            total_likes = GoalLike.objects.filter(goal=goal).count()
            total_dislikes = GoalDislike.objects.filter(goal=goal).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }

    # for requirement like
    elif index == 3:
        requirement = Requirement.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

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
                if RequirementLike.objects.filter(
                    requirement=requirement, like__liked_by=member
                ).exists():
                    RequirementLike.objects.filter(
                        requirement=requirement, like__liked_by=member
                    ).delete()
                if requirement_dislike:
                    total_likes = RequirementLike.objects.filter(
                        requirement=requirement
                    ).count()
                    total_dislikes = RequirementDislike.objects.filter(
                        requirement=requirement
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = RequirementLike.objects.filter(
                        requirement=requirement
                    ).count()
                    total_dislikes = RequirementDislike.objects.filter(
                        requirement=requirement
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = RequirementLike.objects.filter(
                    requirement=requirement
                ).count()
                total_dislikes = RequirementDislike.objects.filter(
                    requirement=requirement
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            undislike = RequirementDislike.objects.filter(
                requirement=requirement, dislike__disliked_by=member
            ).delete()

            total_likes = RequirementLike.objects.filter(
                requirement=requirement
            ).count()
            total_dislikes = RequirementDislike.objects.filter(
                requirement=requirement
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }

    #    for scenario like
    elif index == 4:
        scenario = RequirementScenario.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

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
                if ScenarioLike.objects.filter(
                    scenario=scenario.scenario, like__liked_by=member
                ).exists():
                    ScenarioLike.objects.filter(
                        scenario=scenario.scenario, like__liked_by=member
                    ).delete()
                if scenario_dislike:
                    total_likes = ScenarioLike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    total_dislikes = ScenarioDislike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = ScenarioLike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    total_dislikes = ScenarioDislike.objects.filter(
                        scenario=scenario.scenario
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }

            else:
                total_likes = ScenarioLike.objects.filter(
                    scenario=scenario.scenario
                ).count()
                total_dislikes = ScenarioDislike.objects.filter(
                    scenario=scenario.scenario
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:

            undislike = ScenarioDislike.objects.filter(
                scenario=scenario.scenario, dislike__disliked_by=member
            ).delete()
            total_likes = ScenarioLike.objects.filter(
                scenario=scenario.scenario
            ).count()
            total_dislikes = ScenarioDislike.objects.filter(
                scenario=scenario.scenario
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }

    #  for process like
    elif index == 5:
        process = RequirementProcess.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not ProcessDislike.objects.filter(
            process=process.process, dislike__disliked_by=member
        ).exists():
            dislike = Dislike.objects.create(dislike=True, disliked_by=member)
            dislike.save()
            if dislike:
                # then creating project_like
                process_dislike = ProcessDislike.objects.create(
                    dislike=dislike, process=process.process
                )
                process_dislike.save()
                if ProcessLike.objects.filter(
                    process=process.process, like__liked_by=member
                ).exists():
                    ProcessLike.objects.filter(
                        process=process.process, like__liked_by=member
                    ).delete()
                if process_dislike:
                    total_likes = ProcessLike.objects.filter(
                        process=process.process
                    ).count()
                    total_dislikes = ProcessDislike.objects.filter(
                        process=process.process
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = ProcessLike.objects.filter(
                        process=process.process
                    ).count()
                    total_dislikes = ProcessDislike.objects.filter(
                        process=process.process
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = ProcessLike.objects.filter(
                    process=process.process
                ).count()
                total_dislikes = ProcessDislike.objects.filter(
                    process=process.process
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # return redirect("projects:viewmyproject", project_id=project_id)
            undislike = ProcessDislike.objects.filter(
                process=process.process, dislike__disliked_by=member
            ).delete()
            total_likes = ProcessLike.objects.filter(process=process.process).count()
            total_dislikes = ProcessDislike.objects.filter(
                process=process.process
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }

    #  for usecase like
    elif index == 6:
        usecase = RequirementUsecase.objects.get(id=module_id)
        member = Member.objects.get(user=request.user)
        context = list()

        if not UseCaseDislike.objects.filter(
            use_case=usecase.usecase, dislike__disliked_by=member
        ).exists():
            dislike = Dislike.objects.create(dislike=True, disliked_by=member)
            dislike.save()
            if dislike:
                # then creating project_like
                usecase_dislike = UseCaseDislike.objects.create(
                    dislike=dislike, use_case=usecase.usecase
                )
                usecase_dislike.save()
                if UseCaseLike.objects.filter(
                    use_case=usecase.usecase, like__liked_by=member
                ).exists():
                    UseCaseLike.objects.filter(
                        use_case=usecase.usecase, like__liked_by=member
                    ).delete()
                if usecase_dislike:
                    total_likes = UseCaseLike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    total_dislikes = UseCaseDislike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    info = {
                        "status": True,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Successfuly disliked!",
                    }
                else:
                    total_likes = UseCaseLike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    total_dislikes = UseCaseDislike.objects.filter(
                        use_case=usecase.usecase
                    ).count()
                    info = {
                        "status": False,
                        "total_likes": total_likes,
                        "total_dislikes": total_dislikes,
                        "message": "Failed to dislike!",
                    }
                    # return True
                # return redirect("projects:viewmyproject", project_id=project_id)
            else:
                total_likes = UseCaseLike.objects.filter(
                    use_case=usecase.usecase
                ).count()
                total_dislikes = UseCaseDislike.objects.filter(
                    use_case=usecase.usecase
                ).count()
                info = {
                    "status": False,
                    "total_likes": total_likes,
                    "total_dislikes": total_dislikes,
                    "message": "Failed to update your dislike!",
                }
        else:
            # removing one side dislike if there is existing like
            undislike = UseCaseDislike.objects.filter(
                use_case=usecase.usecase, dislike__disliked_by=member
            ).delete()
            total_likes = UseCaseLike.objects.filter(use_case=usecase.usecase).count()
            total_dislikes = UseCaseDislike.objects.filter(
                use_case=usecase.usecase
            ).count()
            info = {
                "status": True,
                "total_likes": total_likes,
                "total_dislikes": total_dislikes,
                "message": "Successfuly undisliked!",
            }
    context.append(info)
    return JsonResponse(context, safe=False)


# updating stakeholder
def update_stakeholder(request, stakeholder_id):
    stakeholder = request.POST.get("stakeholder")
    update_stakeholder_names = Stakeholder.objects.filter(id=stakeholder_id).update(
        name=stakeholder
    )
    return redirect(request.META["HTTP_REFERER"])


def scenario_process(request, scenario_id):
    indexhead = "Associated Scenario Processes"
    scenario = Scenario.objects.get(id=scenario_id)
    processes = (
        ScenarioProcess.objects.filter(scenario=scenario)
        .order_by("process__id")
        .distinct("process__id")
    )
    process_list = []
    for process_ in processes:
        process_list.append(process_.process)
    processes = (
        RequirementProcess.objects.filter(process__in=process_list)
        .order_by("process__id")
        .distinct("process__id")
    )
    project = Project.objects.get(id=scenario.project.id)
    paginate = Paginator(processes, 10)
    page_number = request.GET.get("page")
    processes = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "processes": processes,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def usecase_process(request, usecase_id):
    indexhead = "Associated Use Case Processes"
    usecase = UseCase.objects.get(id=usecase_id)
    processes = (
        ProcessUsecase.objects.filter(usecase=usecase)
        .order_by("process__id")
        .distinct("process__id")
    )
    process_list = []
    for process_ in processes:
        process_list.append(process_.process)
    processes = (
        RequirementProcess.objects.filter(process__in=process_list)
        .order_by("process__id")
        .distinct("process__id")
    )
    project = Project.objects.get(id=usecase.project.id)
    paginate = Paginator(processes, 10)
    page_number = request.GET.get("page")
    processes = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/process/process.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "processes": processes,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def usecase_scenario(request, usecase_id):
    indexhead = "Associated Use Case Scenario"
    usecase = UseCase.objects.get(id=usecase_id)
    scenarios = (
        ScenarioUsecase.objects.filter(usecase=usecase)
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    scenario_list = []
    for scenario_ in scenarios:
        scenario_list.append(scenario_.scenario)
    scenarios = (
        RequirementScenario.objects.filter(scenario__in=scenario_list)
        .order_by("scenario__id")
        .distinct("scenario__id")
    )
    project = Project.objects.get(id=usecase.project.id)
    paginate = Paginator(scenarios, 10)
    page_number = request.GET.get("page")
    scenarios = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "scenarios": scenarios,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def process_scenario(request, process_id):
    indexhead = "Associated Process Scenarios"
    process = Process.objects.get(id=process_id)
    scenarios = (
        ScenarioProcess.objects.filter(process=process)
        .order_by("process__id")
        .distinct("process__id")
    )
    scenario_list = []
    for scenario_ in scenarios:
        scenario_list.append(scenario_.scenario)
    scenarios = (
        RequirementScenario.objects.filter(scenario__in=scenario_list)
        .order_by("scenario__id")
        .distinct("scenario__id")
    )
    project = Project.objects.get(id=process.project.id)
    paginate = Paginator(scenarios, 10)
    page_number = request.GET.get("page")
    scenarios = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "scenarios": scenarios,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def scenario_usecase(request, scenario_id):
    indexhead = "Associated Scenario Use Case"
    scenario = Scenario.objects.get(id=scenario_id)
    usecases = (
        ScenarioUsecase.objects.filter(scenario=scenario)
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    usecase_list = []
    for usecase_ in usecases:
        usecase_list.append(usecase_.usecase)
    usecases = (
        RequirementUsecase.objects.filter(usecase__in=usecase_list)
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    project = Project.objects.get(id=scenario.project.id)
    paginate = Paginator(usecases, 10)
    page_number = request.GET.get("page")
    usecases = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "usecases": usecases,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def process_usecase(request, process_id):
    indexhead = "Associated Process Use Cases"
    process = Process.objects.get(id=process_id)
    usecases = (
        ProcessUsecase.objects.filter(process=process)
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    usecase_list = []
    for usecase_ in usecases:
        usecase_list.append(usecase_.usecase)
    usecases = (
        RequirementUsecase.objects.filter(usecase__in=usecase_list)
        .order_by("usecase__id")
        .distinct("usecase__id")
    )
    project = Project.objects.get(id=process.project.id)
    paginate = Paginator(usecases, 10)
    page_number = request.GET.get("page")
    usecases = paginate.get_page(page_number)
    member = Member.objects.get(user=request.user)
    return render(
        request,
        "projects/usecase/usecases.html",
        {
            "indexhead": indexhead,
            "project_id": project.id,
            "usecases": usecases,
            "member": member,
            "project": project,
            "hidesearch": 1,
            "notification": notification(request),
            "total_notification": total_notification(request),
        },
    )


def associate_scenario_with_requirement(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    requirement_list = request.POST.getlist("requirement")
    for requirement in requirement_list:
        requirement = Requirement.objects.get(id=requirement)
        create_scenario_requirement = RequirementScenario.objects.create(
            scenario=scenario, requirement=requirement
        )
        create_scenario_requirement.save()
    return redirect(request.META["HTTP_REFERER"])


def associate_scenario_with_process(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    process_list = request.POST.getlist("process")
    for process in process_list:
        process = Process.objects.get(id=process)
        create_scenario_process = ScenarioProcess.objects.create(
            scenario=scenario, process=process
        )
        create_scenario_process.save()
    return redirect(request.META["HTTP_REFERER"])


def associate_scenario_with_usecase(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    usecase_list = request.POST.getlist("usecase")
    for usecase in usecase_list:
        usecase = UseCase.objects.get(id=usecase)
        create_scenario_usecase = ScenarioUsecase.objects.create(
            scenario=scenario, usecase=usecase
        )
        create_scenario_usecase.save()
    return redirect(request.META["HTTP_REFERER"])


def associate_process_with_scenario(request, process_id):
    process = Process.objects.get(id=process_id)
    scenario_list = request.POST.getlist("scenario")
    for scenario in scenario_list:
        scenario = Scenario.objects.get(id=scenario)
        create_process_scenario = ScenarioProcess.objects.create(
            scenario=scenario, process=process
        )
        create_process_scenario.save()
    return redirect(request.META["HTTP_REFERER"])


def associate_process_with_usecase(request, process_id):
    process = Process.objects.get(id=process_id)
    usecase_list = request.POST.getlist("usecase")
    for usecase in usecase_list:
        usecase = UseCase.objects.get(id=usecase)
        create_process_usecase = ProcessUsecase.objects.create(
            process=process, usecase=usecase
        )
        create_process_usecase.save()
    return redirect(request.META["HTTP_REFERER"])


def associate_process_with_requirement(request, process_id):
    process = Process.objects.get(id=process_id)
    requirement_list = request.POST.getlist("requirement")
    for requirement in requirement_list:
        requirement = Requirement.objects.get(id=requirement)
        create_process_requirement = RequirementProcess.objects.create(
            process=process, requirement=requirement
        )
        create_process_requirement.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_usecase_with_process(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    process_list = request.POST.getlist("process")
    for process in process_list:
        process = Process.objects.get(id=process)
        create_usecase_process = ProcessUsecase.objects.create(
            usecase=usecase, process=process
        )
        create_usecase_process.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_usecase_with_scenario(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    scenario_list = request.POST.getlist("scenario")
    for scenario in scenario_list:
        scenario = Scenario.objects.get(id=scenario)
        create_usecase_scenario = ScenarioUsecase.objects.create(
            usecase=usecase, scenario=scenario
        )
        create_usecase_scenario.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_usecase_with_requirement(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    requirement_list = request.POST.getlist("requirement")
    for requirement in requirement_list:
        requirement = Requirement.objects.get(id=requirement)
        create_usecase_requirement = RequirementUsecase.objects.create(
            usecase=usecase, requirement=requirement
        )
        create_usecase_requirement.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_requirement_with_scenario(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    scenario_list = request.POST.getlist("scenario")
    for scenario in scenario_list:
        scenario = Scenario.objects.get(id=scenario)
        create_requirement_scenario = RequirementScenario.objects.create(
            scenario=scenario, requirement=requirement
        )
        create_requirement_scenario.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_requirement_with_goal(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    goal_list = request.POST.getlist("goal")
    for goal in goal_list:
        goal = Goal.objects.get(id=goal)
        create_association = RequirementGoal.objects.create(
            goal=goal, requirement=requirement
        )
        create_association.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_requirement_with_process(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    process_list = request.POST.getlist("process")
    for process in process_list:
        process = Process.objects.get(id=process)
        create_requirement_process = RequirementProcess.objects.create(
            requirement=requirement, process=process
        )
        create_requirement_process.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_requirement_with_usecase(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    usecase_list = request.POST.getlist("usecase")
    for usecase in usecase_list:
        usecase = UseCase.objects.get(id=usecase)
        create_requirement_usecase = RequirementUsecase.objects.create(
            usecase=usecase, requirement=requirement
        )
        create_requirement_usecase.save()

    return redirect(request.META["HTTP_REFERER"])


def associate_goal_with_viewpoint(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    viewpoint_list = request.POST.getlist("viewpoints")
    for viewpoint in viewpoint_list:
        viewpoint = Viewpoint.objects.get(id=viewpoint)
        create_association = ViewpointGoal.objects.create(
            goal=goal, viewpoint=viewpoint
        )
    return redirect(request.META["HTTP_REFERER"])


def associate_goal_with_requirement(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    requirement_list = request.POST.getlist("requirement")
    for requirement in requirement_list:
        requirement = Requirement.objects.get(id=requirement)
        create_association = RequirementGoal.objects.create(
            goal=goal, requirement=requirement
        )
    return redirect(request.META["HTTP_REFERER"])


def delete_goal_association_with_requirement(request, association_id):
    delete_association = RequirementGoal.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_goal_association_with_viewpoint(request, association_id):
    current_goal_id = int(request.GET.get("ids"))
    print(current_goal_id)
    if current_goal_id == int(association_id):
        goal = ViewpointGoal.objects.get(id=association_id)
        delete_association = ViewpointGoal.objects.filter(id=association_id).delete()
        return general_goals(request, project_id=goal.goal.project.id)

    delete_association = ViewpointGoal.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_requirement_association_with_goal(request, association_id):
    print("hited")
    current_requirement_id = int(request.GET.get("id"))
    if int(association_id) == current_requirement_id:
        requirement = RequirementGoal.objects.get(id=current_requirement_id)
        delete_association = RequirementGoal.objects.filter(id=association_id).delete()
        return general_requirements(
            request, project_id=requirement.requirement.project.id
        )
    delete_association = RequirementGoal.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_requirement_association_with_scenario(request, association_id):
    delete_association = RequirementScenario.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_requirement_association_with_process(request, association_id):
    delete_association = RequirementProcess.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_requirement_association_with_usecase(request, association_id):
    delete_association = RequirementUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_scenario_association_with_requirement(request, association_id):
    current_scenario_id = int(request.GET.get("id"))
    if int(association_id) == current_scenario_id:
        scenario = RequirementScenario.objects.get(id=current_scenario_id)
        delete_association = RequirementScenario.objects.filter(
            id=association_id
        ).delete()
        return general_scenario(request, project_id=scenario.scenario.project.id)
    delete_association = RequirementScenario.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_scenario_association_with_process(request, association_id):
    delete_association = ScenarioProcess.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_scenario_association_with_usecase(request, association_id):
    delete_association = ScenarioUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_process_association_with_usecase(request, association_id):
    delete_association = ProcessUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_process_association_with_scenario(request, association_id):
    delete_association = ScenarioProcess.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_usecase_association_with_requirement(request, association_id):
    current_usecase_id = int(request.GET.get("id"))
    if int(association_id) == current_usecase_id:
        usecase = RequirementUsecase.objects.get(id=current_usecase_id)
        delete_association = RequirementUsecase.objects.filter(
            id=association_id
        ).delete()
        return general_usecase(request, project_id=usecase.usecase.project.id)
    delete_association = RequirementUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_usecase_association_with_scenario(request, association_id):
    delete_association = ScenarioUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_usecase_association_with_process(request, association_id):
    delete_association = ProcessUsecase.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_process_association_with_requirement(request, association_id):
    current_process_id = int(request.GET.get("id"))
    if current_process_id == int(association_id):
        process = RequirementProcess.objects.get(id=current_process_id)
        delete_association = RequirementProcess.objects.filter(
            id=association_id
        ).delete()
        return general_process(request, project_id=process.process.project.id)
    delete_association = RequirementProcess.objects.filter(id=association_id).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_decomposition_with_goal(request, goal_id):
    original_goal_id = int(request.GET.get("id"))
    original_goal = Goal.objects.get(id=original_goal_id)
    decomposed_goal = goal_id
    delete_decomposition = GoalDecomposition.objects.filter(
        original_goal=original_goal, decomposed_goal=decomposed_goal
    ).delete()
    return redirect(request.META["HTTP_REFERER"])


def delete_relationship_with_goal(request, goal_id):
    origin_goal_id = int(request.GET.get("id"))
    origin_goal = Goal.objects.get(id=origin_goal_id)
    related_goal = goal_id
    delete_relationship = GoalRelationship.objects.filter(
        origin_goal=origin_goal, related_goal=related_goal
    ).delete()
    return redirect(request.META["HTTP_REFERER"])


def general_projects(request, project_id=None, message=None, requestmessage=None):
    indexhead = "Projects"
    placeholder = "search projects"
    if request.method == "POST":
        keyword = request.POST.get("project_keyword")
        projects = (
            Project.objects.filter(
                Q(project_title__icontains=keyword)
                | Q(description__icontains=keyword)
                | Q(project_visibility__icontains=keyword)
            )
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
    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(
        request,
        "web/projects.html",
        {
            "indexhead": indexhead,
            "projects": projects,
            "message": message,
            "placeholder": placeholder,
            "project_id": project_id,
            "requestmessage": requestmessage,
        },
    )


@login_required(login_url="login")
def invited(request):
    project_id = request.GET.get("invitation_id")
    if project_id != None:
        project_id = int(project_id)
        member = Member.objects.get(user=request.user)
        project = Project.objects.get(id=project_id)
        if not ProjectMembership.objects.filter(
            project=project, member=member
        ).exists():
            invitation = ProjectMembership.objects.create(
                project=project, member=member, member_role="member", status="invited"
            )
            invitation.save()
            if invitation:
                link = "invitations"
                activity = (
                    "You have been invited by "
                    + str(project.created_by)
                    + " on "
                    + str(project.project_title)
                    + " project"
                )
                notify(request, affected_user=member, activity=activity, link=link)
                return redirect("projects:invitations")

        return redirect("index")
    return redirect("index")


def linear_goals(request, original_goal):
    linear_decomposed_goals_id = GoalDecomposition.objects.filter(
        original_goal=original_goal, decomposition_operator="Linear"
    )
    linear_goal_ids = []
    for goal_id in linear_decomposed_goals_id:
        linear_goal_ids.append(goal_id.decomposed_goal)

    linear_goals = (
        ViewpointGoal.objects.filter(goal__id__in=linear_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(linear_goals, 4)
    page_number = request.GET.get("page")
    linear_goals = paginate.get_page(page_number)
    return linear_goals


def or_goals(request, original_goal):
    or_decomposed_goals_id = GoalDecomposition.objects.filter(
        original_goal=original_goal, decomposition_operator="OR"
    )
    or_goal_ids = []
    for goal_id in or_decomposed_goals_id:
        or_goal_ids.append(goal_id.decomposed_goal)

    or_goals = (
        ViewpointGoal.objects.filter(goal__id__in=or_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(or_goals, 4)
    page_number = request.GET.get("page")
    or_goals = paginate.get_page(page_number)
    return or_goals


def and_goals(request, original_goal):
    and_decomposed_goals_id = GoalDecomposition.objects.filter(
        original_goal=original_goal, decomposition_operator="AND"
    )
    and_goal_ids = []
    for goal_id in and_decomposed_goals_id:
        and_goal_ids.append(goal_id.decomposed_goal)

    and_goals = (
        ViewpointGoal.objects.filter(goal__id__in=and_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(and_goals, 4)
    page_number = request.GET.get("page")
    and_goals = paginate.get_page(page_number)
    return and_goals


def contribute_goals(request, original_goal):
    contribute_related_goals_id = GoalRelationship.objects.filter(
        origin_goal=original_goal, relation_type="Contribute"
    )
    contribute_goal_ids = []
    for goal_id in contribute_related_goals_id:
        contribute_goal_ids.append(goal_id.related_goal)

    contribute_goals = (
        ViewpointGoal.objects.filter(goal__id__in=contribute_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(contribute_goals, 4)
    page_number = request.GET.get("page")
    contribute_goals = paginate.get_page(page_number)
    return contribute_goals


def require_goals(request, original_goal):
    require_related_goals_id = GoalRelationship.objects.filter(
        origin_goal=original_goal, relation_type="Require"
    )
    require_goal_ids = []
    for goal_id in require_related_goals_id:
        require_goal_ids.append(goal_id.related_goal)

    require_goals = (
        ViewpointGoal.objects.filter(goal__id__in=require_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(require_goals, 4)
    page_number = request.GET.get("page")
    require_goals = paginate.get_page(page_number)
    return require_goals


def conflict_goals(request, original_goal):
    conflict_related_goals_id = GoalRelationship.objects.filter(
        origin_goal=original_goal, relation_type="Conflict"
    )
    conflict_goal_ids = []
    for goal_id in conflict_related_goals_id:
        conflict_goal_ids.append(goal_id.related_goal)

    conflict_goals = (
        ViewpointGoal.objects.filter(goal__id__in=conflict_goal_ids)
        .order_by("goal__id")
        .distinct("goal__id")
    )
    paginate = Paginator(conflict_goals, 4)
    page_number = request.GET.get("page")
    conflict_goals = paginate.get_page(page_number)
    return conflict_goals


#generating short Url
def short_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib.request.urlopen(apiurl + url).read()
    return tinyurl.decode("utf-8")