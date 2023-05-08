from rest_framework import generics
from .models import Loan
from .serializers import LoanSerializer
from datetime import datetime
from rest_framework.views import Response, status


class LoanView(generics.ListCreateAPIView):
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
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_url_kwarg = "loan_id"
