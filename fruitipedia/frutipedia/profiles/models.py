from django.core.validators import MinLengthValidator
from django.db import models

from frutipedia.profiles.validators import validate_name_starts_with_letter


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(2), validate_name_starts_with_letter],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=35,
        validators=[MinLengthValidator(1),validate_name_starts_with_letter],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False,
        unique=True,
    )

    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        help_text= "*Password length requirements: 8 to 20 characters",
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        default=18,
        blank=True,
        null=True,
    )
