from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from SpeedApp.cars.choices import CarTypeChoices
from SpeedApp.cars.validators import validate_year


class Car(models.Model):
    type = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        choices=CarTypeChoices.choices,
    )

    model = models.CharField(
        max_length=15,
        validators=(MinLengthValidator(1),),
        null=False,
        blank=False,

    )

    year = models.IntegerField(
        validators=(validate_year,),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        },
        verbose_name='Image URL'
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(1.0),
        ),
        null=False,
        blank=False,

    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name="cars"
    )
