from rest_framework import generics, permissions

from .models import CustomUser, Post, Photo
from .serializers import UserSerializer, PostSerializer, PhotoSerializer

class UserListView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserPostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):

        queryset = Post.objects.filter(author_id=self.kwargs.get('pk'))
        return queryset


class PhotoListView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):

        queryset = Photo.objects.filter(post_id=self.kwargs.get('post_pk'))
        return queryset
    


