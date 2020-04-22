from rest_framework import routers
from rest_framework.response import Response
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .api import *
from .views import *

app_name = "projects"
urlpatterns = [
    path("createproject", createProject, name="createproject"),
    path("myprojects", myProjects, name="myprojects"),
    url(r'^viewmyproject/(?P<project_id>\d+)/$', viewMyproject, name="viewmyproject"),
    path("projects", projects, name="projects"),
    path("projectmembers", projectMembers, name="projectmembers"),
    url(r'^viewproject/(?P<project_id>\d+)/$', viewProject, name="viewproject"),
    path("memberrequests", memberRequest, name="memberrequest"),
    path("profile", profile, name="profile"),
    url(r'^viewpoint/(?P<viewpoint_id>\d+)/$', viewpoint, name="viewpoint"),
    url(r'^viewpoints/(?P<project_id>\d+)/$', viewpoints, name="viewpoints"),
    url(r'^createviewpoint/(?P<project_id>\d+)/$', createViewpoint, name="createviewpoint"),
    url(r'^goals/(?P<viewpoint_id>\d+)/$', goals, name="goals"),
    url(r'^viewgoal/(?P<goal_id>\d+)/$', viewGoal, name="viewgoal"),
    url(r'^creategoal/(?P<viewpoint_id>\d+)/$', createGoal, name="creategoal"),
    path("requirements", requirements, name="requirements"),
    path("viewrequirement", viewrequirement, name="viewrequirement"),
    path("createrequirement", createRequirement, name="createrequirement"),
    path("scenarios", scenarios, name='scenarios'),
    path("viewscenario", viewscenario, name='viewscenario'),
    path("createscenario", createScenario, name='createscenario'),
    path("processes", processes, name="processes"),
    path("viewprocess", viewprocess, name="viewprocess"),
    path("createprocess", createProcess, name="createprocess"),
    path("usecases", usecases, name="usecases"),
    path("viewusecase", viewusecase, name="viewusecase"),
    path("createusecase", createUsecase, name="createusecase"),
    path("logout", logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
