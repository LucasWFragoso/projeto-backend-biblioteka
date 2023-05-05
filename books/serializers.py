from books.models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    copia = serializers.SerializerMethodField()
    pivo = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'category', 'copy', 'follow']