from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    followers = models.ManyToManyField(
        'self', related_name='followees', symmetrical=False)


# Modify the ManyToManyField related names to avoid clashes
CustomUser.groups.field.remote_field.related_name = 'customuser_groups'
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_user_permissions'


class Post(models.Model):
    author = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)