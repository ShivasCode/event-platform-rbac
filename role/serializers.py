

from rest_framework import serializers
from .models import Role
from groups.models import Groups
from permissions.models import Permissions
from permissions.serializers import PermissionSerializer
from groups.serializers import GroupSerializer

class BaseRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleGetSerializer(BaseRoleSerializer):
    permissions = PermissionSerializer(many=True, read_only=True)
    groups = GroupSerializer()

    class Meta:
        model = Role
        fields = ('id', 'name', 'permissions', 'groups')


class RoleCreateSerializer(serializers.ModelSerializer):
    permissions = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Role
        fields = '__all__'

    def create(self, validated_data):
        permissions_data = validated_data.pop('permissions', [])
        role = Role.objects.create(**validated_data)

        for permission_id in permissions_data:
            try:
                permission = Permissions.objects.get(id=permission_id)
                role.permissions.add(permission)
            except Permissions.DoesNotExist:
                raise serializers.ValidationError(f"Permission with ID {permission_id} does not exist.")

        return role

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['permissions'] = PermissionSerializer(instance.permissions.all(), many=True).data
        return representation

class RoleUpdateSerializer(serializers.ModelSerializer):
    permissions = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Role
        fields = ('id', 'name', 'permissions')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

        permissions_data = validated_data.get('permissions', [])
        instance.permissions.clear()

        for permission_id in permissions_data:
            try:
                permission = Permissions.objects.get(id=permission_id)
                instance.permissions.add(permission)
            except Permissions.DoesNotExist:
                raise serializers.ValidationError(f"Permission with ID {permission_id} does not exist.")

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['permissions'] = PermissionSerializer(instance.permissions.all(), many=True).data
        return representation

class RoleWithGroupsSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ('id', 'name', 'permissions', 'groups')

class GroupWithRolesSerializer(serializers.ModelSerializer):
    roles = RoleGetSerializer(many=True, read_only=True, source='groups_role')

    class Meta:
        model = Groups
        fields = ('id', 'name', 'description', 'roles')

# class UserRoleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserRole 
#         fields = '__all__'