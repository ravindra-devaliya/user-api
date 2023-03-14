from django.db import models
from backend.models import BaseModel

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
