from rest_framework import serializers

from .models import CustomUser, Post, Photo


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='userpost-list', format='html')

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'posts', )
        extra_kwargs = {'password': {'write_only': True}}


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'


