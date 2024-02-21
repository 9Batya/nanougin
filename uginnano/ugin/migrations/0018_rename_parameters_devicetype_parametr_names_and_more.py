# Generated by Django 5.0.2 on 2024-02-21 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugin', '0017_device_device_type_id_device_parametrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='devicetype',
            old_name='parameters',
            new_name='parametr_names',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_model', to='ugin.devicemodel'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='device_type_id', to='ugin.devicetype'),
        ),
        migrations.AlterField(
            model_name='device',
            name='parametrs',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='devicemodel',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_type', to='ugin.devicetype'),
        ),
        migrations.AlterField(
            model_name='parametr',
            name='parametr_type',
            field=models.CharField(choices=[('int', 'integer'), ('text', 'text'), ('bool', 'boolean')], default=None, max_length=200),
        ),
    ]
