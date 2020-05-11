from rest_framework import routers
from rest_framework.response import Response
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from .api import *
from .views import *
from .docx_generation import *

app_name = "projects"
urlpatterns = [
    # PROJECT URLS
    path("createproject", createProject, name="createproject"),
    path("myprojects", myProjects, name="myprojects"),
    url(r'^viewmyproject/(?P<project_id>\d+)/$', viewMyproject, name="viewmyproject"),
    url(r'^membershiprequest/(?P<project_id>\d+)/$' , membershipRequest, name='membershiprequest'),
    url(r'^deleteproject/(?P<project_id>\d+)/$', deleteProject, name="deleteproject"),
    # url(r'^projectfilter/(?P<project_id>\w+)/(?P<page>\w+)/$', filterProject, name='filterproject'),
    url(r'^editproject/(?P<project_id>\d+)/$', editProject, name="editproject"),
    url(r'^createprojectcomment/(?P<project_id>\d+)/$', createProjectComment, name="createprojectcomment"),
    url(r'^createviewpointcomment/(?P<viewpoint_id>\d+)/$', createViewpointComment, name="createviewpointcomment"),
    url(r'^projectincentives/(?P<project_id>\d+)/$', projectIncentive, name="projectincentives"),
    path("projects", projects, name="projects"),
    path("membershipprojects", membershipProjects, name="membershipprojects"),
    url(r'^approvemember/(?P<membership_id>\w+)/(?P<project_id>\d+)/$', membershipApproval, name='approvemember'),
    url(r'^membershiprejection/(?P<membership_id>\w+)/(?P<project_id>\d+)/$', membershipRejection, name='membershiprejection'),
    url(r'^projectmembers/(?P<project_id>\d+)/$', projectMembers, name="projectmembers"),
    url(r'^suspendmembership/(?P<membership_id>\d+)/$', suspendMembership, name="suspendmembership"),
    url(r'^activatemembership/(?P<membership_id>\d+)/$', activateMembership, name="activatemembership"),
    url(r'^viewproject/(?P<project_id>\d+)/$', viewProject, name="viewproject"),
    url(r'^memberrequests/(?P<project_id>\d+)/$', memberRequest, name="memberrequest"),
    url(r'^invitemembers/(?P<project_id>\d+)/$', inviteMembers, name="invitemembers"),
    path("profile", profile, name="profile"),
    # VIEWPOINT URLS
    url(r'^viewpoint/(?P<viewpoint_id>\d+)/$', viewPoint, name="viewpoint"),
    url(r'^viewpoints/(?P<project_id>\d+)/$', viewpoints, name="viewpoints"),
    url(r'^createviewpoint/(?P<project_id>\d+)/$', createViewpoint, name="createviewpoint"),
        # GOAL URLS
    url(r'^goals/(?P<viewpoint_id>\d+)/$', goals, name="goals"),
    url(r'^viewgoal/(?P<goal_id>\d+)/$', viewGoal, name="viewgoal"),
    url(r'^creategoal/(?P<viewpoint_id>\d+)/$', createGoal, name="creategoal"),
        # REQUIREMENT URLS
    url(r'^requirements/(?P<goal_id>\d+)/$', requirements, name="requirements"),
    url(r'^viewrequirement/(?P<requirement_id>\d+)/$', viewrequirement, name="viewrequirement"),
    url(r'^createrequirement/(?P<goal_id>\d+)/$', createRequirement, name="createrequirement"),
        # SCENARIO URLS
    url(r'^scenarios/(?P<requirement_id>\d+)/$', scenarios, name='scenarios'),
    url(r'^viewscenario/(?P<scenario_id>\d+)/$', viewscenario, name='viewscenario'),
    url(r'^createscenario/(?P<requirement_id>\d+)/$', createScenario, name='createscenario'),
        # PROCESS URLS
    url(r'^processes/(?P<scenario_id>\d+)/$', processes, name="processes"),
    url(r'^viewprocess/(?P<process_id>\d+)/$', viewprocess, name="viewprocess"),
    url(r'^createprocess/(?P<scenario_id>\d+)/$', createProcess, name="createprocess"),
        # USECASE URLS
    url(r'^usecases/(?P<process_id>\d+)/$', usecases, name="usecases"),
    url(r'^viewusecase/(?P<usecase_id>\d+)/$', viewusecase, name="viewusecase"),
    url(r'^createusecase/(?P<process_id>\d+)/$', createUsecase, name="createusecase"),
    
    # Creating word docs URL
    url(r'^generatedocs/(?P<project_id>\d+)/$', create_docx, name='generatedocs'),
    
    # rating URLS
    url(r'^rateproject/(?P<project_id>\d+)/$', projectRate, name='rateproject'),
    url(r'^rateviewpoint/(?P<viewpoint_id>\d+)/$', viewpointRate, name='rateviewpoint'),
    path("logout", logout, name="logout"),

    # From Project to usecase Resources URLS 
    url(r'^viewpointresources/(?P<viewpoint_id>\d+)/$', viewpointResources, name='viewpointresources'),
    url(r'^projectresources/(?P<project_id>\d+)/$', projectResources, name='projectresources'),
    url(r'^addprojectresources/(?P<project_id>\d+)/$', addProjectResources, name='addprojectresources'),
    url(r'^addviewpointresources/(?P<viewpoint_id>\d+)/$', addViewpointResources, name='addviewpointresources'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
