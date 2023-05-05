from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that name already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    # def create(self, validated_data: dict) -> User:
    #     return User.objects.create_superuser(**validated_data)

    # def update(self, instance: User, validated_data: dict) -> User:
    #     for key, value in validated_data.items():
    #         if key == "password":
    #             instance.set_password(value)
    #         else:
    #             setattr(instance, key, value)

    #     instance.save()

    #     return instance

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
        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}
