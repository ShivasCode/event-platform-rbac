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
    role = RoleGetSerializer(many=True)
    groups = serializers.StringRelatedField(source='roles.groups', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'groups')

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        user = CustomUser.objects.create_user(**validated_data)
        user.roles.set(roles_data)  # Set the roles for the user
        return user

    
#For post method assigning 
class CustomUserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)
    groups = serializers.StringRelatedField(source='roles.groups', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'role', 'groups')

    def create(self, validated_data):
        roles_data = validated_data.pop('role')
        user = CustomUser.objects.create_user(**validated_data)
        user.role.set(roles_data) 
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        role_data = RoleGetSerializer(instance.role, many=True).data
        representation['role'] = role_data
        return representation
