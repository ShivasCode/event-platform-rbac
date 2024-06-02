from django.shortcuts import render
from rest_framework import generics

from .models import Groups, Module, Event, Booth

from .serializers import GroupSerializer, ModuleSerializer, EventSerializer, BoothSerializer
from rest_framework import permissions
from rest_framework.views import APIView
from permissions.permissions import HasPermission, EventBasedPermission



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


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_name = 'get_event'
    serializer_class = EventSerializer

class EventCreateAPIView(generics.CreateAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAdminUser]
    permission_name = 'post_event'
    serializer_class = EventSerializer

class EventDeleteAPIView(generics.DestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAdminUser]
    permission_name = 'delete_event'
    serializer_class = EventSerializer

class EventRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    permission_name = 'retrieve_event'
    serializer_class = EventSerializer

class BoothCreateAPIView(generics.CreateAPIView):
    serializer_class = BoothSerializer
    permission_classes = [EventBasedPermission]
    permission_name = 'post_booth'

    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_id')
        serializer.save(event_id=event_id)



class BoothListAPIView(generics.ListAPIView):
    serializer_class = BoothSerializer
    permission_classes = [EventBasedPermission]
    permission_name = 'get_booth_exhibitor'

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return Booth.objects.filter(event_id=event_id)


