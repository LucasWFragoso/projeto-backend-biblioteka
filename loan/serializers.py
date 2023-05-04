from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {"user_id": {"read_only": True}, "copy_id": {"read_only": True}}
