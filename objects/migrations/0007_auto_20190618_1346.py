# Generated by Django 2.1.1 on 2019-06-18 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0006_auto_20190618_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='rooms',
        ),
        migrations.AddField(
            model_name='room',
            name='centre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='objects.building'),
            preserve_default=False,
        ),
    ]