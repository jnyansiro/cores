from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class MemberForm(forms.ModelForm):
    class Meta:
        model: Member
        fields: "_all_"

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class ProjectForm(forms.ModelForm):
    class Meta:
        model: Project
        fields: "_all_"


class ViewPointForm(forms.ModelForm):
    class Meta:
        model: Viewpoint
        fields: "_all_"


class GoalForm(forms.ModelForm):
    class Meta:
        model: Goal
        fields: "_all_"


class RequirementForm(forms.ModelForm):
    class Meta:
        model: Requirement
        fields: "_all_"


class ScenarioForm(forms.ModelForm):
    class Meta:
        model: Scenario
        fields: "_all_"


class ProcessForm(forms.ModelForm):
    class Meta:
        model: Process
        fields: "_all_"


class UseCaseForm(forms.ModelForm):
    class Meta:
        model: UseCase
        fields: "_all_"


class CommentForm(forms.ModelForm):
    class Meta:
        model: Comment
        fields: "_all_"


class LikeForm(forms.ModelForm):
    class Meta:
        model: Like
        fields: "_all_"


class DislikeForm(forms.ModelForm):
    class Meta:
        model: Dislike
        fields: "_all_"


class RateForm(forms.ModelForm):
    class Meta:
        model: StarRate
        fields: "_all_"


class IncentivesForm(forms.ModelForm):
    class Meta:
        model: Incentive
        fields: "_all_"
