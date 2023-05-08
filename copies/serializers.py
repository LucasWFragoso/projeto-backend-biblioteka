from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "book"]
        # depth = 2
        # extra_kwarg = {"book": {"read_only": True}}

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
