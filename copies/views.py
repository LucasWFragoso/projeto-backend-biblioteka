from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
)

from .serializers import CopySerializer
from .models import Copy
from users.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.serializers import Book
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import Response


class CreateCopyView(CreateAPIView):
    serializer_class = CopySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    lookup_url_kwarg = "book_id"

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs.get("book_id"))
        book.copies_count += 1
        book.save()
        serializer.save(book=book)


from books.models import Follow
from books.serializers import FollowSerializer


class FollowViews(CreateAPIView, DestroyAPIView):
    queryset = Follow.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FollowSerializer

    def perform_create(self, serializer):
        user = self.request.user
        book = get_object_or_404(Book, id=self.kwargs["book_id"])
        search_follow = Follow.objects.filter(user=user, book=book).first()
        if search_follow:
            raise Exception("User already follows this book")
        return serializer.save(user=user, book=book)

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=400)

    def get_object(self):
        book_id = self.kwargs["book_id"]
        queryset = self.get_queryset()
        object = get_object_or_404(queryset, book__id=book_id)
        return object
