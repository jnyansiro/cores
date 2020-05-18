from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.
def privacyPolicy(requiest):
    pass
def termsConditions(request):
    pass

def indexs(request):
    members = Member.objects.all().count()
    members = members + 100
    projects = Project.objects.all().count()
    projects = projects + 10
    comments = Comment.objects.all().count()
    rates = StarRate.objects.all().count()
    return render(request, "web/index.html", {'members':members, 'projects':projects,'rates':rates, 'comments':comments})


@login_required(login_url="login")
def index(request):

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
            "member": member,
            "members": members,
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


# project views and project workspace
@login_required(login_url="login")
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
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "sectors": sectors,
            "member": member,
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
    member_details = Member.objects.exclude(id__in=ids).order_by("-id")
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
            return profile(request)
    return profile(request)


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
            return profile(request)
    return profile(request)


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
            return profile(request)
    return profile(request)


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
        },
    )


@login_required(login_url="login")
def deleteProject(request, project_id):
    delete_project = Project.objects.get(id=project_id).delete()
    if delete_project:
        return myProjects(request)


@login_required(login_url="login")
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
                comments = ViewPointComment.objects.filter(viewpoint=viewpoint)
                return viewPoint(request, viewpoint_id=viewpoint_id)
    return viewPoint(request, viewpoint_id=viewpoint_id)


@login_required(login_url="login")
def projectIncentive(request, project_id=None):
    project = Project.objects.get(id=project_id)
    hidesearch = "hide"
    return render(
        request,
        "projects/my_projects/project_incentive.html",
        {"hidesearch": hidesearch, "project_id": project_id,'project':project},
    )


@login_required(login_url="login")
def membershipProjects(request):
    indexhead = "Projects / Membership Project(s)"
    member = Member.objects.get(user=request.user)
    membershipprojects = ProjectMembership.objects.filter(
        member=member, status="active", member_role="member"
    ).order_by("-id")
    return render(
        request,
        "projects/other_projects/membership_projects.html",
        {
            "indexhead": indexhead,
            "membershipprojects": membershipprojects,
            "member": member,
        },
    )


@login_required(login_url="login")
def myProjects(request):
    indexhead = "Projects / My Project(s)"
    member = Member.objects.get(user=request.user)
    myProject = Project.objects.filter(created_by=member).order_by("-id")
    return render(
        request,
        "projects/my_projects/myproject.html",
        {"indexhead": indexhead, "myProject": myProject, "member": member},
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
    total_rates = rates.count()
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
            "member": member,
            "projectRate": projectRate,
            "total_rates": total_rates,
            "rates": rates,
        },
    )


@login_required(login_url="login")
def viewProject(request, project_id, message=None):
    indexhead = "Project Details"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    project = Project.objects.get(id=project_id)
    comments = ProjectComment.objects.filter(project=project).order_by("-id")
    projectRate = ProjectRate.objects.filter(
        project=project, star_rate__rated_by=member
    )
    rates = ProjectRate.objects.filter(project=project).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    if project.project_visibility == "private":
        if ProjectMembership.objects.filter(member=member, project=project).exists():
            membership = ProjectMembership.objects.get(member=member, project=project)

            if membership.status == "request":
                requestmessage = "Sorry your Request to join this project is still on processing stage, we will notify you once your request being accepted or rejected"
                return projects(
                    request, project_id=project_id, requestmessage=requestmessage
                )
            if membership.status == "rejected":
                requestmessage = "Sorry you can not access this project, your Request to join this project has been Rejected"
                return projects(
                    request, project_id=project_id, requestmessage=requestmessage
                )
            if membership.status == "removed":
                requestmessage = "Sorry you can not access this project, you have been removed from this project"
                return projects(
                    request, project_id=project_id, requestmessage=requestmessage
                )
            if membership.status == "suspended":
                requestmessage = "Sorry you can not access this project, your  project membership has been suspended"
                return projects(
                    request, project_id=project_id, requestmessage=requestmessage
                )
            return render(
                request,
                "projects/other_projects/view_project.html",
                {
                    "indexhead": indexhead,
                    "hidesearch": hidesearch,
                    "project": project,
                    "comments": comments,
                    "total_comments": total_comments,
                    "member": member,
                    "projectRate": projectRate,
                    "message": message,
                    "rates": rates,
                    "total_rates": total_rates,
                },
            )
        message = "This is Private Project, Do you want to ask for joining?"
        return projects(request, project_id=project.id, message=message)
    return render(
        request,
        "projects/other_projects/view_project.html",
        {
            "indexhead": indexhead,
            "hidesearch": hidesearch,
            "project": project,
            "comments": comments,
            "total_comments": total_comments,
            "member": member,
            "projectRate": projectRate,
            "message": message,
            "rates": rates,
            "total_rates": total_rates,
        },
    )


