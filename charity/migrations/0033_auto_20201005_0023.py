# Generated by Django 3.1 on 2020-10-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0032_auto_20201005_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
