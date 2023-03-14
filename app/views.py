from django.shortcuts import render
from app.serializers import PostSerializers
from app.serializers import AuthorSerializers
from app.serializers import BookSerializers
from app.models import Post
from app.models import Author
from app.models import Book
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [AllowAny]


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes = [AllowAny]


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [AllowAny]


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = [AllowAny]
