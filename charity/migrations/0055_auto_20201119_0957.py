# Generated by Django 3.1.3 on 2020-11-19 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0054_auto_20201119_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='time',
            field=models.CharField(blank=True, max_length=75),
        ),
    ]