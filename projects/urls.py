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
    path('system-projects', general_projects, name="system-projects"),
    path("myprojects", myProjects, name="myprojects"),
    url(r'^addstakeholder/(?P<project_id>\d+)/$', add_stakeholder, name="addstakeholder"),
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
    url(r'^deletenotifications/$', deleteNotifications, name='deletenotifications'),
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
    url(r'^invited/$', invited, name="invited"),
    url(r'^memberdetails/(?P<member_id>\d+)/$', viewMemberDetails, name='memberdetails'),
    url(r'^updatepersonaldetails/$', updatePersonalDetails, name="updatepersonaldetails"),
    url(r'^updateresidencedetails/$', updateResidenceDetails, name="updateresidencedetails"),
    url(r'^updatejobdetails/$', updateJobDetails, name="updatejobdetails"),
    url(r'^removeprojectincentive/(?P<project_incentive_id>\d+)/$', remove_project_incentive, name="removeprojectincentive"),
    path("profile", profile, name="profile"),


    # General links from viewpoint to usecase
    url(r'^projectgoals/(?P<project_id>\d+)/$', general_goals, name="projectgoals"),
    url(r'^projectrequirements/(?P<project_id>\d+)/$', general_requirements, name="projectrequirements"),
    url(r'^projectscenarios/(?P<project_id>\d+)/$', general_scenario, name="projectscenarios"),
    url(r'^projectprocesses/(?P<project_id>\d+)/$', general_process, name="projectprocesses"),
    url(r'^projectusecases/(?P<project_id>\d+)/$', general_usecase, name="projectusecases"),


    # VIEWPOINT URLS
    url(r'^viewpoint/(?P<viewpoint_id>\d+)/$', viewPoint, name="viewpoint"),
    url(r'^associate-viewpoints/(?P<goal_id>\d+)/$', associate_viewpoints, name="associate-viewpoints"),
    url(r'^viewpoints/(?P<project_id>\d+)/$', viewpoints, name="viewpoints"),
    url(r'^createviewpoint/(?P<project_id>\d+)/$', createViewpoint, name="createviewpoint"),

        # GOAL URLS
    url(r'^goals/(?P<viewpoint_id>\d+)/$', goals, name="goals"),
    url(r'^related-goals/(?P<goal_id>\d+)/$', related_goals , name="related-goals"),
    url(r'^decomposed-goals/(?P<goal_id>\d+)/$', decomposed_goals, name="decomposed-goals"),
    url(r'^viewgoal/(?P<goal_id>\d+)/$', viewGoal, name="viewgoal"),
    url(r'^creategoal/(?P<project_id>\d+)/$', createGoal, name="creategoal"),
    url(r'^decompose-goal/$', decompose_goal, name="decompose-goal"),
    url(r'^relate-goal/$', relate_goal, name="relate-goal"),
    url(r'^associate-goal-with-viewpoint/(?P<goal_id>\d+)/$', associate_goal_with_viewpoint, name="associate-goal-with-viewpoint"),


        # REQUIREMENT URLS
    url(r'^requirements/(?P<goal_id>\d+)/$', requirements, name="requirements"),
    url(r'^viewrequirement/(?P<requirement_id>\d+)/$', viewrequirement, name="viewrequirement"),
    url(r'^createrequirement/(?P<project_id>\d+)/$', createRequirement, name="createrequirement"),
    url(r'^scenariorequirement/(?P<scenario_id>\d+)/$', scenario_requirement, name="scenariorequirement"),
    url(r'^processrequirements/(?P<process_id>\d+)/$', process_requirements, name="processrequirements"),
    url(r'^usecaserequirements/(?P<usecase_id>\d+)/$', usecase_requirements, name="usecaserequirements"),
    url(r'^requirementgoals/(?P<requirement_id>\d+)/$', requirementgoals, name="requirementgoals"),

        # SCENARIO URLS
    url(r'^scenarios/(?P<requirement_id>\d+)/$', scenarios, name='scenarios'),
    url(r'^viewscenario/(?P<scenario_id>\d+)/$', viewscenario, name='viewscenario'),
    url(r'^createscenario/(?P<project_id>\d+)/$', createScenario, name='createscenario'),
    
        # PROCESS URLS

    url(r'^processes/(?P<requirement_id>\d+)/$', processes, name="processes"),
    url(r'^viewprocess/(?P<process_id>\d+)/$', viewprocess, name="viewprocess"),
    url(r'^createprocess/(?P<project_id>\d+)/$', createProcess, name="createprocess"),

        # USECASE URLS
    url(r'^usecases/(?P<requirement_id>\d+)/$', usecases, name="usecases"),
    url(r'^viewusecase/(?P<usecase_id>\d+)/$', viewusecase, name="viewusecase"),
    url(r'^createusecase/(?P<project_id>\d+)/$', createUsecase, name="createusecase"),
    
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
    url(r'^like/(?P<module_id>\d+)/$', like, name="like"),
    url(r'^dislike/(?P<module_id>\d+)/$', dislike, name="dislike"),


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

    #approval of contributions URLS
    url(r'^projectcontributions/(?P<project_id>\d+)/$', project_contributions, name="projectcontributions"),
    url(r'^viewpointcontributions/(?P<project_id>\d+)/$',viewpoint_contributions, name="viewpointcontributions"),
    url(r'^goalcontributions/(?P<project_id>\d+)/$',goal_contributions, name="goalcontributions"),
    url(r'^requirementcontributions/(?P<project_id>\d+)/$',requirement_contributions, name="requirementcontributions"),
    url(r'^scenariocontributions/(?P<project_id>\d+)/$',scenario_contributions, name="scenariocontributions"),
    url(r'^processcontributions/(?P<project_id>\d+)/$',process_contributions, name="processcontributions"),
    url(r'^usecasecontributions/(?P<project_id>\d+)/$',usecase_contributions, name="usecasecontributions"),
    url(r'^approveviewpoint/(?P<viewpoint_id>\d+)/$', approve_viewpoint, name="approveviewpoint"),
