from rest_framework import serializers
from .models import *


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ViewpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewpoint
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = "__all__"


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"


class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = "__all__"


class StarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarRate
        fields = "__all__"


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"


class RequirementArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementArtifact
        fields = "__all__"


class IncentiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentive
        fields = "__all__"


class ProjectMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = "__all__"


class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = "__all__"


class ViewpointCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPointComment
        fields = "__all__"


class GoalCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalComment
        fields = "__all__"


class RequirementCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementComment
        fields = "__all__"


class ScenarioCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioComment
        fields = "__all__"


class ProcessCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessComment
        fields = "__all__"


class UseCaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseComment
        fields = "__all__"


class RequirementArtifactCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactComment
        fields = "__all__"


class ProjectLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLike
        fields = "__all__"


class ProjectLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectLike
        fields = "__all__"


class ViewpointLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewpointLike
        fields = "__all__"


class GoalLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalLike
        fields = "__all__"


class RequirementLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementLike
        fields = "__all__"


class ScenarioLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioLike
        fields = "__all__"


class ProcessLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessLike
        fields = "__all__"


class UseCaseLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseLike
        fields = "__all__"


class RequirementArtifactLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementArtifactLike
        fields = "__all__"


class ProjectDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDislike
        fields = "__all__"


class ViewpointDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewpointDislike
        fields = "__all__"


class GoalDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalDislike
        fields = "__all__"


class RequirementDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementDislike
        fields = "__all__"


class RequirementArtifactDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementArtifactDislike
        fields = "__all__"


class ScenarioDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioDislike
        fields = "__all__"


class ProcessDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessDislike
        fields = "__all__"


class UseCaseDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseDislike
        fields = "__all__"


class ProjectRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRate
        fields = "__all__"


class ViewpointRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewPointRate
        fields = "__all__"


class RequirementRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementRate
        fields = "__all__"


class ScenarioRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScenarioRate
        fields = "__all__"


class GoalRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalRate
        fields = "__all__"


class ProcessRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessRate
        fields = "__all__"


class UseCaseRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseRate
        fields = "__all__"


class RequirementArtifactRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementArtifactRate
        fields = "__all__"
