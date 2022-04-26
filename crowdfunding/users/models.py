from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    avatar = models.URLField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.username