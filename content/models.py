from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    follower = models.ManyToManyField('self', related_name='followees', symmetrical=False)
