from rest_framework.permissions import BasePermission
from users.models import CustomUser

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_roles = self.get_user_roles(request.user)
            if user_roles:
                permission_name = getattr(view, 'permission_name', None)

                for user_role in user_roles:
                    if permission_name and permission_name in user_role.permissions.values_list('name', flat=True):
                        return True

        return False

    def get_user_roles(self, user):
        try:
            return user.role.all()
        except CustomUser.DoesNotExist:
            return None
