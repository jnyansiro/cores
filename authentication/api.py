from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics
from .serializers import *
from projects.models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
