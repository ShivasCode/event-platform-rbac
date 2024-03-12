from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from role.models import Role

class CustomUser(AbstractUser):
    role = models.ForeignKey(Role,on_delete=models.CASCADE,related_name="user_role")

