from django.urls import path

from .views import (
    UserListView,
    UserDetailView,
    UserPostListView,
    PhotoListView,

)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/posts/', UserPostListView.as_view(), name='userpost-list'),
    path('users/<int:pk>/posts/<int:post_pk>/photos/', PhotoListView.as_view(), name='photos-list'),



]