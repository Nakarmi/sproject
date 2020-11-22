# Generated by Django 3.1.3 on 2020-11-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_auto_20201122_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='status',
            field=models.CharField(choices=[('Planned', 'PLANNED'), ('Ongoing', 'ONGOING'), ('Completed', 'COMPLETED')], max_length=9),
        ),
    ]
