# Generated by Django 5.0.2 on 2024-02-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugin', '0015_delete_deviceparametr'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametr',
            name='parametr_type',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
