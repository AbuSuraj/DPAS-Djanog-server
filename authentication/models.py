# authentication/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    userid = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.email
