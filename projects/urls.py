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
    url(r'^projectincentives/(?P<project_id>\d+)/$', projectIncentive, name="projectincentives"),
    path("projects", projects, name="projects"),
    path("membershipprojects", membershipProjects, name="membershipprojects"),
    url(r'^approvemember/(?P<membership_id>\w+)/(?P<project_id>\d+)/$', membershipApproval, name='approvemember'),
    url(r'^invitations/$', invitations, name='invitations'),
    url(r'^incentives/$', incentives, name='incentives'),
    url(r'^membershiprejection/(?P<membership_id>\w+)/(?P<project_id>\d+)/$', membershipRejection, name='membershiprejection'),
    url(r'^projectmembers/(?P<project_id>\d+)/$', projectMembers, name="projectmembers"),
    url(r'^suspendmembership/(?P<membership_id>\d+)/$', suspendMembership, name="suspendmembership"),
    url(r'^acceptinvitation/(?P<request_id>\d+)/$', acceptInvitation, name="acceptinvitation"),
    url(r'^rejectinvitation/(?P<request_id>\d+)/$', rejectInvitation, name="rejectinvitation"),
    url(r'^removemember/(?P<membership_id>\d+)/$', removeMember, name="removemember"),
    url(r'^activatemembership/(?P<membership_id>\d+)/$', activateMembership, name="activatemembership"),
    url(r'^viewproject/(?P<project_id>\d+)/$', viewProject, name="viewproject"),
    url(r'^memberrequests/(?P<project_id>\d+)/$', memberRequest, name="memberrequest"),
    url(r'^invitemembers/(?P<project_id>\d+)/$', inviteMembers, name="invitemembers"),
    url(r'^membershipinvitation/(?P<project_id>\w+)/(?P<member_id>\d+)/$', sendInvitation, name='membershipinvitation'),
    url(r'^memberdetails/(?P<member_id>\d+)/$', viewMemberDetails, name='memberdetails'),
    url(r'^updatepersonaldetails/$', updatePersonalDetails, name="updatepersonaldetails"),
    url(r'^updateresidencedetails/$', updateResidenceDetails, name="updateresidencedetails"),
    url(r'^updatejobdetails/$', updateJobDetails, name="updatejobdetails"),
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

   #comments URLS
    url(r'^createprojectcomment/(?P<project_id>\d+)/$', createProjectComment, name="createprojectcomment"),
    url(r'^createviewpointcomment/(?P<viewpoint_id>\d+)/$', createViewpointComment, name="createviewpointcomment"),
    url(r'^goalcomment/(?P<goal_id>\d+)/$', goalComment, name="goalcomment"),
    url(r'^requirementcomment/(?P<requirement_id>\d+)/$', requirementComment, name="requirementcomment"),
    url(r'^scenariocomment/(?P<scenario_id>\d+)/$', scenarioComment, name="scenariocomment"),
    url(r'^processcomment/(?P<process_id>\d+)/$', processComment, name="processcomment"),
    url(r'^usecasecomment/(?P<usecase_id>\d+)/$', usecaseComment, name="usecasecomment"),
    
    # rating URLS
    url(r'^rateproject/(?P<project_id>\d+)/$', projectRate, name='rateproject'),
    url(r'^rateviewpoint/(?P<viewpoint_id>\d+)/$', viewpointRate, name='rateviewpoint'),
    url(r'^rategoal/(?P<goal_id>\d+)/$', goalRate, name='rategoal'),
    url(r'^raterequirement/(?P<requirement_id>\d+)/$', requirementRate, name='raterequirement'),
    url(r'^ratescenario/(?P<scenario_id>\d+)/$', scenarioRate, name='ratescenario'),
    url(r'^rateprocess/(?P<process_id>\d+)/$', processRate, name='rateprocess'),
    url(r'^rateusecase/(?P<usecase_id>\d+)/$', usecaseRate, name='rateusecase'),
    

    # From Project to usecase Resources URLS 
    url(r'^viewpointresources/(?P<viewpoint_id>\d+)/$', viewpointResources, name='viewpointresources'),
    url(r'^projectresources/(?P<project_id>\d+)/$', projectResources, name='projectresources'),
    url(r'^addprojectresources/(?P<project_id>\d+)/$', addProjectResources, name='addprojectresources'),
    url(r'^addviewpointresources/(?P<viewpoint_id>\d+)/$', addViewpointResources, name='addviewpointresources'),
    url(r'^goalresources/(?P<goal_id>\d+)/$', goalResources, name="goalresources"),
    url(r'^requirementresources/(?P<requirement_id>\d+)/$', requirementResources, name="requirementresources"),
    url(r'^scenarioresources/(?P<scenario_id>\d+)/$', scenarioResources, name="scenarioresources"),
    url(r'^processresources/(?P<process_id>\d+)/$', processResources, name="processresources"),
    url(r'^usecaseresources/(?P<usecase_id>\d+)/$', usecaseResources, name="usecaseresources"),
    url(r'^addgoalresources/(?P<goal_id>\d+)/$', addGoalResources, name="addgoalresources"),
    url(r'^addrequirementresources/(?P<requirement_id>\d+)/$', addRequirementResources, name="addrequirementresources"),
    url(r'^addscenarioresources/(?P<scenario_id>\d+)/$', addScenarioResources, name="addscenarioresources"),
    url(r'^addprocessresources/(?P<process_id>\d+)/$', addProcessResources, name="addprocessresources"),
    url(r'^addpusecaseresources/(?P<usecase_id>\d+)/$', addUsecaseResources, name="addusecaseresources"),

    path("logout", logout, name="logout"),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
