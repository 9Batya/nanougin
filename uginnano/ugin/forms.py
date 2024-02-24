from django import forms
from .models import Device, DeviceType, DeviceModel
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

class DeviceGetForm(forms.ModelForm):

    # device_model = forms.ModelChoiceField(queryset=DeviceModel.objects.filter(device_type=device_type_id).values_list('model_name'),
    #                                       empty_label="Категория не выбрана", label="Категории")
    class Meta:
        model = Device
        fields = ['device_type_id', 'device_model', 'parametrs']
        labels = {'device_type_id': 'Тип устройства', 'device_model': 'Модель устройства',
                  'parametrs': 'Парпаметры устройства'}
