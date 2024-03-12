from rest_framework.permissions import BasePermission
# from role.models import UserRole
from users.models import CustomUser

class HasPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            user_role = self.get_user_role(request.user)
            if user_role:
                permission_name = getattr(view, 'permission_name', None)

                if permission_name and permission_name in user_role.permissions.values_list('name', flat=True):
                    return True

        return False

    def get_user_role(self, user):
        try:
            return user.role
        except CustomUser.DoesNotExist:
            return None
