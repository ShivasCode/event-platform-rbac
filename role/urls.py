from django.urls import path 
from .views import GroupsRoleListView, RoleCreateView, RoleListView, GroupWithRolesListView

urlpatterns = [
    path('role/create/', RoleCreateView.as_view()),
    path('role/list/', RoleListView.as_view()),
    path('group-roles/', GroupsRoleListView.as_view()),
    path('groups-with-roles/', GroupWithRolesListView.as_view(), name='group-list'),

    # path('user-role/', UserRoleListCreateView.as_view())
]