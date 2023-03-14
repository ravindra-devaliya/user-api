from rest_framework.serializers import ModelSerializer
from app.models import Post
from app.models import Author
from app.models import Book


class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorSerializers(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializers(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
