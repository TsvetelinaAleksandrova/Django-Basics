# Generated by Django 4.2.16 on 2024-10-24 19:28

import django.core.validators
from django.db import migrations, models
import frutipedia.profiles.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), frutipedia.profiles.validators.validate_name_starts_with_letter])),
                ('last_name', models.CharField(max_length=35, validators=[django.core.validators.MinLengthValidator(1), frutipedia.profiles.validators.validate_name_starts_with_letter])),
                ('email', models.EmailField(max_length=40, unique=True)),
                ('password', models.CharField(help_text='*Password length requirements: 8 to 20 characters', max_length=20, validators=[django.core.validators.MinLengthValidator(8)])),
                ('image_url', models.URLField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, default=18, null=True)),
            ],
        ),
    ]
