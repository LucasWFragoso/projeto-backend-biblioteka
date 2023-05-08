from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from datetime import timedelta, date
from books.models import Book


def is_weekend(day):
    return day.weekday() >= 5


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source="book", write_only=True
    )

    def create(self, validated_data):
        devolution_date = date.today() + timedelta(days=7)
        while is_weekend(devolution_date):
            devolution_date += timedelta(days=1)
        validated_data["devolution_date"] = devolution_date
        book = validated_data.pop("book")
        if book.copies_count == 0:
            raise Exception("Não tem cópias disponíveis!")
        book.copies_count -= 1
        book.save()
        copy_id = book.copies.first().id
        data = {"copy_id": copy_id, **validated_data}

        return super().create(data)

    def update(self, instance, validated_data):
        copy = Copy.objects.get(id=instance.copy_id)
        book = Book.objects.get(id=copy.book_id)
        book.copies_count += 1
        book.save()
        return super().update(instance, validated_data)

    class Meta:
        model = Loan
        fields = [
            "id",
            "created_at",
            "devolution_date",
            "is_returned",
            "user_id",
            "book_id",
        ]
        depth = 2
        extra_kwargs = {"devolution_date": {"read_only": True}}
