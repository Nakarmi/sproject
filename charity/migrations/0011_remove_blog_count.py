# Generated by Django 3.1.3 on 2020-11-25 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0010_blog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='count',
        ),
    ]