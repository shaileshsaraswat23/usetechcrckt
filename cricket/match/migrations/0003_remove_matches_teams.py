# Generated by Django 3.0.8 on 2020-08-20 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_matches_teams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matches',
            name='teams',
        ),
    ]