@login_required(login_url="login")
def projectMembers(request, project_id=None):
    indexhead = "Projects / Project-Members"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    project_member = (
        ProjectMembership.objects.filter(project=project)
        .exclude(status__in=["removed", "rejected", "invited"])
        .order_by("-id")
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
            return viewProject(request, project_id=project_id)
    return viewProject(request, project_id=project_id)


@login_required(login_url="login")
def membershipApproval(request, membership_id, project_id):
    member = ProjectMembership.objects.filter(id=membership_id)
    member.update(status="active")
    if member:
        return memberRequest(request, project_id=project_id)


@login_required(login_url="login")
def membershipRejection(request, membership_id, project_id):
    member = ProjectMembership.objects.filter(id=membership_id).update(
        status="rejected"
    )
    if member:
        return memberRequest(request, project_id=project_id)


@login_required(login_url="login")
def suspendMembership(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)

    if membership.member_role != "Admin":
        suspend = ProjectMembership.objects.filter(id=membership_id).update(
            status="suspended"
        )
        if suspend:
            return projectMembers(request, project_id=membership.project.id)
    return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def removeMember(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)
    if membership.member_role != "Admin":
        remove = ProjectMembership.objects.filter(id=membership_id).delete()
        if remove:
            return projectMembers(request, project_id=membership.project.id)
    return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def incentives(request):
    indexhead = "Member Incentives"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    incentives = ProjectIncentive.objects.filter(member=member)
    return render(
        request,
        "user/incentives.html",
        {
            "indexhead": indexhead,
            "incentives": incentives,
            "member": member,
            "hidesearch": hidesearch,
        },
    )


@login_required(login_url="login")
def invitations(request):
    indexhead = "Project Membership Invitations:"
    hidesearch = "hide"
    member = Member.objects.get(user=request.user)
    invitations = ProjectMembership.objects.filter(member=member, status="invited")
    return render(
        request,
        "user/invitations.html",
        {
            "member": member,
            "indexhead": indexhead,
            "invitations": invitations,
            "hidesearch": hidesearch,
        },
    )


@login_required(login_url="login")
def acceptInvitation(request, request_id):
    accept = ProjectMembership.objects.filter(id=request_id).update(status="active")
    if accept:
        return invitations(request)


@login_required(login_url="login")
def rejectInvitation(request, request_id):
    reject = ProjectMembership.objects.filter(id=request_id).update(status="Rejected")
    if reject:
        return invitations(request)


@login_required(login_url="login")
def activateMembership(request, membership_id):
    membership = ProjectMembership.objects.get(id=membership_id)
    activate = ProjectMembership.objects.filter(id=membership_id).update(
        status="active"
    )
    if activate:
        return projectMembers(request, project_id=membership.project.id)


@login_required(login_url="login")
def memberRequest(request, project_id):
    indexhead = "Project / Member Requests"
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    member_details = ProjectMembership.objects.filter(project=project, status="request")

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
        },
    )


