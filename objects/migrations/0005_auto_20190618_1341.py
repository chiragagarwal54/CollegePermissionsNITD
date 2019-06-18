# Generated by Django 2.1.1 on 2019-06-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_auto_20190618_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='centre',
        ),
        migrations.AddField(
            model_name='building',
            name='rooms',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='objects.room'),
            preserve_default=False,
        ),
    ]
