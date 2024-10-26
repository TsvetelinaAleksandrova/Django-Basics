from django.core.validators import MinValueValidator
from django.db import models

from SpeedApp.profiles.validators import validate_username_length, validate_username_chars


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            validate_username_length,
            validate_username_chars,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(21),
        ),
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=25,

        null=True,
        blank=True,
        verbose_name='First Name'
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        if self.first_name:
            return f'{self.first_name}'
        if self.last_name:
            return f'{self.last_name}'
        return None
