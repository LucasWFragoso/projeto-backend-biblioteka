from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from datetime import timedelta, date
from books.models import Book
from rest_framework.exceptions import ValidationError
from apscheduler.schedulers.background import BackgroundScheduler


def is_weekend(day):
    return day.weekday() >= 5


scheduler = BackgroundScheduler()


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source="book", write_only=True
    )

    def create(self, validated_data):
        user = validated_data.get("user")
        if user.is_allowed:
            devolution_date = date.today() + timedelta(days=7)
            while is_weekend(devolution_date):
                devolution_date += timedelta(days=1)
            validated_data["devolution_date"] = devolution_date
            book = validated_data.pop("book")
            if book.copies_count == 0:
                raise ValidationError("Não tem cópias disponíveis!")
            book.copies_count -= 1
            book.save()
            copy_id = book.copies.first().id
            data = {"copy_id": copy_id, **validated_data}

            return super().create(data)
        else:
            raise ValidationError("User isn't allowed to borrow!")

    def update(self, instance, validated_data):
        is_returned = validated_data.get("is_returned")

        if is_returned:
            self.schedule_user_unblock(instance)
        copy = Copy.objects.get(id=instance.copy_id)
        book = Book.objects.get(id=copy.book_id)
        book.copies_count += 1
        book.save()
        return super().update(instance, validated_data)

    @classmethod
    def schedule_user_unblock(cls, instance):
        if not instance.is_returned:
            scheduler.add_job(
                func=cls.unblock_user,
                args=[instance.user_id],
                trigger="interval",
                hours=120,
                id=f"user_{instance.user_id}_unblock",
            )
            scheduler.start()

    @staticmethod
    def unblock_user(user_id):
        from users.models import User

        user = User.objects.get(id=user_id)
        user.is_allowed = True
        user.save()
        scheduler.pause_job(job_id=f"user_{user_id}_unblock")
        return

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
