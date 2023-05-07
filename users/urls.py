from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("users/login/", CustomTokenObtainPairView.as_view()),
]
