from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.



def index(request):
    if not request.user.is_authenticated:
        return render(request,"login.html" , {})
    indexhead = "Dashboard"
    return render(request, "index.html", {"indexhead": indexhead})


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth_login(request, user)
                return render(request, 'index.html', {})
            message = "sorry your account is inactive communicate with your Admin"
            return render(request, "login.html", {"message": message})
        message = "Soory you entered incorrect credentials"
        return render(request, "login.html", {"message": message})
    return render(request, "login.html", {})


def logout(request):
    auth_logout(request)
    return render(request, "login.html", {})

def registration(request):
    if request.method == "POST":
        pass  
    return render(request, "registration.html", {})


def forgetpassword(request):
    return render(request, "password_recover.html", {})


def pagenotfound(request, exception):

    return render(request, "pagenotfound.html", {})


def servererror(request):

    return render(request, "pagenotfound.html", {})


# project views
def createProject(request):
    indexhead = "Project / Create-Project"
    return render(
        request, "projects/my_projects/create_project.html", {"indexhead": indexhead}
    )


def myProjects(request):
    indexhead = "Projects / My Project(s)"
    return render(
        request, "projects/my_projects/myproject.html", {"indexhead": indexhead}
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
    indexhead = 'Project / Member Requests'
    return render(request,"projects/my_projects/member_request.html",{'indexhead':indexhead})

def inviteMember(request):
    indexhead = 'Project / Invite Members'
    return render(request,"projects/my_projects/member_request.html",{'indexhead':indexhead})

def projects(request):
    indexhead = "Projects"
    return render(
        request, "projects/other_projects/projects.html", {"indexhead": indexhead}
    )
