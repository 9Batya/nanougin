# Generated by Django 5.0.2 on 2024-02-20 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugin', '0013_rename_parametr_deviceparametr'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeviceTypeParametr',
            new_name='Parametr',
        ),
    ]