@login_required(login_url="login")
def projects(request, project_id=None, message=None, requestmessage=None):
    indexhead = "Projects"
    member = Member.objects.get(user=request.user)
    projects = Project.objects.all().order_by("-id")

    return render(
        request,
        "projects/other_projects/projects.html",
        {
            "indexhead": indexhead,
            "projects": projects,
            "member": member,
            "message": message,
            "project_id": project_id,
            "requestmessage": requestmessage,
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
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    viewpointRate = ViewPointRate.objects.filter(
        view_point=viewpoint, star_rate__rated_by=member
    )
    rates = ViewPointRate.objects.filter(view_point=viewpoint).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
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
            "member": member,
            "project": project,
            "message": message,
            "viewpointRate": viewpointRate,
            "rates": rates,
            "total_rates": total_rates,
            "comments": comments,
            "total_comments": total_comments,
            "message": message,
        },
    )


@login_required(login_url="login")
def viewpoints(request, project_id):

    indexhead = "Project - ViewPoint"
    project = Project.objects.get(id=project_id)
    hidesearch = "hide"
    projects = Project.objects.all().order_by("-id")
    if request.method == "POST":
        project_id = request.POST.get("project")
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
                "member": member,
                "project": project,
                "projects": projects,
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
            "member": member,
            "project": project,
            "projects": projects,
        },
    )


@login_required(login_url="login")
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
                    "member": member,
                    "project": project,
                },
            )

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
                "member": member,
                "project": project,
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
        },
    )


