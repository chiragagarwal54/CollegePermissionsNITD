# Generated by Django 2.2.4 on 2019-08-27 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authorizationlist',
            name='for_rooms',
        ),
    ]
