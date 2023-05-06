from django.db import models
from users.serializers import User


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)


class Follow(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book", null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True
    )
