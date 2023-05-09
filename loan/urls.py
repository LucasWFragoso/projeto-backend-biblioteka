from django.urls import path
from .views import LoanView, LoanViewDetail, UserLoansViewDetail

urlpatterns = [
    path("loan/", LoanView.as_view()),
    path("loan/<int:loan_id>/", LoanViewDetail.as_view()),

]
