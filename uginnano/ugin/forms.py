from django import forms
from .models import Device, DeviceType
select_device_type = [device_type for device_type in
                      DeviceType.objects.values_list('pk','type_name')]
class DeviceForm(forms.Form):
    device_type = forms.ChoiceField(label='Тип устройства',help_text='выберите тип устройства',
                                    choices=select_device_type)
    device_model = forms.ChoiceField(label='Тип устройства', help_text='выберите тип устройства',
                                    choices=list)
    field_order = ["device_type",'device_model']
