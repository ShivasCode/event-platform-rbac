from django.shortcuts import render
from rest_framework import generics

from .models import Groups, Module

from .serializers import GroupSerializer, ModuleSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from permissions.permissions import HasPermission



# Create your views here.


class GroupsCreateListView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]




class ModuleListAPIView(generics.ListAPIView):
    queryset = Module.objects.all()
    permission_classes = [HasPermission]
    permission_name = 'get_module'  
    serializer_class = ModuleSerializer


class ModuleCreateAPIView(generics.CreateAPIView):
    queryset = Module.objects.all()
    permission_classes = [HasPermission]
    permission_name = 'post_module'  
    serializer_class = ModuleSerializer

class ModuleDeleteAPIView(generics.DestroyAPIView):
    queryset = Module.objects.all()
    permission_classes = [HasPermission]
    permission_name = 'delete_module'  
    serializer_class = ModuleSerializer

class ModuleRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Module.objects.all()
    permission_classes = [HasPermission]
    permission_name = 'retrieve_module'  
    serializer_class = ModuleSerializer