@login_required(login_url="login")
def viewGoal(request, goal_id,message=None):
    indexhead = "Goal Description"
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    comments = GoalComment.objects.filter(goal=goal).order_by("-id")
    goalRate = GoalRate.objects.filter(
        goal=goal, star_rate__rated_by=member
    )
    rates = GoalRate.objects.filter(goal=goal).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
    if request.method == "POST":
        goal = request.POST.get("goal")
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
                'comments':comments,
                'goalRate':goalRate,
                'tota_rates':total_rates,
                'total_comments':total_comments,
                'message':message,
                'rates':rates,
                "goals": goals,
                "member": member,
                "project": project,
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
            'comments':comments,
            'goalRate':goalRate,
            'tota_rates':total_rates,
            'total_comments':total_comments,
            'rates':rates,
            "goals": goals,
            'message':message,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def createGoal(request, viewpoint_id):
    indexhead = "Create Goal"
    member = Member.objects.get(user=request.user)
    categories = Category.objects.all().order_by("category_name")
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
                    "member": member,
                    "project": project,
                },
            )

    return render(
        request,
        "projects/Goals/create_goal.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
            "categories": categories,
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
                "member": member,
                "project": project,
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
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def viewrequirement(request, requirement_id=None, message=None):
    indexhead = "Requirement Description"
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    comments = RequirementComment.objects.filter(requirement=requirement).order_by("-id")
    requirementRate = RequirementRate.objects.filter(
        requirement=requirement, star_rate__rated_by=member
    )
    rates = RequirementRate.objects.filter(requirement=requirement).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()
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
        comments = RequirementComment.objects.filter(requirement=requirement).order_by("-id")
        requirementRate = RequirementRate.objects.filter(
            requirement=requirement, star_rate__rated_by=member
        )
        rates = RequirementRate.objects.filter(requirement=requirement).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
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
                'rates':rates,
                'total_rates':total_rates,
                'requirementRate':requirementRate,
                'comments':comments,
                'total_comments':total_comments,
                "requirements": requirements,
                "requirement": requirement,
                "member": member,
                "project": project,
            },
        )
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
            'rates':rates,
            'total_rates':total_rates,
            'comments':comments,
            'total_comments':total_comments,
            'requirementRate':requirementRate,
            "requirements": requirements,
            "requirement": requirement,
            'message':message,
            "member": member,
            "project": project,
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
        requirement_link = request.POST.get("link")
        requirement_photo = request.FILES.get("requirement_photo")
        requirement_docs = request.FILES.get("requirement_docs")
        description = request.POST.get("requirement_descriptions")
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        requirement = Requirement.objects.create(
            name=requirement_title,
            requirement_photo=requirement_photo,
            requirement_links=requirement_link,
            created_by=created_by,
            requirement_docs=requirement_docs,
            description=description,
            goal=goal,
        )
        requirement.save()
        if requirement:
            indexhead = "Goal-Requirements"
            requirements = Requirement.objects.filter(goal=goal).order_by("-id")
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
                    "member": member,
                    "project": project,
                },
            )

    return render(
        request,
        "projects/requirements/create_requirement.html",
        {
            "indexhead": indexhead,
            "goal_id": goal_id,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
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
                "scenarios": scenarios,
                "goals": goals,
                "requirement_id": requirement_id,
                "member": member,
                "project": project,
            },
        )

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
        "projects/scenario/scenarios.html",
        {
            "indexhead": indexhead,
            "viewpoint_id": viewpoint_id,
            "goal_id": goal.id,
            "project_id": project_id,
            "requirements": requirements,
            "scenarios": scenarios,
            "viewpoints": viewpoints,
            "goals": goals,
            "requirement_id": requirement_id,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def viewscenario(request, scenario_id=None, message=None):
    indexhead = "Scenario Description"
    member = Member.objects.get(user=request.user)
    scenario = Scenario.objects.get(id=scenario_id)
    comments = ScenarioComment.objects.filter(scenario=scenario).order_by("-id")
    scenarioRate = ScenarioRate.objects.filter(
            scenario=scenario, star_rate__rated_by=member
        )
    rates = ScenarioRate.objects.filter(scenario=scenario).order_by(
        "-star_rate__number_of_stars"
    )
    total_rates = rates.count()
    total_comments = comments.count()

    if request.POST.get("scenario"):
        scenario_id = request.POST.get("scenario")
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
        comments = ScenarioComment.objects.filter(scenario=scenario).order_by("-id")
        scenarioRate = ScenarioRate.objects.filter(
                scenario=scenario, star_rate__rated_by=member
            )
        rates = ScenarioRate.objects.filter(scenario=scenario).order_by(
            "-star_rate__number_of_stars"
        )
        total_rates = rates.count()
        total_comments = comments.count()
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
                "scenarios": scenarios,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                'rates':rates,
                'total_rates':total_rates,
                'comments':comments,
                'total_comments':comments,
                'scenarioRate':scenarioRate,
                "member": member,
                "project": project,
            },
        )
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    scenarios = Scenario.objects.filter(requirement=requirement)
    goal = Goal.objects.get(id=requirement.goal.id)
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
            "viewpoints": viewpoints,
            "scenarios": scenarios,
            "requirements": requirements,
            "requirement_id": requirement.id,
            'rates':rates,
            'total_rates':total_rates,
            'comments':comments,
            'total_comments':total_comments,
            'scenarioRate':scenarioRate,
            'message':message,
            "member": member,
            "project": project,
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
    viewpoints = Viewpoint.objects.filter(project=project.id).order_by("-id")
    if request.method == "POST":
        scenario_title = request.POST.get("scenario_title")
        scenario_link = request.POST.get("link")
        scenario_photo = request.FILES.get("scenario_photo")
        scenario_docs = request.FILES.get("scenario_docs")
        description = request.POST.get("scenario_descriptions")
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        scenario = Scenario.objects.create(
            name=scenario_title,
            scenario_photo=scenario_photo,
            scenario_links=scenario_link,
            created_by=created_by,
            scenario_docs=scenario_docs,
            description=description,
            requirement=requirement,
        )
        scenario.save()
        if scenario:
            indexhead = "Requirements-Scenarios:"
            requirements = Requirement.objects.filter(goal=goal).order_by("-id")
            scenarios = Scenario.objects.filter(requirement=requirement).order_by("-id")
            return render(
                request,
                "projects/scenario/scenarios.html",
                {
                    "indexhead": indexhead,
                    "viewpoint_id": viewpoint_id,
                    "goal_id": goal.id,
                    "project_id": project_id,
                    "requirements": requirements,
                    "requirement_id": requirement.id,
                    "scenarios": scenarios,
                    "viewpoints": viewpoints,
                    "goals": goals,
                    "member": member,
                    "project": project,
                },
            )
    return render(
        request,
        "projects/scenario/create_scenario.html",
        {
            "indexhead": indexhead,
            "requirement_id": requirement_id,
            "viewpoints": viewpoints,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def processes(request, scenario_id):
    indexhead = "Scenario-Processes"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        scenario_id = request.POST.get("scenario")
        scenario = Scenario.objects.get(id=scenario_id)
        processes = Process.objects.filter(scenario=scenario)
        requirement = Requirement.objects.get(id=scenario.requirement.id)
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
                "scenario_id": scenario.id,
                "goals": goals,
                "requirement_id": requirement.id,
                "member": member,
                "project": project,
            },
        )

    scenario = Scenario.objects.get(id=scenario_id)
    processes = Process.objects.filter(scenario=scenario)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
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
            "scenarios": scenarios,
            "scenario_id": scenario.id,
            "viewpoints": viewpoints,
            "goals": goals,
            "processes": processes,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
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
                'rates':rates,
                'total_rates':total_rates,
                'processRate':processRate,
                'comments':comments,
                'total_comments':total_comments,
                "processes": processes,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                "member": member,
                "project": project,
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
            "viewpoints": viewpoints,
            "processes": processes,
            "scenarios": scenarios,
            "requirements": requirements,
            "requirement_id": requirement.id,
            'rates':rates,
            'total_rates':total_rates,
            'processRate':processRate,
            'comments':comments,
            'total_comments':total_comments,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def createProcess(request, scenario_id):
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
    if request.method == "POST":
        process_title = request.POST.get("process_title")
        process_link = request.POST.get("link")
        process_photo = request.FILES.get("process_photo")
        process_docs = request.FILES.get("process_docs")
        description = request.POST.get("process_descriptions")
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        process = Process.objects.create(
            process_name=process_title,
            process_photo=process_photo,
            process_links=process_link,
            created_by=created_by,
            process_docs=process_docs,
            description=description,
            scenario=scenario,
        )
        process.save()
        if process:
            indexhead = "Scenario-Processes:"
            requirements = Requirement.objects.filter(goal=goal).order_by("-id")
            scenarios = Scenario.objects.filter(requirement=requirement).order_by("-id")
            processes = Process.objects.filter(scenario=scenario).order_by("-id")
            return render(
                request,
                "projects/process/process.html",
                {
                    "indexhead": indexhead,
                    "viewpoint_id": viewpoint_id,
                    "goal_id": goal.id,
                    "project_id": project_id,
                    "requirements": requirements,
                    "requirement_id": requirement.id,
                    "scenarios": scenarios,
                    "scenario_id": scenario.id,
                    "viewpoints": viewpoints,
                    "processes": processes,
                    "goals": goals,
                    "member": member,
                    "project": project,
                },
            )

    return render(
        request,
        "projects/process/create_process.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "scenario_id": scenario_id,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
def usecases(request, process_id):
    indexhead = "Process-Usecases"
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        process_id = request.POST.get("process")
        process = Process.objects.get(id=process_id)
        scenario = Scenario.objects.get(id=process.scenario.id)
        usecases = UseCase.objects.filter(process=process).order_by("-id")
        processes = Process.objects.filter(scenario=scenario)
        requirement = Requirement.objects.get(id=scenario.requirement.id)
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
                "scenarios": scenarios,
                "processes": processes,
                "scenario_id": scenario.id,
                "goals": goals,
                "usecases": usecases,
                "process_id": process.id,
                "requirement_id": requirement.id,
                "member": member,
                "project": project,
            },
        )
    process = Process.objects.get(id=process_id)
    usecases = UseCase.objects.filter(process=process).order_by("-id")
    scenario = Scenario.objects.get(id=process.scenario.id)
    processes = Process.objects.filter(scenario=scenario)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
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
            "scenarios": scenarios,
            "scenario_id": scenario.id,
            "viewpoints": viewpoints,
            "goals": goals,
            "usecases": usecases,
            "process_id": process.id,
            "processes": processes,
            "requirement_id": requirement.id,
            "member": member,
            "project": project,
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
                "process": process,
                "process_id": process.id,
                "scenarios": scenarios,
                "processes": processes,
                "usecase": usecase,
                "usecases": usecases,
                "usecase_id": usecase.id,
                "viewpoints": viewpoints,
                "requirements": requirements,
                "requirement_id": requirement.id,
                'rates':rates,
                'total_rates':total_rates,
                'usecaseRate':usecaseRate,
                'comments':comments,
                'total_comments':total_comments,
                "member": member,
                "project": project,
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
            'message':message,
            "viewpoints": viewpoints,
            "processes": processes,
            "scenarios": scenarios,
            "usecase": usecase,
            "usecases": usecases,
            "usecase_id": usecase_id,
            "process_id": process.id,
            "requirements": requirements,
            "requirement_id": requirement.id,
            'rates':rates,
            'total_rates':total_rates,
            'usecaseRate':usecaseRate,
            'comments':comments,
            'total_comments':total_comments,
            "member": member,
            "project": project,
        },
    )


