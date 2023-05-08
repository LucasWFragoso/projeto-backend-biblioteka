from django.db import models


class Loan(models.Model):
    created_at = models.DateField(auto_now_add=True)
    devolution_date = models.DateField(null=False)
    is_returned = models.BooleanField(default=False)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="loans",
    )
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="loans",
    )
