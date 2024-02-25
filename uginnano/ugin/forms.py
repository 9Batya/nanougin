from django import forms
from .models import Device, DeviceType
from django_json_widget.widgets import JSONEditorWidget
select_device_type = [('---------', '---------')] + [device_type for device_type in
                      DeviceType.objects.values_list('pk','type_name')]
class DeviceFormNew(forms.Form):
    device_type = forms.ChoiceField(label='Тип устройства', choices=select_device_type,
                                    widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    device_model = forms.ChoiceField(label='Модель',choices=str,
                                     widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    field_order = ["device_type",'device_model']

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['parametrs']
        labels = {'parametrs': 'Парпаметры устройства'}
        widgets = {
            'parametrs': JSONEditorWidget(mode='form'),
        }

class DeviceGetForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['parametrs']
        labels = {'parametrs': 'Парпаметры устройства'}
        widgets = {
            'parametrs': JSONEditorWidget(mode='form'),
        }

class DeviceSearch(forms.Form):
    device_ip = forms.CharField(label='ip адрес',help_text='Введите ip адрес устройства')
    field_order = ["device_ip"]