from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    birthdate = models.DateField(null=True)
    collaborator = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True, null=True)
