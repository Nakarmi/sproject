# Generated by Django 3.1 on 2020-09-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0024_auto_20200923_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='joined_from',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]