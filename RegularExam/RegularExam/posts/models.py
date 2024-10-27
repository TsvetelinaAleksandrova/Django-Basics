from django.core.validators import MinLengthValidator
from django.db import models

from RegularExam.authors.models import Author


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(5),
        ],
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        }
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        related_name="posts",
    )
