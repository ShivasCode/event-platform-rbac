from rest_framework import serializers
from .models import Groups,Module, Event, Booth

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = '__all__'
        extra_kwargs = {
            'event': {'required': False}
        }