from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

# from serializers import CopySerializer
from .serializers import CopySerializer
from .models import Copy
from users.permissions import IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.serializers import Book


class CreateCopyView(CreateAPIView):
    serializer_class = CopySerializer
    queryset = Copy.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    lookup_url_kwarg = "book_id"

    def perform_create(self, serializer):
        book = Book.objects.get(pk=self.kwargs["book_id"])
        # book_id = self.lookup_url_kwarg
        serializer.save(book=book)


from books.models import Follow
from books.serializers import FollowSerializer
from django.shortcuts import get_object_or_404


class FollowListCreateView(ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer


class FollowRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

    def get_queryset(self):
        user = self.request.user
        book_id = self.kwargs["book_id"]
        return Follow.objects.filter(user=user, book=book_id)

    def get_object(self):
        book_id = self.kwargs["book_id"]
        queryset = self.get_queryset()
        object = get_object_or_404(queryset, book__id=book_id)
        return object
