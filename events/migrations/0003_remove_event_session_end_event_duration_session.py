# Generated by Django 4.0.6 on 2022-12-08 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_remove_event_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='session_end',
        ),
        migrations.AddField(
            model_name='event',
            name='duration_session',
            field=models.CharField(default=1, max_length=8, verbose_name='Продолжительность сеанса'),
            preserve_default=False,
        ),
    ]
