from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    avatar = models.URLField(null=True, blank=True, max_length=1000)
    bio = models.TextField(null=True, blank=True, max_length=2000)
    
    def __str__(self):
        return self.username