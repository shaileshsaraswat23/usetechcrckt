# Generated by Django 3.0.8 on 2020-08-18 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20200818_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamform',
            name='logouri',
            field=models.ImageField(upload_to='team'),
        ),
    ]
