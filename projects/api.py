from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from .serializers import *
from .models import *


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MemberSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


class ViewpointViewSet(viewsets.ModelViewSet):
    queryset = Viewpoint.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewpointSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalSerializer


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScenarioSerializer


class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcessSerializer


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UseCaseSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CommentSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LikeSerializer


class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DislikeSerializer


class StarRateViewSet(viewsets.ModelViewSet):
    queryset = StarRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = StarRateSerializer


class RequirementArtifactViewSet(viewsets.ModelViewSet):
    queryset = RequirementArtifact.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementArtifactSerializer


class IncentiveViewSet(viewsets.ModelViewSet):
    queryset = Incentive.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = IncentiveSerializer


class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RepositorySerializer


class ProjectCommentViewSet(viewsets.ModelViewSet):
    queryset = ProjectComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectCommentSerializer


class ViewPointCommentViewSet(viewsets.ModelViewSet):
    queryset = ViewPointComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewpointCommentSerializer


class GoalCommentViewSet(viewsets.ModelViewSet):
    queryset = GoalComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalCommentSerializer


class RequirementCommentViewSet(viewsets.ModelViewSet):
    queryset = RequirementComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementCommentSerializer


class ScenarioCommentViewSet(viewsets.ModelViewSet):
    queryset = ScenarioComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScenarioCommentSerializer


class ProcessCommentViewSet(viewsets.ModelViewSet):
    queryset = ProcessComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcessCommentSerializer


class UseCaseCommentViewSet(viewsets.ModelViewSet):
    queryset = UseCaseComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UseCaseCommentSerializer


class ArtifactCommentViewSet(viewsets.ModelViewSet):
    queryset = ArtifactComment.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementArtifactCommentSerializer


class ProjectLikeViewSet(viewsets.ModelViewSet):
    queryset = ProjectLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectLikeSerializer


class ViewpointLikeViewSet(viewsets.ModelViewSet):
    queryset = ViewpointLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewpointLikeSerializer


class GoalLikeViewSet(viewsets.ModelViewSet):
    queryset = GoalLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalLikeSerializer


class RequirementLikeViewSet(viewsets.ModelViewSet):
    queryset = RequirementLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementLikeSerializer


class ScenarioLikeViewSet(viewsets.ModelViewSet):
    queryset = ScenarioLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScenarioLikeSerializer


class UseCaseLikeViewSet(viewsets.ModelViewSet):
    queryset = UseCaseLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UseCaseLikeSerializer


class ProcessLikeViewSet(viewsets.ModelViewSet):
    queryset = ProcessLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcessLikeSerializer


class RequirementArtifactLikeViewSet(viewsets.ModelViewSet):
    queryset = RequirementArtifactLike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementArtifactLikeSerializer


class ProjectDislikeViewSet(viewsets.ModelViewSet):
    queryset = ProjectDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectDislikeSerializer


class ViewpointDislikeViewSet(viewsets.ModelViewSet):
    queryset = ViewpointDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewpointDislikeSerializer


class GoalDislikeViewSet(viewsets.ModelViewSet):
    queryset = GoalDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalDislikeSerializer


class RequirementDislikeViewSet(viewsets.ModelViewSet):
    queryset = RequirementDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementDislikeSerializer


class ScenarioDislikeViewSet(viewsets.ModelViewSet):
    queryset = ScenarioDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScenarioDislikeSerializer


class ProcessDislikeViewSet(viewsets.ModelViewSet):
    queryset = ProcessDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcessDislikeSerializer


class UseCaseDislikeViewSet(viewsets.ModelViewSet):
    queryset = UseCaseDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UseCaseDislikeSerializer


class RequirementArtifactDislikeViewSet(viewsets.ModelViewSet):
    queryset = RequirementArtifactDislike.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementArtifactDislikeSerializer


class ProjectRateViewSet(viewsets.ModelViewSet):
    queryset = ProjectRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectRateSerializer


class RequirementRateViewSet(viewsets.ModelViewSet):
    queryset = RequirementRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementRateSerializer


class ViewpointRateViewSet(viewsets.ModelViewSet):
    queryset = ViewPointRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ViewpointRateSerializer


class GoalRateViewSet(viewsets.ModelViewSet):
    queryset = GoalRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = GoalRateSerializer


class ScenarioRateViewSet(viewsets.ModelViewSet):
    queryset = ScenarioRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ScenarioRateSerializer


class ProcessRateViewSet(viewsets.ModelViewSet):
    queryset = ProcessRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProcessRateSerializer


class UseCaseRateViewSet(viewsets.ModelViewSet):
    queryset = UseCaseRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UseCaseRateSerializer


class RequirementArtifactRateViewSet(viewsets.ModelViewSet):
    queryset = RequirementArtifactRate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RequirementArtifactRateSerializer


class View_ProjectMembersViewset(viewsets.ModelViewSet):
    queryset = ProjectMembership.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectMembershipSerializer
