from rest_framework.permissions import BasePermission
from users.models import CustomUser
from rest_framework import response


from rest_framework.permissions import BasePermission
from users.models import CustomUser,Registrant

class EventBasedPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True

            user = request.user
            event_id = view.kwargs.get('event_id')  
            if event_id:
                staff_exists = Registrant.objects.filter(user=request.user, event_id=event_id, is_staff=True).exists()
                registrant_exists = Registrant.objects.filter(user=request.user, event_id=event_id, payment_status=True).exists()
                if staff_exists:
                    return True
                elif registrant_exists:
                    user_roles = self.get_user_roles(request.user)
                    if user_roles:
                        permission_name = getattr(view, 'permission_name', None)
                        for user_role in user_roles:
                            if permission_name and permission_name in user_role.permissions.values_list('name', flat=True):
                                return True
                    return False  #User has no roles
                return False  #User is not a registrant for this event or has not paid

        return False  #User is not authenticated

    def get_user_roles(self, user):
        try:
            return user.role.all()
        except CustomUser.DoesNotExist:
            return None


class HasPermission(BasePermission):
    def has_permission(self, request, view):        
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_staff:
                return True
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
