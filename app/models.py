from django.db import models
from backend.models import BaseModel
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

GRADE = [("excellent", 1), ("average", 0), ("bad", -1)]


class Post(BaseModel):
    title = models.CharField(max_length=255)
    author = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Author Name"
    )
    rating = models.CharField(choices=GRADE, default="average", max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post"


class Author(BaseModel):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, verbose_name="Book Title")
    publication = models.CharField(max_length=255)
    rating = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
