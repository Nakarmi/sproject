# Generated by Django 3.1 on 2020-10-05 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0045_auto_20201005_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='updated_at',
        ),
    ]