@login_required(login_url="login")
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
    if request.method == "POST":
        usecase_title = request.POST.get("usecase_title")
        usecase_link = request.POST.get("link")
        usecase_photo = request.FILES.get("usecase_photo")
        usecase_docs = request.FILES.get("usecase_docs")
        description = request.POST.get("usecase_descriptions")
        created_by = Member.objects.get(user=request.user)

        # then creating requirement
        usecase = UseCase.objects.create(
            usecase_name=usecase_title,
            usecase_photo=usecase_photo,
            usecase_link=usecase_link,
            created_by=created_by,
            usecase_docs=usecase_docs,
            description=description,
            process=process,
        )
        usecase.save()
        if usecase:
            indexhead = "Process-Usecases:"
            requirements = Requirement.objects.filter(goal=goal).order_by("-id")
            scenarios = Scenario.objects.filter(requirement=requirement).order_by("-id")
            processes = Process.objects.filter(scenario=scenario).order_by("-id")
            usecases = UseCase.objects.filter(process=process).order_by("-id")
            return render(
                request,
                "projects/usecase/usecases.html",
                {
                    "indexhead": indexhead,
                    "viewpoint_id": viewpoint_id,
                    "goal_id": goal.id,
                    "project_id": project_id,
                    "requirements": requirements,
                    "requirement_id": requirement.id,
                    "scenarios": scenarios,
                    "scenario_id": scenario.id,
                    "viewpoints": viewpoints,
                    "processes": processes,
                    "process_id": process.id,
                    "usecases": usecases,
                    "goals": goals,
                    "member": member,
                    "project": project,
                },
            )

    return render(
        request,
        "projects/usecase/create_usecase.html",
        {
            "indexhead": indexhead,
            "viewpoints": viewpoints,
            "process_id": process_id,
            "member": member,
            "project": project,
        },
    )


