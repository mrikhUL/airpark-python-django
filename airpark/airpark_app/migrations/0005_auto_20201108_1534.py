# Generated by Django 3.1.2 on 2020-11-08 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airpark_app', '0004_auto_20201108_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
