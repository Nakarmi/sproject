# Generated by Django 3.1 on 2020-10-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0040_auto_20201005_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(max_length=255, null=True),
        ),
    ]