# Rate


@login_required(login_url="login")
def projectRate(request, project_id):
    if request.POST.get("rate") != None:

        project = Project.objects.get(id=project_id)
        member = Member.objects.get(user=request.user)

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
                    return viewProject(request, project_id=project_id)
        message = (
            "sorry you have already rated this project you can not rate this again"
        )
        return viewProject(request, project_id=project_id, message=message)
    message = "sorry you can not rate zero star, rate start from one star !!"
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
                    return viewPoint(
                        request, project_id=project_id, viewpoint_id=viewpoint_id
                    )

        message = "sorry you have already rated this Viewpoint you can not rate again"
        return viewPoint(
            request, project_id=project.id, viewpoint_id=viewpoint_id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewPoint(
        request, project_id=project.id, viewpoint_id=viewpoint_id, message=message
    )

@login_required(login_url="login")
def goalRate(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not GoalRate.objects.filter(
            goal=goal, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                goal_rate = GoalRate.objects.create(
                    goal=goal, star_rate=rate
                )
                goal_rate.save()
                if goal_rate:
                    return viewGoal(
                        request, goal_id=goal.id
                    )

        message = "sorry you have already rated this Goal you can not rate it again"
        return viewGoal(
            request, goal_id=goal.id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewGoal(
        request, goal_id=goal.id, message=message
    )


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
                    return viewrequirement(
                        request, requirement_id=requirement.id
                    )

        message = "sorry you have already rated this requirement you can not rate it again"
        return viewrequirement(
            request, requirement_id=requirement.id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewrequirement(
        request,requirement_id=requirement.id, message=message
    )

@login_required(login_url="login")
def scenarioRate(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    if request.POST.get("rate") != None:
        member = Member.objects.get(user=request.user)
        if not ScenarioRate.objects.filter(
            scenario=scenario, star_rate__rated_by=member
        ).exists():

            rate = StarRate.objects.create(
                rated_by=member, number_of_stars=request.POST.get("rate")
            )
            rate.save()
            if rate:

                scenario_rate = ScenarioRate.objects.create(
                    scenario=scenario, star_rate=rate
                )
                scenario_rate.save()
                if scenario_rate:
                    return viewscenario(
                        request, scenario_id=scenario.id
                    )

        message = "sorry you have already rated this Scenario you can not rate it again"
        return viewscenario(
            request,scenario_id=scenario.id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewscenario(
        request, scenario_id=scenario.id, message=message
    )

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
                    return viewprocess(
                        request, process_id=process.id
                    )

        message = "sorry you have already rated this process you can not rate it again"
        return viewprocess(
            request,process_id=process.id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewprocess(
        request, process_id=process.id, message=message
    )

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
                    return viewusecase(
                        request, usecase_id=usecase.id
                    )

        message = "sorry you have already rated this Usecase you can not rate it again"
        return viewusecase(
            request,usecase_id=usecase.id, message=message
        )
    message = "sorry you can not rate zero star, rate start from one star !!"
    return viewusecase(
        request, usecase_id=usecase.id, message=message
    )

# resources functions for all from project to usecase


@login_required(login_url="login")
def projectResources(request, project_id):
    indexhead = "Project Resources:"
    hidesearch = "hide"
    project = Project.objects.get(id=project_id)
    resources = ProjectRepository.objects.filter(project=project).order_by("-id")
    member = Member.objects.get(user=request.user)
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
        },
    )


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
            "goal_id":goal.id,
            'goal':goal,
            'viewpoint':viewpoint,
            "member": member,
            "project": project,
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
    resources = RequirementRepository.objects.filter(requirement=requirement).order_by("-id")
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
            "requirement_id":requirement.id,
            "requirement":requirement,
            'viewpoint':viewpoint,
            "member": member,
            "project": project,
        },
    )

@login_required(login_url="login")
def scenarioResources(request, scenario_id):
    indexhead = "Scenario Resources:"
    hidesearch = "hide"
    scenario = Scenario.objects.get(id=scenario_id)
    requirement = Requirement.objects.get(id=scenario.requirement.id)
    goal = Goal.objects.get(id=requirement.goal.id)
    viewpoint = Viewpoint.objects.get(id=goal.viewpoint.id)
    project = Project.objects.get(id=viewpoint.project.id)
    resources = ScenarioRepository.objects.filter(scenario=scenario).order_by("-id")
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
            "requirement":requirement,
            "scenario_id":scenario.id,
            'scenario':scenario,
            "viewpoint":viewpoint,
            "member": member,
            "project": project
        }
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
            "requirement":requirement,
            'viewpoint':viewpoint,
            'process':process,
            'process_id':process.id,
            "member": member,
            "project": project,
        }
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
                "requirement":requirement,
                'usecase_id':usecase.id,
                'usecase':usecase,
                'viewpoint':viewpoint,
                "member": member,
                "project": project,
            }
        )


