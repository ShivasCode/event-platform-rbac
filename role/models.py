from django.db import models
from groups.models import Groups
from permissions.models import Permissions


class Role(models.Model):
    name = models.CharField(max_length=255)
    groups = models.ForeignKey(Groups, on_delete=models.CASCADE, related_name='groups_role')
    permissions = models.ManyToManyField(Permissions)

    def __str__(self):
        return self.name

# class UserRole(models.Model):
#     # name = models.CharField(max_length=255)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="userrole_user", null=True, blank=True)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='userrole_role')