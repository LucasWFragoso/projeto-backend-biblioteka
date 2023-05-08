from django.db import models


class Copy(models.Model):
    book = models.ForeignKey(
        "books.Book",
        on_delete=models.CASCADE,
        related_name="copies",
    )
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.book.copies_count += 1
        self.book.save()
        self.save()
