from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    copy_id = serializers.PrimaryKeyRelatedField(
        queryset=Copy.objects.all(), source="copy", write_only=True
    )

    class Meta:
        model = Loan
        fields = [
            "id",
            "created_at",
            "devolution_date",
            "is_returned",
            "user_id",
            "copy_id",
        ]
