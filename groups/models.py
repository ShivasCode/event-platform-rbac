from django.db import models

# Create your models here.
class Groups(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        
class Module(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=255)

class Booth(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_booth')