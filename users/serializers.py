from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def create(self, validated_data: dict) -> User:
        if validated_data["collaborator"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "birthdate",
            "password",
            "is_superuser",
            "username",
            "collaborator",
            "is_allowed",
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_allowed": {"read_only": True},
        }
