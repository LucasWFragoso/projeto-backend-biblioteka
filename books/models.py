from django.db import models


# Model do Livro que também deve ter um campo read only com uma lógica que leia quantas Copy pertencem ao ID do próprio Book.
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    follow = models.ForeignKey(
        "Follow", on_delete=models.CASCADE, related_name="follows", null=True
    )


# Model da Cópia que deve ter a ForeignKey de Book
# class Copy(models.Model):
#     ...


# # Model do empréstimo que deve conter a ForeignKey de Copy, ForeignKey do User importado do abstract user do app users.
# class Loan(models.Model):
#     ...


# Model do Seguindo, contém a ForeignKey do usuário e ForeignKey de Book
class Follow(models.Model):
    ...
