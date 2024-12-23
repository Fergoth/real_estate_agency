# Generated by Django 2.2.24 on 2024-12-02 03:01

from django.db import migrations


def fill_new_building_field(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(year_gte=2015).update(new_building=True)
    Flat.objects.filter(year_lt=2015).update(new_building=False)


def move_backwards(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.all().update(new_building=None)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_field, move_backwards)
    ]
