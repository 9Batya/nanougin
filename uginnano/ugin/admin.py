from django.contrib import admin
from django import forms
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
# Register your models here.
from .models import DeviceType, DeviceModel, Device, Parametr


class Parametrinline(admin.StackedInline):
    model = Device
    extra = 1

class DeviceTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ('parametr_names',)


@admin.register(Device)
class DevicesModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(mode='form')},
    }


admin.site.register(DeviceType, DeviceTypeAdmin)

admin.site.register(Parametr)

admin.site.register(DeviceModel)



