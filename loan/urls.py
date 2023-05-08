from django.urls import path
from .views import LoanView, LoanViewDetail

urlpatterns = [
    path("loan/", LoanView.as_view()),
    path("loan/<int:loan_id>/", LoanViewDetail.as_view()),
]
