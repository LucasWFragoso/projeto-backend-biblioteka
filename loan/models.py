from django.db import models


class Loan(models.Model):
    created_at = models.DateField(null=False)
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

    def save(self, *args, **kwargs):
        self.copy.is_deleted = True
        self.copy.save()
        self.copy.book.copies_count -= 1
        self.copy.book.save()
        super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.copy.is_deleted = False
        self.copy.save()
        self.copy.book.copies_count += 1
        self.copy.book.save()
        super().save(*args, **kwargs)
