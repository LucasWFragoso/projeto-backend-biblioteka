from rest_framework import generics, permissions
from users.permissions import IsAdminOrReadOnly
from .models import Book
from .serializers import BookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny & IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.AllowAny & IsAdminOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
