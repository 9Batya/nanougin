from django import forms
from .models import Device, DeviceType
from django_json_widget.widgets import JSONEditorWidget
import json
from django.forms import TextInput

# Здесь небольшое ухищрение для выбора device_type
select_device_type = [('---------', '---------')] + [device_type for device_type in
                                                     DeviceType.objects.values_list('pk', 'type_name')]


# Форма для предсоздания device (/ugin/device/new/)
class DeviceFormNew(forms.Form):
    device_type = forms.ChoiceField(label='Тип устройства', choices=select_device_type,
                                    widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    device_model = forms.ChoiceField(label='Модель', choices=str,
                                     widget=forms.Select(attrs={'onchange': 'this.form.submit();'}))

    field_order = ["device_type", 'device_model']



# Форма для изменения параметров и последующего сохранения (/ugin/deviceadd/)
class DynamicForm(forms.Form):
    def __init__(self, parametrs, *args, **kwargs):
        super(DynamicForm, self).__init__(*args, **kwargs)
        for key, value in parametrs.items():
            self.fields[key] = forms.CharField(initial=value, label=key)



class CustomJSONWidget(TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ''
        data_dict = json.loads(value)

        parametrs_form = DynamicForm(parametrs=data_dict)
        parametrs_form.is_valid()  # Вызываем для проведения валидации

        return parametrs_form.as_p()

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['parametrs']
        labels = {'parametrs': 'Параметры устройства'}
        widgets = {
            'parametrs': CustomJSONWidget,
        }



# Форма для поиска устройств (/ugin/devicesearch/)
class DeviceSearch(forms.Form):
    device_ip = forms.CharField(label='ip адрес')
    field_order = ["device_ip"]