@login_required(login_url="login")
def addProjectResources(request, project_id):
    project = Project.objects.get(id=project_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            projectrepository = ProjectRepository.objects.create(
                project=project, repository=repository
            )
            projectrepository.save()
            if projectrepository:
                return projectResources(request, project_id)
    return projectResources(request, project_id)


@login_required(login_url="login")
def addViewpointResources(request, viewpoint_id):
    viewpoint = Viewpoint.objects.get(id=viewpoint_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            viewpointrepository = ViewpointRepository.objects.create(
                viewpoint=viewpoint, repository=repository
            )
            viewpointrepository.save()
            if viewpointrepository:
                return viewpointResources(request, viewpoint_id)
    return viewpointResources(request, viewpoint_id)

@login_required(login_url="login")
def addGoalResources(request, goal_id):
    goal= Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            goalrepository = GoalRepository.objects.create(
                goal=goal, repository=repository
            )
            goalrepository.save()
            if goalrepository:
                return goalResources(request, goal_id)
    return goalResources(request, goal_id)

@login_required(login_url="login")
def addRequirementResources(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            requirementrepository = RequirementRepository.objects.create(
                requirement=requirement, repository=repository
            )
            requirementrepository.save()
            if requirementrepository:
                return requirementResources(request, requirement_id)
    return requirementResources(request, requirement_id)


@login_required(login_url="login")
def addScenarioResources(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            scenariorepository = ScenarioRepository.objects.create(
                scenario=scenario, repository=repository
            )
            scenariorepository.save()
            if scenariorepository:
                return scenarioResources(request, scenario_id)
    return scenarioResources(request, scenario_id)

@login_required(login_url="login")
def addProcessResources(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            processrepository = ProcessRepository.objects.create(
                process=process, repository=repository
            )
            processrepository.save()
            if processrepository:
                return processResources(request, process_id)
    return processResources(request, process_id)

@login_required(login_url="login")
def addUsecaseResources(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        image = request.FILES.get("image")
        docs = request.FILES.get("docs")
        links = request.POST.get("links")
        repository = Repository.objects.create(
            added_by=member, image=image, links=links, docs=docs,
        )
        repository.save()
        if repository:
            usecaserepository = UsecaseRepository.objects.create(
                usecase=usecase, repository=repository
            )
            usecaserepository.save()
            if usecaserepository:
                return usecaseResources(request, usecase_id)
    return usecaseResources(request, usecase_id)

@login_required(login_url="login")
def goalComment(request, goal_id):
    goal = Goal.objects.get(id=goal_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        goal_comment = GoalComment.objects.create(
            comment=create_comment,
            goal=goal
        )
        goal_comment.save()
        return viewGoal(request,goal_id=goal_id)
    return viewGoal(request,goal_id=goal_id)

@login_required(login_url="login")
def requirementComment(request, requirement_id):
    requirement = Requirement.objects.get(id=requirement_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        requirement_comment = RequirementComment.objects.create(
            comment=create_comment,
            requirement=requirement
        )
        requirement_comment.save()
        return viewrequirement(request,requirement_id=requirement_id)
    return viewrequirement(request,requirement_id=requirement_id)


@login_required(login_url="login")
def scenarioComment(request, scenario_id):
    scenario = Scenario.objects.get(id=scenario_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        scenario_comment = ScenarioComment.objects.create(
            comment=create_comment,
            scenario=scenario
        )
        scenario_comment.save()
        return viewscenario(request,scenario_id=scenario_id)
    return viewscenario(request,scenario_id=scenario_id)

@login_required(login_url="login")
def processComment(request, process_id):
    process = Process.objects.get(id=process_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        process_comment = ProcessComment.objects.create(
            comment=create_comment,
            process=process
        )
        process_comment.save()
        return viewprocess(request,process_id=process_id)
    return viewprocess(request,process_id=process_id)

@login_required(login_url="login")
def usecaseComment(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        usecase_comment = UseCaseComment.objects.create(
            comment=create_comment,
            usecase=create_comment
        )
        usecase_comment.save()
        return viewusecase(request,usecase_id=usecase_id)
    return viewusecase(request,usecase_id=usecase_id)


@login_required(login_url="login")
def usecaseComment(request, usecase_id):
    usecase = UseCase.objects.get(id=usecase_id)
    member = Member.objects.get(user=request.user)
    if request.method == "POST":
        comment = request.POST.get('comment')
        create_comment = Comment.objects.create(
            comment=comment,
            commented_by=member
        )
        create_comment.save()
        usecase_comment = UseCaseComment.objects.create(
            comment=create_comment,
            usecase=usecase
        )
        usecase_comment.save()
        return viewusecase(request,usecase_id=usecase_id)
    return viewusecase(request,usecase_id=usecase_id)