# Generated by Django 5.1.1 on 2024-09-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
