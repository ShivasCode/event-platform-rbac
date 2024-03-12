from rest_framework import serializers
from .models import CustomUser
from role.models import Role
from role.serializers import RoleGetSerializer

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()

    class Meta:
        model = CustomUser
        fields = '__all__'

#For getting list of users 
class CustomUserGetSerializer(serializers.ModelSerializer):
    role = RoleGetSerializer()
    groups = serializers.StringRelatedField(source='role.groups', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'groups')

    def create(self, validated_data):
        role_instance = validated_data.pop('role')
        user = CustomUser.objects.create_user(role=role_instance, **validated_data)
        return user

#For post method assigning 
class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    groups = serializers.StringRelatedField(source='role.groups', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'groups')

    def create(self, validated_data):
        role_instance = validated_data.pop('role')
        user = CustomUser.objects.create_user(role=role_instance, **validated_data)
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        role_data = RoleGetSerializer(instance.role).data
        representation['role'] = role_data
        return representation
