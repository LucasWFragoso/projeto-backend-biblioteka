from rest_framework import generics
from .models import Loan
from .serializers import LoanSerializer
from datetime import datetime
from rest_framework.views import Response, status
from users.permissions import OwnerOrAdmin, IsAdminOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from django.shortcuts import get_object_or_404


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def post(self, request, *args, **kwargs):
        request_data = request.data.copy()
        request_data["created_at"] = datetime.now().date()
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class LoanViewDetail(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "loan_id"


class UserLoansViewDetail(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [OwnerOrAdmin]
    serializer_class = LoanSerializer
    lookup_field = "user_id"

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        find_user = get_object_or_404(User, id=user_id)
        loans = Loan.objects.filter(user=find_user)
        return loans
