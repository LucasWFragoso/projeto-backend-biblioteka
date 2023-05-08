from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.settings import api_settings
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email_field = "email"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[self.email_field] = self.fields["username"]
        del self.fields["username"]

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }

        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed("Wrong credentials")

        return super().validate(attrs)
