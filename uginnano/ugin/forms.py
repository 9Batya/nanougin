from django import forms
from .models import Device, DeviceType
from django_json_widget.widgets import JSONEditorWidget
#Здесь небольшое ухищрение для выбора device_type
select_device_type = [('---------', '---------')] + [device_type for device_type in
                      DeviceType.objects.values_list('pk','type_name')]
#Форма для предсоздания device (/ugin/device/new/)
class DeviceFormNew(forms.Form):
    device_type = forms.ChoiceField(label='Тип устройства', choices=select_device_type,
                                    widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    device_model = forms.ChoiceField(label='Модель',choices=str,
                                     widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    field_order = ["device_type",'device_model']
#Форма для изменения параметров и последующего сохранения (/ugin/deviceadd/)
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['parametrs']
        labels = {'parametrs': 'Парпаметры устройства'}
        widgets = {
            'parametrs': JSONEditorWidget(mode='form'),
        }
#Форма для поиска устройств (/ugin/devicesearch/)
class DeviceSearch(forms.Form):
    device_ip = forms.CharField(label='ip адрес',help_text='Введите ip адрес устройства')
    field_order = ["device_ip"]