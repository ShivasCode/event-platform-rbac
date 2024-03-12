

from django.urls import path 
from .views import UserLoginView, CustomUserCreateView, CustomUserUpdateView, CustomUserListView, CustomUserDeleteView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('user-create/', CustomUserCreateView.as_view()),
    path('user-update/<int:pk>/', CustomUserUpdateView.as_view()),
    path('user-list/', CustomUserListView.as_view()),
    path('user-delete/<int:pk>/', CustomUserDeleteView.as_view()),

]