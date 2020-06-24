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
    url(r'^addincentives/(?P<project_id>\d+)/$', add_incentive, name="addincentives"),
    url(r'^removeincentive/(?P<incentive_id>\d+)/$', remove_incentive, name="removeincentive"),
    url(r'^readnotifications/$', readNotifications, name='readnotifications'),
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


    # General links from viewpoint to usecase
    url(r'^projectgoals/(?P<project_id>\d+)/$', general_goals, name="projectgoals"),
    url(r'^projectrequirements/(?P<project_id>\d+)/$', general_requirements, name="projectrequirements"),
    url(r'^projectscenarios/(?P<project_id>\d+)/$', general_scenario, name="projectscenarios"),
    url(r'^projectprocesses/(?P<project_id>\d+)/$', general_process, name="projectprocesses"),
    url(r'^projectusecases/(?P<project_id>\d+)/$', general_usecase, name="projectusecases"),


    # VIEWPOINT URLSrequirements
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
    url(r'^processes/(?P<requirement_id>\d+)/$', processes, name="processes"),
    url(r'^viewprocess/(?P<process_id>\d+)/$', viewprocess, name="viewprocess"),
    url(r'^createprocess/(?P<requirement_id>\d+)/$', createProcess, name="createprocess"),
        # USECASE URLS
    url(r'^usecases/(?P<requirement_id>\d+)/$', usecases, name="usecases"),
    url(r'^viewusecase/(?P<usecase_id>\d+)/$', viewusecase, name="viewusecase"),
    url(r'^createusecase/(?P<requirement_id>\d+)/$', createUsecase, name="createusecase"),
    
    # Creating word docs URL
    url(r'^generatedocs/(?P<project_id>\d+)/$', create_docx, name='generatedocs'),
    url(r'^deletefile/(?P<file_id>\d+)/$', delete_file, name="deletefile"),

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
    url(r'^viewlinkresource/(?P<resource_id>\d+)/$', viewLinkResource, name='viewlinkresource'),
    url(r'^viewdocumentresource/(?P<resource_id>\d+)/$', viewDocumentResource, name='viewdocumentresource'),
    url(r'^viewimageresource/(?P<resource_id>\d+)/$', viewImageResource, name='viewimageresource'),

    # Like and dislike urls
    url(r'^myprojectlike/(?P<project_id>\d+)/$', my_project_like, name="myprojectlike"),
    url(r'^projectlike/(?P<project_id>\d+)/$', project_like, name="projectlike"),
    url(r'^viewpointlike/(?P<viewpoint_id>\d+)/$', viewpoint_like, name="viewpointlike"),
    url(r'^goallike/(?P<goal_id>\d+)/$', goal_like, name="goallike"),
    url(r'^requirementlike/(?P<requirement_id>\d+)/$', requirement_like, name="requirementlike"),
    url(r'^scenariolike/(?P<scenario_id>\d+)/$', scenario_like, name="scenariolike"),
    url(r'^processlike/(?P<process_id>\d+)/$', process_like, name="processlike"),
    url(r'^usecaselike/(?P<usecase_id>\d+)/$', usecase_like, name="usecaselike"),

    url(r'^myprojectdislike/(?P<project_id>\d+)/$', my_project_dislike, name="myprojectdislike"),   
    url(r'^projectdislike/(?P<project_id>\d+)/$', project_dislike, name="projectdislike"),
    url(r'^viewpointdislike/(?P<viewpoint_id>\d+)/$', viewpoint_dislike, name="viewpointdislike"),
    url(r'^goaldislike/(?P<goal_id>\d+)/$', goal_dislike, name="goaldislike"),
    url(r'^requirementdislike/(?P<requirement_id>\d+)/$', requirement_dislike, name="requirementdislike"),
    url(r'^scenariodislike/(?P<scenario_id>\d+)/$', scenario_dislike, name="scenariodislike"),
    url(r'^processdislike/(?P<process_id>\d+)/$', process_dislike, name="processdislike"),
    url(r'^usecasedislike/(?P<usecase_id>\d+)/$', usecase_dislike, name="usecasedislike"),

    # Reports URLS
    url(r'^generalreports/$', general_report, name='generalreports'),
    url(r'^myprojectreports/(?P<project_id>\d+)/$', my_project_reports, name='myprojectreports'),

    # update from viewpoint to usecase links
    url(r'^updateviewpoint/(?P<viewpoint_id>\d+)/$', update_viewpoint, name="updateviewpoint"),
    url(r'^updategoal/(?P<goal_id>\d+)/$', update_goal, name="updategoal"),
    url(r'^updaterequirement/(?P<requirement_id>\d+)/$', update_requirement, name="updaterequirement"),
    url(r'^updatescenario/(?P<scenario_id>\d+)/$', update_scenario, name="updatescenario"),
    url(r'^updatepeocess/(?P<process_id>\d+)/$', update_process, name="updateprocess"),
    url(r'^updateusecase/(?P<usecase_id>\d+)/$', update_usecase, name="updateusecase"),
    

    # detele form viewpoint to usecase
    url(r'^deleteviewpoint/(?P<viewpoint_id>\d+)/$', delete_viewpoint, name="deleteviewpoint"),
    url(r'^deletegoal/(?P<goal_id>\d+)/$', delete_goal, name="deletegoal"),
    url(r'^deleterequirement/(?P<requirement_id>\d+)/$', delete_requirement, name="deleterequirement"),
    url(r'^deletescenario/(?P<scenario_id>\d+)/$', delete_scenario, name="deletescenario"),
    url(r'^deleteprocess/(?P<process_id>\d+)/$', delete_process, name="deleteprocess"),
    url(r'^deleteusecase/(?P<usecase_id>\d+)/$', delete_usecase, name="deleteusecase"),
    
    path('subscribe', subscribe, name="subscribe"),

    path("logout", logout, name="logout"),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
