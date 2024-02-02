from django.utils import path

from .views import (
    UserListView,
    UserDetailView,

    PostListView,
    PostDetailView,

    PhotoListView,
    PhotoDetailView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('photos/', PhotoListView.as_view(), name='photos'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),


]