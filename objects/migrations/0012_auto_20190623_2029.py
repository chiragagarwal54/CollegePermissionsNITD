# Generated by Django 2.1.1 on 2019-06-23 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('objects', '0011_auto_20190622_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissionform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=500)),
                ('dates', models.DateField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Building')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='room',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Building'),
        ),
        migrations.AddField(
            model_name='permissionform',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objects.Room'),
        ),
    ]