# Generated by Django 3.0.8 on 2020-08-20 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='fifties',
        ),
        migrations.RemoveField(
            model_name='players',
            name='highestscore',
        ),
        migrations.RemoveField(
            model_name='players',
            name='hundreds',
        ),
        migrations.RemoveField(
            model_name='players',
            name='totalmatches',
        ),
        migrations.RemoveField(
            model_name='players',
            name='totalruns',
        ),
    ]
