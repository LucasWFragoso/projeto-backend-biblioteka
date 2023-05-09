from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "book_id"]
        depth = 1

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)
