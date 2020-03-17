from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics
from knox.models import AuthToken
from .serializers import *
from projects.models import *



class FemaleUsers(viewsets.ModelViewSet):
    queryset = Member.objects.filter(gender="Female")
    permission_classes = [
        permissions.AllowAny
    ]
    # serializer_class = GenderSerializer