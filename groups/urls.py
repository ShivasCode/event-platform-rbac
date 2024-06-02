from django.urls import path
from .views import GroupsCreateListView, ModuleCreateAPIView, ModuleDeleteAPIView, ModuleListAPIView, ModuleRetrieveAPIView
from .views import EventCreateAPIView, EventDeleteAPIView, EventListAPIView, EventRetrieveAPIView
from .views import BoothCreateAPIView, BoothListAPIView

urlpatterns = [
    path('groups/', GroupsCreateListView.as_view()),
    path('module/create/', ModuleCreateAPIView.as_view()),
    path('module/delete/<int:pk>/', ModuleDeleteAPIView.as_view()),
    path('module/list/', ModuleListAPIView.as_view()),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view()),

    path('event/create/', EventCreateAPIView.as_view()),
    path('event/delete/<int:pk>/', EventDeleteAPIView.as_view()),
    path('event/list/', EventListAPIView.as_view()),
    path('event/<int:pk>/', EventRetrieveAPIView.as_view()),

    path('event/<int:event_id>/booth/create/', BoothCreateAPIView.as_view(), name='booth-create'),
    path('event/<int:event_id>/booth/list/', BoothListAPIView.as_view(), name='booth-list'),
]
