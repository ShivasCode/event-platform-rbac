from django.db import models
from groups.models import Event
# Create your models here.
from django.contrib.auth.models import AbstractUser
from role.models import Role

class CustomUser(AbstractUser):
    # role = models.ForeignKey(Role,on_delete=models.CASCADE,related_name="user_role")
    role = models.ManyToManyField(Role,related_name='customuser_role')
    email = models.EmailField(unique=True)  


# if we used m2m in customuser, we cannot track the registrant status ex. Payment status
class Registrant(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_registrant')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrant_event')
    payment_status = models.BooleanField(default=False)
    # role = models.ManyToManyField(Role,related_name='customuser_role')
    is_staff = models.BooleanField(default=False)