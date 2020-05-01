from django.db import models
from django.apps import apps
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date, timedelta
from django.apps import apps
from django.conf import settings
import requests
from django.conf import settings
from datetime import timezone
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email=None, username=None, password=None):
        user = self.model(
            email=self.normalize_email(email), password=password, username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username=None, password=None):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["username", "password"]

    objects = UserManager()

    def __str__(self):
        return self.username


class LoginLog(models.Model):
    """Model definition for LoginLog."""

    # TODO: Define fields here
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for LoginLog."""

        verbose_name = "LoginLog"
        verbose_name_plural = "LoginLogs"

    def __str__(self):
        """Unicode representation of LoginLog."""
        return self.login_time


class ActivityLog(models.Model):
    """Model definition for ActivityLog."""

    # TODO: Define fields here
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    activity = models.CharField(max_length=500)
    activity_time = models.DateTimeField(auto_now=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ActivityLog."""

        verbose_name = "ActivityLog"
        verbose_name_plural = "ActivityLogs"

    def __str__(self):
        """Unicode representation of ActivityLog."""
        return self.activity

class Sector(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    sector_name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Unicode representation of ActivityLog."""
        return self.sector_name


class Member(models.Model):
    """Model definition for Member."""

    # TODO: Define fields here
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50) 
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField(auto_now=False,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=34, blank=True)
    job_email = models.EmailField(max_length=34, blank=True)
    country = models.CharField(max_length=50, blank=True,default="Tanzania")
    region = models.CharField(max_length=260, blank=True,null=True)
    district = models.CharField(max_length=260, blank=True,null=True)
    professional = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    institution_name = models.CharField(max_length=50, blank=True)
    profile_photo = models.ImageField(max_length=50, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    update_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Member."""

        verbose_name = "Member"
        verbose_name_plural = "Members"

    @property
    def full_name(self):
        return self.first_name + " " + self.middle_name + " " + self.surname
    def __str__(self):
        return self.full_name


class Project(models.Model):
    """Model definition for Project."""

    # TODO: Define fields here
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    project_title = models.CharField(max_length=50)
    project_photo = models.ImageField(max_length=50,blank=True,null=True)
    project_files = models.FileField(max_length=50,blank=True,null=True)
    description = models.CharField(max_length=5000,null=True,blank=True)
    due_date = models.DateTimeField(auto_now=False)
    project_visibility = models.CharField(max_length=40,null=True,blank=True)
    is_public = models.BooleanField(default=False)
    is_invitational = models.BooleanField(default=False)
    is_discoverable = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Project."""

        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        """Unicode representation of Project."""
        return self.project_title

class ProjectSector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Unicode representation of ActivityLog."""
        return self.id



class Incentive(models.Model):
    """Model definition for Incentive."""

    # TODO: Define fields here
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    incentive_type = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Incentive."""

        verbose_name = "Incentive"
        verbose_name_plural = "Incentives"

    def __str__(self):
        """Unicode representation of Incentive."""
        return self.incentive_type


class ProjectIncentive(models.Model):
    """Model definition for ProjectIncentive."""

    # TODO: Define fields here
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    incentive = models.ForeignKey("Incentive", on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, blank=True, null=True)
    amount = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectIncentive."""

        verbose_name = "ProjectIncentive"
        verbose_name_plural = "ProjectIncentives"

    def __str__(self):
        """Unicode representation of ProjectIncentive."""
        return self.amount


class ProjectMembership(models.Model):
    """Model definition for ProjectMembership."""

    # TODO: Define fields here
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    member_role = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectMembership."""

        verbose_name = "ProjectMembership"
        verbose_name_plural = "ProjectMemberships"

    def __str__(self):
        """Unicode representation of ProjectMembership."""
        return self.project.project_title


class Viewpoint(models.Model):
    """Model definition for Viewpoint."""

    # TODO: Define fields here
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE)
    viewpoint_name = models.CharField(max_length=50)
    viewpoint_links= models.CharField(max_length=600,blank=True,null=True)
    viewpoint_photo = models.ImageField(blank=True,null=True)
    viewpoint_docs = models.FileField(max_length=500,blank=True,null=True)
    description = models.CharField(max_length=2300)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Viewpoint."""

        verbose_name = "Viewpoint"
        verbose_name_plural = "Viewpoints"

    def __str__(self):
        """Unicode representation of Viewpoint."""
        return self.viewpoint_name


class Goal(models.Model):
    """Model definition for Goal."""

    # TODO: Define fields here
    viewpoint = models.ForeignKey("Viewpoint", on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=50)
    goal_photo = models.ImageField(blank=True,null=True)
    goal_link = models.CharField(max_length=50,blank=True,null=True)
    goal_docs = models.FileField(blank=True,null=True)
    description = models.CharField(max_length=2300, null=True, blank=True)
    category = models.CharField(max_length=50,null=True)  # example comflict
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Goal."""

        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        """Unicode representation of Goal."""
        return self.goal_name


class Requirement(models.Model):
    """Model definition for Requirement."""

    # TODO: Define fields here
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    requirement_photo = models.ImageField(blank=True,null=True)
    requirement_docs = models.FileField(max_length=500,blank=True,null=True)
    description = models.CharField(max_length=2500 ,null=True, blank=True)
    requirement_links = models.CharField(max_length=50,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Requirement."""

        verbose_name = "Requirement"
        verbose_name_plural = "Requirements"

    def __str__(self):
        """Unicode representation of Requirement."""
        return self.name


class Scenario(models.Model):
    """Model definition for Scenario."""

    # TODO: Define fields here
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    scenario_photo = models.ImageField(blank=True,null=True)
    scenario_docs = models.FileField(blank=True,null=True)
    scenario_links = models.CharField(max_length=1500,blank=True, null=True)
    description = models.CharField(max_length=1500)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Scenario."""

        verbose_name = "Scenario"
        verbose_name_plural = "Scenarios"

    def __str__(self):
        """Unicode representation of Scenario."""
        return self.name


class Process(models.Model):
    """Model definition for Process."""

    # TODO: Define fields here
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    process_name = models.CharField(max_length=60)
    process_links = models.CharField(max_length=500, blank=True, null=True)
    process_photo = models.ImageField(blank=True,null=True)
    process_docs = models.FileField(max_length=500,blank=True,null=True)
    description = models.CharField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Process."""

        verbose_name = "Process"
        verbose_name_plural = "Processs"

    def __str__(self):
        """Unicode representation of Process."""
        return self.process_name


class UseCase(models.Model):
    """Model definition for UseCase."""

    # TODO: Define fields here
    usecase_name = models.CharField(max_length=50)
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    usecase_link = models.CharField(max_length=500)
    usecase_photo = models.ImageField(blank=True,null=True)
    usecase_docs = models.FileField(max_length=500,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UseCase."""

        verbose_name = "UseCase"
        verbose_name_plural = "UseCases"

    def __str__(self):
        """Unicode representation of UseCase."""
        return self.usecase_name


class Repository(models.Model):
    """Model definition for Repository."""

    # TODO: Define fields here
    added_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    resource_name = models.CharField(max_length=500)
    resource_type = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Repository."""

        verbose_name = "Repository"
        verbose_name_plural = "Repositorys"

    def __str__(self):
        """Unicode representation of Repository."""
        return self.resource_name


class Comment(models.Model):
    """Model definition for Comment."""

    # TODO: Define fields here
    commented_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    comment = models.CharField(max_length=2500)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Comment."""

        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.comment


class RequirementArtifact(models.Model):
    """Model definition for RequirementArtifact."""

    # TODO: Define fields here
    created_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    artifact_type = models.CharField(max_length=50)
    artifact_content = models.CharField(max_length=500)
    artifact_link = models.CharField(max_length=200, null=True, blank=True)
    uploaded_file = models.FileField(max_length=50,blank=True,null=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementArtifact."""

        verbose_name = "RequirementArtifact"
        verbose_name_plural = "RequirementArtifacts"

    def __str__(self):
        return self.artifact_content


class StarRate(models.Model):
    """Model definition for StarRate."""

    # TODO: Define fields here
    rated_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    number_of_stars = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for StarRate."""

        verbose_name = "StarRate"
        verbose_name_plural = "StarRates"

    def __str__(self):
        """Unicode representation of StarRate."""
        return self.number_of_stars


class Like(models.Model):
    """Model definition for Like."""

    # TODO: Define fields here
    liked_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Like."""

        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        """Unicode representation of Like."""
        return self.liked_by


class Dislike(models.Model):
    """Model definition for Dislike."""

    # TODO: Define fields here
    disliked_by = models.ForeignKey("Member", on_delete=models.CASCADE)
    dislike = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Dislike."""

        verbose_name = "Dislike"
        verbose_name_plural = "Dislikes"

    def __str__(self):
        """Unicode representation of Dislike."""
        return self.dislike


class ProjectComment(models.Model):
    """Model definition for ProjectComment."""

    # TODO: Define fields here
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectComment."""

        verbose_name = "ProjectComment"
        verbose_name_plural = "ProjectComments"

    def __str__(self):
        """Unicode representation of ProjectComment."""
        pass


class ArtifactComment(models.Model):
    """Model definition for ArtifactComment."""

    # TODO: Define fields here
    requirement_artifact = models.ForeignKey(
        "RequirementArtifact", on_delete=models.CASCADE
    )
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ArtifactComment."""

        verbose_name = "ArtifactComment"
        verbose_name_plural = "ArtifactComments"

    def __str__(self):
        """Unicode representation of ArtifactComment."""
        pass


class ViewPointComment(models.Model):
    """Model definition for ViewPointComment."""

    # TODO: Define fields here
    viewpoint = models.ForeignKey("Viewpoint", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ViewPointComment."""

        verbose_name = "ViewPointComment"
        verbose_name_plural = "ViewPointComments"

    def __str__(self):
        """Unicode representation of ViewPointComment."""
        pass


class GoalComment(models.Model):
    """Model definition for GoalComment."""

    # TODO: Define fields here
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GoalComment."""

        verbose_name = "GoalComment"
        verbose_name_plural = "GoalComments"

    def __str__(self):
        """Unicode representation of GoalComment."""
        pass


class RequirementComment(models.Model):
    """Model definition for RequirementComment."""

    # TODO: Define fields here
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementComment."""

        verbose_name = "RequirementComment"
        verbose_name_plural = "RequirementComments"

    def __str__(self):
        """Unicode representation of RequirementComment."""
        pass


class ScenarioComment(models.Model):
    """Model definition for ScenarioComment."""

    # TODO: Define fields here
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ScenarioComment."""

        verbose_name = "ScenarioComment"
        verbose_name_plural = "ScenarioComments"

    def __str__(self):
        """Unicode representation of ScenarioComment."""
        pass


class ProcessComment(models.Model):
    """Model definition for ProcessComment."""

    # TODO: Define fields here
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProcessComment."""

        verbose_name = "ProcessComment"
        verbose_name_plural = "ProcessComments"

    def __str__(self):
        """Unicode representation of ProcessComment."""
        pass


class UseCaseComment(models.Model):
    """Model definition for UseCaseComment."""

    # TODO: Define fields here
    usecase = models.ForeignKey("UseCase", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UseCaseComment."""

        verbose_name = "UseCaseComment"
        verbose_name_plural = "UseCaseComments"

    def __str__(self):
        """Unicode representation of UseCaseComment."""
        pass


class ProjectRate(models.Model):
    """Model definition for ProjectRate."""

    # TODO: Define fields here
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectRate."""

        verbose_name = "ProjectRate"
        verbose_name_plural = "ProjectRates"

    def __str__(self):
        """Unicode representation of ProjectRate."""
        pass


class RequirementArtifactRate(models.Model):
    """Model definition for RequirementArtifactRate."""

    # TODO: Define fields here
    requiremet_artifact = models.ForeignKey(
        "RequirementArtifact", on_delete=models.CASCADE
    )
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementArtifactRate."""

        verbose_name = "RequirementArtifactRate"
        verbose_name_plural = "RequirementArtifactRates"

    def __str__(self):
        """Unicode representation of RequirementArtifactRate."""
        pass


class ViewPointRate(models.Model):
    """Model definition for ViewPointRate."""

    # TODO: Define fields here
    view_point = models.ForeignKey("Viewpoint", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ViewPointRate."""

        verbose_name = "ViewPointRate"
        verbose_name_plural = "ViewPointRates"

    def __str__(self):
        """Unicode representation of ViewPointRate."""
        pass


class GoalRate(models.Model):
    """Model definition for GoalRate."""

    # TODO: Define fields here
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GoalRate."""

        verbose_name = "GoalRate"
        verbose_name_plural = "GoalRates"

    def __str__(self):
        """Unicode representation of GoalRate."""
        pass


class RequirementRate(models.Model):
    """Model definition for RequirementRate."""

    # TODO: Define fields here
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementRate."""

        verbose_name = "RequirementRate"
        verbose_name_plural = "RequirementRates"

    def __str__(self):
        """Unicode representation of RequirementRate."""
        pass


class ScenarioRate(models.Model):
    """Model definition for ScenarioRate."""

    # TODO: Define fields here
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ScenarioRate."""

        verbose_name = "ScenarioRate"
        verbose_name_plural = "ScenarioRates"

    def __str__(self):
        """Unicode representation of ScenarioRate."""
        pass


class ProcessRate(models.Model):
    """Model definition for ProcessRate."""

    # TODO: Define fields here
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProcessRate."""

        verbose_name = "ProcessRate"
        verbose_name_plural = "ProcessRates"

    def __str__(self):
        """Unicode representation of ProcessRate."""
        pass


class UseCaseRate(models.Model):
    """Model definition for UseCaseRate."""

    # TODO: Define fields here
    usecase = models.ForeignKey("UseCase", on_delete=models.CASCADE)
    star_rate = models.ForeignKey("StarRate", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UseCaseRate."""

        verbose_name = "UseCaseRate"
        verbose_name_plural = "UseCaseRates"

    def __str__(self):
        """Unicode representation of UseCaseRate."""
        pass


class ProjectLike(models.Model):
    """Model definition for ProjectLike."""

    # TODO: Define fields here
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectLike."""

        verbose_name = "ProjectLike"
        verbose_name_plural = "ProjectLikes"

    def __str__(self):
        """Unicode representation of ProjectLike."""
        pass


class ViewpointLike(models.Model):
    """Model definition for ViewpointLike."""

    # TODO: Define fields here
    view_point = models.ForeignKey("Viewpoint", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ViewpointLike."""

        verbose_name = "ViewpointLike"
        verbose_name_plural = "ViewpointLikes"

    def __str__(self):
        """Unicode representation of ViewpointLike."""
        pass


class GoalLike(models.Model):
    """Model definition for GoalLike."""

    # TODO: Define fields here
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GoalLike."""

        verbose_name = "GoalLike"
        verbose_name_plural = "GoalLikes"

    def __str__(self):
        """Unicode representation of GoalLike."""
        pass


class RequirementLike(models.Model):
    """Model definition for RequirementLike."""

    # TODO: Define fields here
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementLike."""

        verbose_name = "RequirementLike"
        verbose_name_plural = "RequirementLikes"

    def __str__(self):
        """Unicode representation of RequirementLike."""
        pass


class ScenarioLike(models.Model):
    """Model definition for ScenarioLike."""

    # TODO: Define fields here
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ScenarioLike."""

        verbose_name = "ScenarioLike"
        verbose_name_plural = "ScenarioLikes"

    def __str__(self):
        """Unicode representation of ScenarioLike."""
        pass


class ProcessLike(models.Model):
    """Model definition for ProcessLike."""

    # TODO: Define fields here
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProcessLike."""

        verbose_name = "ProcessLike"
        verbose_name_plural = "ProcessLikes"

    def __str__(self):
        """Unicode representation of ProcessLike."""
        pass


class UseCaseLike(models.Model):
    """Model definition for UseCaseLike."""

    # TODO: Define fields here
    use_case = models.ForeignKey("UseCase", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UseCaseLike."""

        verbose_name = "UseCaseLike"
        verbose_name_plural = "UseCaseLikes"

    def __str__(self):
        """Unicode representation of UseCaseLike."""
        pass


class CommentLike(models.Model):
    """Model definition for CommentLike."""

    # TODO: Define fields here
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for CommentLike."""

        verbose_name = "CommentLike"
        verbose_name_plural = "CommentLikes"

    def __str__(self):
        """Unicode representation of CommentLike."""
        pass


class RequirementArtifactLike(models.Model):
    """Model definition for RequirementArtifactLike."""

    # TODO: Define fields here
    requirement_artifact = models.ForeignKey(
        "RequirementArtifact", on_delete=models.CASCADE
    )
    like = models.ForeignKey("Like", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementArtifactLike."""

        verbose_name = "RequirementArtifactLike"
        verbose_name_plural = "RequirementArtifactLikes"

    def __str__(self):
        """Unicode representation of RequirementArtifactLike."""
        pass


class ProjectDislike(models.Model):
    """Model definition for ProjectDislike."""

    # TODO: Define fields here
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProjectDislike."""

        verbose_name = "ProjectDislike"
        verbose_name_plural = "ProjectDislikes"

    def __str__(self):
        """Unicode representation of ProjectDislike."""
        pass


class RequirementArtifactDislike(models.Model):
    """Model definition for RequirementArtifactDislike."""

    # TODO: Define fields here
    requirement_artifact = models.ForeignKey(
        "RequirementArtifact", on_delete=models.CASCADE
    )
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequirementArtifactDislike."""

        verbose_name = "RequirementArtifactDislike"
        verbose_name_plural = "RequirementArtifactDislikes"

    def __str__(self):
        """Unicode representation of RequirementArtifactDislike."""
        pass


class CommentDislike(models.Model):
    """Model definition for CommentDislike."""

    # TODO: Define fields here
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for CommentDislike."""

        verbose_name = "CommentDislike"
        verbose_name_plural = "CommentDislikes"

    def __str__(self):
        """Unicode representation of CommentDislike."""
        pass


class ViewpointDislike(models.Model):
    """Model definition for ViewpointDislike."""

    # TODO: Define fields here
    view_point = models.ForeignKey("Viewpoint", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ViewpointDislike."""

        verbose_name = "ViewpointDislike"
        verbose_name_plural = "ViewpointDislikes"

    def __str__(self):
        """Unicode representation of ViewpointDislike."""
        pass


class GoalDislike(models.Model):
    """Model definition for GoalDislike."""

    # TODO: Define fields here
    goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for GoalDislike."""

        verbose_name = "GoalDislike"
        verbose_name_plural = "GoalDislikes"

    def __str__(self):
        """Unicode representation of GoalDislike."""
        pass


class RequirementDislike(models.Model):
    """Model definition for RequiremetDislike."""

    # TODO: Define fields here
    requirement = models.ForeignKey("Requirement", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for RequiremetDislike."""

        verbose_name = "RequiremetDislike"
        verbose_name_plural = "RequiremetDislikes"

    def __str__(self):
        """Unicode representation of RequiremetDislike."""
        pass


class ScenarioDislike(models.Model):
    """Model definition for ScenarioDislike."""

    # TODO: Define fields here
    scenario = models.ForeignKey("Scenario", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ScenarioDislike."""

        verbose_name = "ScenarioDislike"
        verbose_name_plural = "ScenarioDislikes"

    def __str__(self):
        """Unicode representation of ScenarioDislike."""
        pass


class ProcessDislike(models.Model):
    """Model definition for ProcessDislike."""

    # TODO: Define fields here
    process = models.ForeignKey("Process", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for ProcessDislike."""

        verbose_name = "ProcessDislike"
        verbose_name_plural = "ProcessDislikes"

    def __str__(self):
        """Unicode representation of ProcessDislike."""
        pass


class UseCaseDislike(models.Model):
    """Model definition for UseCaseDislike."""

    # TODO: Define fields here
    use_case = models.ForeignKey("UseCase", on_delete=models.CASCADE)
    dislike = models.ForeignKey("Dislike", on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for UseCaseDislike."""

        verbose_name = "UseCaseDislike"
        verbose_name_plural = "UseCaseDislikes"

    def __str__(self):
        """Unicode representation of UseCaseDislike."""
        pass
