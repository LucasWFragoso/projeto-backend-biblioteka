from django.db import models
from users.serializers import User


# Model do Livro que também deve ter um campo read only com uma lógica que leia quantas Copy pertencem ao ID do próprio Book.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)


# Model do Seguindo, contém a ForeignKey do usuário e ForeignKey de Book
class Follow(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="follows", null=True
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="follows", null=True
    )
