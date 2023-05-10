from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView
from loan.views import UserLoansViewDetail

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailView.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/<int:user_id>/loans/", UserLoansViewDetail.as_view()),
]
