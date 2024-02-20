# Generated by Django 5.0.2 on 2024-02-20 04:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
                ('device_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ugin.devicetype')),
            ],
        ),
    ]