#  for all comments approval and rejection
    url(r'^bulk-approval-project-comments/$', bulk_approve_project_comments, name="bulk-approval-project-comments"),
    # end

    url(r'^bulk-approval-viewpoint/$', bulk_approve_viewpoint, name="bulk-approval-viewpoint"),
    url(r'^bulk-approval-goal/$', bulk_approve_goal, name="bulk-approval-goal"),
    url(r'^bulk-approval-requirement/$', bulk_approve_requirement, name="bulk-approval-requirement"),
    url(r'^bulk-approval-scenario/$', bulk_approve_scenario, name="bulk-approval-scenario"),
    url(r'^bulk-approval-process/$', bulk_approve_process, name="bulk-approval-process"),
    url(r'^bulk-approval-usecase/$', bulk_approve_usecase, name="bulk-approval-usecase"),
    url(r'^approvegoal/(?P<goal_id>\d+)/$', approve_goal, name="approvegoal"),
    url(r'^approverequirement/(?P<requirement_id>\d+)/$', approve_requirement, name="approverequirement"),
    url(r'^approvescenario/(?P<scenario_id>\d+)/$', approve_scenario, name="approvescenario"),
    url(r'^approveprocess/(?P<process_id>\d+)/$', approve_process, name="approveprocess"),
    url(r'^approveusecase/(?P<usecase_id>\d+)/$', approve_usecase, name="approveusecase"),
    url(r'^approveprojectcomment/(?P<comment_id>\d+)/$', approve_project_comment, name="approveprojectcomment"),
    url(r'^approveviewpointcomment/(?P<comment_id>\d+)/$', approve_viewpoint_comment, name="approveviewpointcomment"),
    url(r'^approvegoalcomment/(?P<comment_id>\d+)/$', approve_goal_comment, name="approvegoalcomment"),
    url(r'^approverequirementcomment/(?P<comment_id>\d+)/$', approve_requirement_comment, name="approverequirementcomment"),
    url(r'^approvescenariocomment/(?P<comment_id>\d+)/$', approve_scenario_comment, name="approvescenariocomment"),
    url(r'^approveprocesscomment/(?P<comment_id>\d+)/$', approve_process_comment, name="approveprocesscomment"),
    url(r'^approveusecasecomment/(?P<comment_id>\d+)/$', approve_usecase_comment, name="approveusecasecomment"),
        

    #Reject contributions URLS
    url(r'^rejectviewpoint/(?P<viewpoint_id>\d+)/$', reject_viewpoint, name="rejectviewpoint"),
    url(r'^rejectgoal/(?P<goal_id>\d+)/$', reject_goal, name="rejectgoal"),
    url(r'^rejectrequirement/(?P<requirement_id>\d+)/$', reject_requirement, name="rejectrequirement"),
    url(r'^rejectscenario/(?P<scenario_id>\d+)/$', reject_scenario, name="rejectscenario"),
    url(r'^rejectprocess/(?P<process_id>\d+)/$', reject_process, name="rejectprocess"),
    url(r'^rejectusecase/(?P<usecase_id>\d+)/$', reject_usecase, name="rejectusecase"),
    url(r'^rejectprojectcomment/(?P<comment_id>\d+)/$', reject_project_comment, name="rejectprojectcomment"),
    url(r'^rejectviewpointcomment/(?P<comment_id>\d+)/$', reject_viewpoint_comment, name="rejectviewpointcomment"),
    url(r'^rejectgoalcomment/(?P<comment_id>\d+)/$', reject_goal_comment, name="rejectgoalcomment"),
    url(r'^rejectrequirementcomment/(?P<comment_id>\d+)/$', reject_requirement_comment, name="rejectrequirementcomment"),
    url(r'^rejectscenariocomment/(?P<comment_id>\d+)/$', reject_scenario_comment, name="rejectscenariocomment"),
    url(r'^rejectprocesscomment/(?P<comment_id>\d+)/$', reject_process_comment, name="rejectprocesscomment"),
    url(r'^rejectusecasecomment/(?P<comment_id>\d+)/$', reject_usecase_comment, name="rejectusecasecomment"),



    #Block contributions URLS
    url(r'^blockviewpoint/(?P<viewpoint_id>\d+)/$', block_viewpoint, name="blockviewpoint"),
    url(r'^blockgoal/(?P<goal_id>\d+)/$', block_goal, name="blockgoal"),
    url(r'^blockrequirement/(?P<requirement_id>\d+)/$', block_requirement, name="blockrequirement"),
    url(r'^blockscenario/(?P<scenario_id>\d+)/$', block_scenario, name="blockscenario"),
    url(r'^blockprocess/(?P<process_id>\d+)/$', block_process, name="blockprocess"),
    url(r'^blockusecase/(?P<usecase_id>\d+)/$', block_usecase, name="blockusecase"),
    url(r'^deletestakeholder/(?P<stakeholder_id>\d+)/$', delete_stakeholder, name="deletestakeholder"),
    url(r'^updatestakeholder/(?P<stakeholder_id>\d+)/$', update_stakeholder, name="updatestakeholder"),

    # Associations URLS

    url(r'^associate-goal-with-requirement/(?P<goal_id>\d+)/$', associate_goal_with_requirement, name='associate-goal-with-requirement'),
    url(r'^associate-requirement-with-goal/(?P<requirement_id>\d+)/$', associate_requirement_with_goal, name='associate-requirement-with-goal'),
    url(r'^associate-requirement-with-scenario/(?P<requirement_id>\d+)/$', associate_requirement_with_scenario, name='associate-requirement-with-scenario'),
    url(r'^associate-requirement-with-process/(?P<requirement_id>\d+)/$', associate_requirement_with_process, name='associate-requirement-with-process'),
    url(r'^associate-requirement-with-usecase/(?P<requirement_id>\d+)/$', associate_requirement_with_usecase, name='associate-requirement-with-usecase'),
    url(r'^associate-scenario-with-requirement/(?P<scenario_id>\d+)/$', associate_scenario_with_requirement, name='associate-scenario-with-requirement'),
    url(r'^associate-scenario-with-process/(?P<scenario_id>\d+)/$', associate_scenario_with_process, name='associate-scenario-with-process'),
    url(r'^associate-scenario-with-usecase/(?P<scenario_id>\d+)/$', associate_scenario_with_usecase, name='associate-scenario-with-usecase'),
    url(r'^associate-process-with-requirement/(?P<process_id>\d+)/$', associate_process_with_requirement, name='associate-process-with-requirement'),
    url(r'^associate-process-with-scenario/(?P<process_id>\d+)/$', associate_process_with_scenario, name='associate-process-with-scenario'),
    url(r'^associate-process-with-usecase/(?P<process_id>\d+)/$', associate_process_with_usecase, name='associate-process-with-usecase'),
    url(r'^associate-usecase-with-requirement/(?P<usecase_id>\d+)/$', associate_usecase_with_requirement, name='associate-usecase-with-requirement'),
    url(r'^associate-usecase-with-scenario/(?P<usecase_id>\d+)/$', associate_usecase_with_scenario, name='associate-usecase-with-scenario'),
    url(r'^associate-usecase-with-process/(?P<usecase_id>\d+)/$', associate_usecase_with_process, name='associate-usecase-with-process'),


    # associated URLS
    url(r'^associated-scenario-processes/(?P<scenario_id>\d+)/$', scenario_process, name='associated-scenario-process'),
    url(r'^associated-scenario-usecases/(?P<scenario_id>\d+)/$', scenario_usecase, name='associated-scenario-usecase'),
    url(r'^associated-process-scenarios/(?P<process_id>\d+)/$', process_scenario, name='associated-process-scenarios'),
    url(r'^associated-process-usecases/(?P<process_id>\d+)/$', process_usecase, name='associated-process-usecases'),
    url(r'^associated-usecase-scenario/(?P<usecase_id>\d+)/$', usecase_scenario, name='associated-usecase-scenario'),
    url(r'^associated-usecase-process/(?P<usecase_id>\d+)/$', usecase_process, name='associated-usecase-process'),

    #dissociation URLS
    url(r'^dissociate_goal_with_viewpoint/(?P<association_id>\d+)/$', delete_goal_association_with_viewpoint, name='dissociate_goal_with_viewpoint'),
    url(r'^dissociate_goal_with_requirement/(?P<association_id>\d+)/$', delete_goal_association_with_requirement, name='dissociate_goal_with_requirement'),
    url(r'^delete_decomposition_with_goal/(?P<goal_id>\d+)/$', delete_decomposition_with_goal, name='delete_decomposition_with_goal'),
    url(r'^delete_relationship_with_goal/(?P<goal_id>\d+)/$', delete_relationship_with_goal, name='delete_relationship_with_goal'),
    url(r'^dissociate_requirement_with_goal/(?P<association_id>\d+)/$', delete_requirement_association_with_goal, name='dissociate_requirement_with_goal'),
    url(r'^dissociate_requirement_with_scenario/(?P<association_id>\d+)/$', delete_requirement_association_with_scenario, name='dissociate_requirement_with_scenario'),
    url(r'^dissociate_requirement_with_process/(?P<association_id>\d+)/$', delete_requirement_association_with_process, name='dissociate_requirement_with_process'),
    url(r'^dissociate_requirement_with_usecase/(?P<association_id>\d+)/$', delete_requirement_association_with_usecase, name='dissociate_requirement_with_usecase'),
    url(r'^dissociate_scenario_with_requirement/(?P<association_id>\d+)/$', delete_scenario_association_with_requirement, name='dissociate_scenario_with_requirement'),
    url(r'^dissociate_scenario_with_process/(?P<association_id>\d+)/$', delete_scenario_association_with_process, name='dissociate_scenario_with_process'),
    url(r'^dissociate_scenario_with_usecase/(?P<association_id>\d+)/$', delete_scenario_association_with_usecase, name='dissociate_scenario_with_usecase'),
    url(r'^dissociate_process_with_requirement/(?P<association_id>\d+)/$', delete_process_association_with_requirement, name='dissociate_process_with_requirement'),
    url(r'^dissociate_process_with_scenario/(?P<association_id>\d+)/$', delete_process_association_with_scenario, name='dissociate_process_with_scenario'),
    url(r'^dissociate_process_with_usecase/(?P<association_id>\d+)/$', delete_process_association_with_usecase, name='dissociate_process_with_usecase'),
    url(r'^dissociate_usecase_with_requirement/(?P<association_id>\d+)/$', delete_usecase_association_with_requirement, name='dissociate_usecase_with_requirement'),
    url(r'^dissociate_usecase_with_scenario/(?P<association_id>\d+)/$', delete_usecase_association_with_scenario, name='dissociate_usecase_with_scenario'),
    url(r'^dissociate_usecase_with_process/(?P<association_id>\d+)/$', delete_usecase_association_with_process, name='dissociate_usecase_with_process'),
    
    
    

    
    path('subscribe', subscribe, name="subscribe"),

    path("logout", logout, name="logout"),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
