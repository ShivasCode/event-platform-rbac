from django.shortcuts import render
from rest_framework import generics
from .models import Permissions
from .serializers import PermissionSerializer
from rest_framework import permissions
# from rest_framework import 
# Create your views here.


class PermissionCreateListView(generics.ListCreateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAdminUser]



