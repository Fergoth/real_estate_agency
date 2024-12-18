# Generated by Django 2.2.24 on 2024-12-02 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20241203_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='complaints', to='property.Flat', verbose_name='Квартира на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
