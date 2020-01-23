from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
            model = Member
            fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class ViewpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewpoint
        fields = '__all__'

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = '__all__'

class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'


class StarRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarRate
        fields = '__all__'


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'


class RequirementArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementArtifact
        fields = '__all__'


class IncentiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentive
        fields = '__all__'

class ProjectMembershpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMembership
        fields = '__all__'a