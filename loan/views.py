from rest_framework import generics
from .models import Loan
from .serializers import LoanSerializer


class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanViewDetail(generics.RetrieveUpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    lookup_url_kwarg = "loan_id"
