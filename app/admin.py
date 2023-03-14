from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.admin import register
from app.models import Post
from app.models import Author
from app.models import Book
from django.utils.html import format_html


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
        "image_view",
        "description",
    ]

    def image_view(self, obj):
        if obj.image:
            return format_html(
                f'<img src="{obj.image.url}" width="auto" height="70px" />'
            )
        return ""


@register(Author)
class AuthorAdmin(ModelAdmin):
    list_display = [
        "name",
        "date_of_birth",
        "nationality",
        "details",
        "image_view",
    ]
    inlines = [BookInline]

    def image_view(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="auto" height="70px" />'.format(obj.image.url)
            )
        return ""

    image_view.short_description = "image"
