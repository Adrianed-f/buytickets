# Generated by Django 4.0.6 on 2022-12-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_event_session_end_event_duration_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
    ]
