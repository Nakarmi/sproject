# Generated by Django 3.1.4 on 2021-03-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0020_auto_20210218_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='mode',
            field=models.CharField(choices=[('q', 'QR Code'), ('c', 'Cheque')], max_length=9),
        ),
        migrations.AlterField(
            model_name='donation',
            name='province',
            field=models.CharField(choices=[('P1', 'Province 1'), ('P2', 'Province 2'), ('P3', 'Province 3'), ('P4', 'Province 4'), ('P5', 'Province 5'), ('P6', 'Province 6'), ('P7', 'Province 7')], max_length=100),
        ),
        migrations.AlterField(
            model_name='donation',
            name='purpose',
            field=models.CharField(choices=[('f', 'Food'), ('e', 'Education'), ('c', 'Clothing'), ('h', 'Health'), ('s', 'Shelter')], max_length=9),
        ),
    ]
