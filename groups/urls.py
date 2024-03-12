from django.urls import path
from .views import GroupsCreateListView, ModuleCreateAPIView, ModuleDeleteAPIView, ModuleListAPIView, ModuleRetrieveAPIView


urlpatterns = [
    path('groups/', GroupsCreateListView.as_view()),
    path('module/create/', ModuleCreateAPIView.as_view()),
    path('module/delete/<int:pk>/', ModuleDeleteAPIView.as_view()),
    path('module/list/', ModuleListAPIView.as_view()),
    path('module/<int:pk>/', ModuleRetrieveAPIView.as_view()),

]