from rest_framework import serializers
from .models import Permissions

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissions
        fields = '__all__'