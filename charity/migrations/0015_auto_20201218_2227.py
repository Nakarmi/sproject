# Generated by Django 3.1.4 on 2020-12-18 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0014_auto_20201218_2212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='province',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='purpose',
        ),
    ]
