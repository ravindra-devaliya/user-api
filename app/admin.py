from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.admin import register
from app.models import Post
from app.models import Author
from app.models import Book


@register(Post)
class PostAdmin(ModelAdmin):
    list_display = ["id", "title", "author", "rating"]


class BookInline(TabularInline):
    model = Book
    extra = 1


@register(Book)
class BookAdmin(ModelAdmin):
    list_display = [
        "title",
        "author",
        "publication",
        "rating",
        "image",
        "description",
    ]


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = [
        "name",
        "date_of_birth",
        "nationality",
        "details",
        "image",
    ]
    inlines = [BookInline]
