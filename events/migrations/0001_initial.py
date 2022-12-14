# Generated by Django 4.0.6 on 2022-12-08 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('placements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название События')),
                ('about', models.TextField(verbose_name='О событии')),
                ('session_start', models.DateTimeField(verbose_name='Начало сеанса')),
                ('session_end', models.DateTimeField(verbose_name='Конец сеанса')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='placements.placement', verbose_name='Распложение')),
            ],
        ),
    ]
