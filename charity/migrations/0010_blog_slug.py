# Generated by Django 3.1.3 on 2020-11-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0009_auto_20201125_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]