from rest_framework import routers
from rest_framework.response import Response
from django.urls import path, include
from .api import *

router = routers.DefaultRouter()
router.register('api/data-analysis/female-members', FemaleUsers, 'female')
router.register('api/data-analysis/male-members', MaleUsers, 'male')
urlpatterns = router.urls