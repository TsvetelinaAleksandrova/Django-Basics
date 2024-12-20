# Generated by Django 4.2.16 on 2024-10-24 19:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import frutipedia.fruits.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), frutipedia.fruits.validators.validate_name_contains_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='profiles.profile')),
            ],
        ),
    ]
