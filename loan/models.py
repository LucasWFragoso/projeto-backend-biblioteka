from django.db import models


class Loan(models.Model):
    created_at = models.DateField(null=False)
    devolution_date = models.DateField(null=False)
    is_returned = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="albums",
    )
    copy = models.ForeignKey(
        "books.Copy",
        on_delete=models.CASCADE,
        related_name="albums",
    )
