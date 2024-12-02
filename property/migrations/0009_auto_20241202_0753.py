# Generated by Django 2.2.24 on 2024-12-02 04:53

from django.db import migrations
import phonenumbers


def fill_pure_phones(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        parsed_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(parsed_phone):
            flat.owner_pure_phone = phonenumbers.format_number(
                parsed_phone,
                phonenumbers.PhoneNumberFormat.E164
            )
        else:
            flat.owner_pure_phone = None
        flat.save()


def move_backwards(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.all():
        flat.owner_pure_phone = None
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20241202_0750'),
    ]

    operations = [
        migrations.RunPython(fill_pure_phones, move_backwards)
    ]