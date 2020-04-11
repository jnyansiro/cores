from rest_framework import routers
from rest_framework.response import Response
from django.urls import path, include
from .api import *
from .views import *

# router = routers.DefaultRouter()
# router.register('api/members', MemberViewSet, 'members')
# router.register('api/projects', ProjectViewSet, 'projects')
# router.register('api/viewpoints', ViewpointViewSet, 'viewpoints')
# router.register('api/goals', GoalViewSet, 'goals')
# router.register('api/requirements', RequirementViewSet, 'requirements')
# router.register('api/scenarios', ScenarioViewSet, 'scenarios')
# router.register('api/likes', LikeViewSet, 'likes')
# router.register('api/comments', CommentViewSet, 'comments')
# router.register('api/dislikes', DislikeViewSet, 'dislikes')
# router.register('api/starrating', StarRateViewSet, 'starrating')
# router.register('api/incentives', IncentiveViewSet, 'incentives')
# router.register('api/requirement-artifacts', RequirementArtifactViewSet, 'requirement-artifact')
# router.register('api/projectcomments', ProjectCommentViewSet, 'projectcomments')
# router.register('api/viewpointcomments', ViewPointCommentViewSet, 'viewpointcomments')
# router.register('api/goalcomments', GoalCommentViewSet, 'goalcomments')
# router.register('api/requirementcomments', RequirementCommentViewSet, 'requirementcomments')
# router.register('api/scenariocomments', ScenarioCommentViewSet, 'scenariocomments')
# router.register('api/processcomments', ProcessCommentViewSet, 'processcomments')
# router.register('api/usecasecomments', UseCaseCommentViewSet, 'usecasecomments')
# router.register('api/artifactcomments', ArtifactCommentViewSet, 'artifactcomments')
# router.register('api/projectlikes', ProjectLikeViewSet, 'projectlikes')
# router.register('api/viewpointlikes', ViewpointLikeViewSet, 'viewpointlikes')
# router.register('api/goallikes', GoalLikeViewSet, 'goallikes')
# router.register('api/requirementlikess', RequirementLikeViewSet, 'requirementlikes')
# router.register('api/scenariolikes', ScenarioLikeViewSet, 'scenariolikes')
# router.register('api/processlikes', ProcessLikeViewSet, 'processlikes')
# router.register('api/usecaselikes', UseCaseLikeViewSet, 'usecaselikes')
# router.register('api/artifactlikes', RequirementArtifactLikeViewSet, 'artifactlikes')
# router.register('api/projectdislikes', ProjectDislikeViewSet, 'projectdislikes')
# router.register('api/viewpointdislikes', ViewpointDislikeViewSet, 'viewpointdislikes')
# router.register('api/goaldislikes', GoalDislikeViewSet, 'goaldislikes')
# router.register('api/requirementdislikes', RequirementDislikeViewSet, 'requrementdislikes')
# router.register('api/scenariodislikes', ScenarioDislikeViewSet, 'scenariodislikes')
# router.register('api/processdislikes', ProcessDislikeViewSet, 'Procestdislikes')
# router.register('api/usecasedislikes', UseCaseDislikeViewSet, 'usecasedislikes')
# router.register('api/artifactdislikes', RequirementArtifactDislikeViewSet, 'artifactdislikes')
# router.register('api/Projectrates', ProjectRateViewSet, 'projectrates')
# router.register('api/viewpointrates', ViewpointRateViewSet, 'viewpointrates')
# router.register('api/goalrates', RequirementRateViewSet, 'requiremetrates')
# router.register('api/scenariorates', ScenarioRateViewSet, 'scenariorates')
# router.register('api/processrates', ProcessRateViewSet, 'processrates')
# router.register('api/artifactrates', RequirementArtifactRateViewSet, 'artifactrates')
# router.register('api/usecaserates', UseCaseRateViewSet, 'usecaserates')
# router.register('api/projects_view', View_ProjectMembersViewset, 'projects-view')
# # router.register('api/goalrate', GoalRateViewSet, 'goalrates')

# urlpatterns = router.urls

app_name = "projects"
urlpatterns = [
    path("createproject", createProject, name="createproject"),
    path("myprojects", myProjects, name="myprojects"),
    path("projects", projects, name="projects"),
    path('projectmembers', projectMembers, name="projectmembers"),
    path('memberrequests', memberRequest, name="memberrequest"),
    path('logout', logout, name="logout")
]
