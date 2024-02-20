from django.contrib import admin

# Register your models here.
from .models import DeviceType, DeviceModel, Device, DeviceParametr, Parametr

# class DeviceModelinline(admin.StackedInline):
#     model = DeviceModel
#     extra = 1

# class Deviceinline(admin.StackedInline):
#     model = Device
#     extra = 1

class Parametrinline(admin.StackedInline):
    model = Device
    extra = 1

# class ParametrInline(admin.StackedInline):
#     model = Parametr
#     extra = 1

class DeviceTypeAdmin(admin.ModelAdmin):
    filter_horizontal = ('parameters',)

# class DeviceModelAdmin(admin.ModelAdmin):
#     inlines = [Deviceinline]
#     filter_horizontal = ('parameters',)


# class DeviceAdmin(admin.ModelAdmin):
#     inlines = [ParametrInline]




# admin.site.register(Device, DeviceAdmin)

# admin.site.register(DeviceModel, DeviceModelAdmin)

admin.site.register(DeviceType, DeviceTypeAdmin)

admin.site.register(Parametr)


