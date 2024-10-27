from django.core.validators import MinLengthValidator
from django.db import models

from RegularExam.authors.validators import validate_name_isalpha, validate_passcode


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4), validate_name_isalpha,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2), validate_name_isalpha,
        ],
        null=False,
        blank=False,
    )

    passcode = models.CharField(
        max_length=6,
        validators=(
            validate_passcode,
        ),
        null=False,
        blank=False,
    )

    pets_number = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
    )

    info = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )
