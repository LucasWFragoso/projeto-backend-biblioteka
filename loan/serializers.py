from rest_framework import serializers
from .models import Loan
from users.models import User
from copies.models import Copy
from datetime import timedelta
import ipdb


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    copy_id = serializers.PrimaryKeyRelatedField(
        queryset=Copy.objects.all(), source="copy", write_only=True
    )

    def create(self, validated_data):
        devolution_date = validated_data["devolution_date"]
        create_at = validated_data["created_at"]
        devolution_date = create_at + timedelta(7)
        ipdb.set_trace()

        return super().create(validated_data)

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
        extra_kwargs = {"devolution_date": {"read_only": True}}
