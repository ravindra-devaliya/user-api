from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField
from app.models import Post
from app.models import Author
from app.models import Book


class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class AuthorSerializers(ModelSerializer):
    books = SerializerMethodField()

    class Meta:
        model = Author
        fields = "__all__"

    def get_books(self, instance):
        books = Book.objects.filter(author_id=instance.id)
        book_serializer = BookSerializers(books, many=True)
        return book_serializer.data


class BookSerializers(ModelSerializer):
    author = SerializerMethodField()

    class Meta:
        model = Book
        fields = "__all__"

    def get_author(self, instance):
        return instance.author.name
