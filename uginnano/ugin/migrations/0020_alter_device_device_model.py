# Generated by Django 5.0.2 on 2024-02-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugin', '0019_alter_device_device_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.CharField(blank=True, choices=[], default=None, max_length=200, null=True),
        ),
    ]