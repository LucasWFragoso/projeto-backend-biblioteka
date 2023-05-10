from django.db import models
from users.serializers import User


class Book(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    category = models.CharField(max_length=20)
    copies_count = models.IntegerField(default=5)


class Follow(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book", null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True
    )
