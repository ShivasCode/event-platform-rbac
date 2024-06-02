from django.urls import path 
from .views import UserLoginView, CustomUserCreateView, CustomUserUpdateView, CustomUserListView, CustomUserDeleteView, UserListByGroupView, JoinEventAPIView, RegistrantListOnEvent

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('user-create/', CustomUserCreateView.as_view()),
    path('user-update/<int:pk>/', CustomUserUpdateView.as_view()),
    path('user-list/', CustomUserListView.as_view()),
    path('user-delete/<int:pk>/', CustomUserDeleteView.as_view()),
    path('users/by_group/<int:group_id>/', UserListByGroupView.as_view(), name='user-list-by-group'),

    path('event/<int:event_id>/join/', JoinEventAPIView.as_view(), name='join_event'),
    path('event/<int:event_id>/registrants/', RegistrantListOnEvent.as_view(), name='registrant_list'),

]
