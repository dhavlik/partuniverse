from django.contrib.auth.models import User
from rest_framework import serializers
from partsmanagement.models import *


# class UserSerializer(serializers.ModelSerializer):
#   class Meta:
#       model = User
#       fields = ('url', 'username', 'email', 'is_staff')


class StorageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        fields = ('name', )
