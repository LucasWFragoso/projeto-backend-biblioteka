from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "email",
            "birthdate",
            "password",
            "is_superuser",
        ]

        extra_kwargs = {"password": {"write_only": True}}
