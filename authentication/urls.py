from rest_framework import routers
from rest_framework.response import Response
from django.urls import path, include
from knox import views as knox_views
from .api import *

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox-logout'),
    # path('api/members/update/',MemberUpdateViewSet.as_view(), name='member-update')
]