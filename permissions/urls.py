from django.urls import path
from .views import PermissionCreateListView


urlpatterns = [
    path('permissions/', PermissionCreateListView.as_view())
]