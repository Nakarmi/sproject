# Generated by Django 3.1.4 on 2021-09-11 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0022_donation_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='image',
        ),
    ]
