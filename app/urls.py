from django.urls import path
from app.views import PostListAPIView
from app.views import PostRetrieveUpdateDestroyAPIView
from app.views import AuthorListAPIView
from app.views import BookListAPIView

urlpatterns = [
    path("posts/", PostListAPIView.as_view(), name="posts"),
    path("post/<int:pk>/", PostRetrieveUpdateDestroyAPIView.as_view()),
    path("authors/", AuthorListAPIView.as_view(), name="authors"),
    path("books/", BookListAPIView.as_view(), name="books"),
]
