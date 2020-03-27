from rest_framework import serializers
from projects.models import *

class GenderSerializer(serializers.ModelSerializer):

    class Meta:
            model = Member
            fields = ['id','gender']