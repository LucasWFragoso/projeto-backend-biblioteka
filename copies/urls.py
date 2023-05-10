from django.urls import path
from . import views

urlpatterns = [
    path("books/<int:book_id>/copy", views.CreateCopyView.as_view()),
    path("books/<int:book_id>/follow", views.FollowViews.as_view()),
]
