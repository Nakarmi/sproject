# Generated by Django 3.1 on 2020-09-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0018_blog_edited_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('T', 'LGBTQ')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='joined_from',
            field=models.DateField(auto_now=True),
        ),
    ]
