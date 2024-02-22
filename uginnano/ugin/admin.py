from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import DeviceType, DeviceModel, Device, Parametr
@admin.register(DeviceType)
class DeviceTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ('parametr_names',)

@admin.register(Device)
class DevicesModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(mode='form')},
    }

admin.site.register(Parametr)

admin.site.register(DeviceModel)



