# Generated by Django 3.1.4 on 2021-09-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0025_auto_20210922_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]