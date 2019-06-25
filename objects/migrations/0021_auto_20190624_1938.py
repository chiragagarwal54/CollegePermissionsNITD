# Generated by Django 2.1.1 on 2019-06-24 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0020_auto_20190624_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionform',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Building'),
        ),
        migrations.AlterField(
            model_name='permissionform',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Room'),
        ),
        migrations.AlterField(
            model_name='room',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Building'),
        ),
    ]