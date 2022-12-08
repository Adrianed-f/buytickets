# Generated by Django 4.0.6 on 2022-12-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='row',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (4, 4), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Ряд'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='seat',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (4, 4), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Место'),
        ),
    ]