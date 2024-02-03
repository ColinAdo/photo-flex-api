from django.utils import path

from .views import (
    UserListView,
    UserDetailView,
    UserPostListView,

    PostListView,
    PostDetailView,
    PostPhotoListView,

    PhotoListView,
    PhotoDetailView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/posts/', UserPostListView.as_view(), name='userpost-list'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/photos/', PostPhotoListView.as_view(), name='postphoto-list'),

    path('photos/', PhotoListView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),


]