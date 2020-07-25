from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(User)
admin.site.register(Sector)
admin.site.register(ProjectRate)
admin.site.register(ViewPointRate)
admin.site.register(ActivityLog)
admin.site.register(ProjectMemberIncentive)
admin.site.register(Subscriber)
admin.site.register(GoalRate)
admin.site.register(Process)
admin.site.register(ViewpointRepository)
admin.site.register(Repository)
admin.site.register(ProjectDislike)
admin.site.register(ProjectLike)
admin.site.register(ProjectIncentive)
admin.site.register(ProjectSector)
admin.site.register(ProjectMembership)
admin.site.register(Member)
admin.site.register(Like)
admin.site.register(StarRate)
admin.site.register(Requirement)
admin.site.register(Goal)
admin.site.register(GoalDecomposition)
admin.site.register(Viewpoint)
admin.site.register(Incentive)
admin.site.register(Category)
admin.site.register(ViewpointGoal)
admin.site.register(GoalRelationship)
admin.site.register(Comment)
admin.site.register(Scenario)
admin.site.register(ResetPassword)
admin.site.register(Stakeholder)
admin.site.register(DefaultViewpoint)
admin.site.register(LoginLog)
admin.site.register(UseCase)
admin.site.register(RequirementUsecase)
admin.site.register(RequirementProcess)
admin.site.register(RequirementScenario)
admin.site.register(RequirementGoal)
admin.site.site_header="CORES Administrator Panel"
admin.site.site_title="CORES"