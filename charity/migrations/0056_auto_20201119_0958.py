# Generated by Django 3.1.3 on 2020-11-19 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0055_auto_20201119_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='time',
            field=models.CharField(max_length=75),
        ),
    ]
