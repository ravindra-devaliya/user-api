from django.urls import path
from app.views import PostListAPIView
from app.views import PostRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="posts"),
    path("post/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view()),
]
