# Generated by Django 3.0.8 on 2020-08-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_auto_20200819_0137'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matches',
            name='teams',
            field=models.ManyToManyField(to='team.teamform'),
        ),
    ]
