# Generated by Django 3.1.3 on 2020-12-06 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airpark_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='car_park_id',
            new_name='car_park',
        ),
    ]