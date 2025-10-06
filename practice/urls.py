"""
URL configuration for practice app.
"""

from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/users/', views.list_users, name='list_users'),
    path('api/users/create/', views.create_user, name='create_user'),
    path('api/users/<str:user_id>/', views.get_user, name='get_user'),
    path('api/users/<str:user_id>/update/', views.update_user, name='update_user'),
    path('api/users/<str:user_id>/delete/', views.delete_user, name='delete_user'),
]
