from django.core.validators import MinLengthValidator
from django.db import models

from frutipedia.fruits.validators import validate_name_contains_only_letters
from frutipedia.profiles.models import Profile


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=(MinLengthValidator(2), validate_name_contains_only_letters),
        null=False,
        blank=False,
        unique=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='fruits'
    )
