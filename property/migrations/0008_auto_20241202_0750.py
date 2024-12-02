# Generated by Django 2.2.24 on 2024-12-02 04:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
