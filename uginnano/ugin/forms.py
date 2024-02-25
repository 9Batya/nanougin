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

    # device_model = forms.ModelChoiceField(queryset=DeviceModel.objects.filter(device_type=device_type_id).values_list('model_name'),
    #                                       empty_label="Категория не выбрана", label="Категории")
    class Meta:
        model = Device
        fields = ['parametrs']
        labels = {'parametrs': 'Парпаметры устройства'}
        widgets = {
            'parametrs': JSONEditorWidget(mode='form'),
        }