from rest_framework import routers
from rest_framework.response import Response
from django.urls import path, include
from .api import *

router = routers.DefaultRouter()
router.register('api/members', MemberViewSet, 'members')
router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/viewpoints', ViewpointViewSet, 'viewpoints')
router.register('api/goals', GoalViewSet, 'goals')
router.register('api/requirements', RequirementViewSet, 'requirements')
router.register('api/scenarios', ScenarioViewSet, 'scenarios')
router.register('api/likes', LikeViewSet, 'likes')
router.register('api/comments', CommentViewSet, 'comments')
router.register('api/dislikes', DislikeViewSet, 'dislikes')
router.register('api/starrating', StarRateViewSet, 'starrating')
router.register('api/incentives', IncentiveViewSet, 'incentives')
router.register('api/requirement-artifacts', RequirementViewSet, 'usecases')
router.register('api/repositories', RepositoryViewSet, 'repositories')
urlpatterns = router.urls
