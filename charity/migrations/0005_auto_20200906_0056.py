# Generated by Django 3.1 on 2020-09-05 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_volunteer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='author',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '98********'. Up to 1 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
