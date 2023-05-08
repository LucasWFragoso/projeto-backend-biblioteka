from books.models import Book, Follow
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = ["id", "name", "author", "category", "copies_count"]


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["id", "book", "user"]
