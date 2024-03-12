from django.shortcuts import render

from .models import Role
from groups.models import Groups
from .serializers import RoleCreateSerializer,RoleGetSerializer, GroupWithRolesSerializer, RoleUpdateSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class RoleListView(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleGetSerializer
    permission_classes = [permissions.IsAdminUser]

class RoleCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleCreateSerializer  
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class RoleUpdateView(generics.UpdateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleUpdateSerializer  
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        serializer.save()



class GroupsRoleListView(generics.ListAPIView):
    serializer_class = RoleGetSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        group_id = self.request.query_params.get('group', None)
        
        if group_id:
            try:
                group = Groups.objects.get(id=group_id)
                return Role.objects.filter(groups=group)
            except Groups.DoesNotExist:
                raise generics.Http404(f"Group with ID {group_id} does not exist.")

        return Role.objects.none()


class GroupWithRolesListView(generics.ListAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupWithRolesSerializer

# class UserRoleListCreateView(generics.ListCreateAPIView):
#     queryset = UserRole.objects.all()
#     serializer_class = UserRoleSerializer
#     permission_classes = [permissions.IsAdminUser]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

# user = UserRole.objects.get(id=1)
# user.delete()