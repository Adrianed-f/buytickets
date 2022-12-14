# Generated by Django 4.0.6 on 2022-12-08 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата приобретения')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.event', verbose_name='Событие')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to='profiles.profile', verbose_name='Владелец')),
            ],
        ),
    ]
