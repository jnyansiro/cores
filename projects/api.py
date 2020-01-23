from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from .serializers import *
from .models import *

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MemberSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectSerializer


class ViewpointViewSet(viewsets.ModelViewSet):
    queryset = Viewpoint.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ViewpointSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = GoalSerializer


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RequirementSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ScenarioSerializer


class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProcessSerializer


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UseCaseSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LikeSerializer


class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DislikeSerializer


class StarRateViewSet(viewsets.ModelViewSet):
    queryset = StarRate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StarRateSerializer


class RequirementArtifactViewSet(viewsets.ModelViewSet):
    queryset = RequirementArtifact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RequirementArtifactSerializer


class IncentiveViewSet(viewsets.ModelViewSet):
    queryset = Incentive.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = IncentiveSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = RepositorySerializer
