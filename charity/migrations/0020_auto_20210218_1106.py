# Generated by Django 3.1.4 on 2021-02-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0019_donation_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(default=0, primary_key='True', serialize=False),
        ),
    ]
