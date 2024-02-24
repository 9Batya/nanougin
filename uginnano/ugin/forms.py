from django import forms
from .models import Device, DeviceModel
class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['device_type_id', 'device_model']
        labels = {'device_type_id': 'тип устройства', 'device_model': 'модель устройства'}

    def __init__(self, *args, **kwargs):
        super(DeviceForm, self).__init__(*args, **kwargs)

        # Проверяем, есть ли в форме поле device_type_id
        if 'device_type_id' in self.fields:
            # Добавляем атрибут onchange для перезагрузки формы при изменении типа устройства
            self.fields['device_type_id'].widget.attrs['onchange'] = 'this.form.submit();'

        # Проверяем, есть ли в форме поле device_model
        if 'device_model' in self.fields:
            # Если выбран тип устройства, обновляем варианты выбора для device_model
            device_type_id = self.data.get('device_type_id')
            if device_type_id:
                model_list = DeviceModel.objects.filter(device_type=device_type_id).values_list('model_name', 'model_name')
                choices = [('---------', '---------')] + list(model_list)
                self.fields['device_model'].choices = choices
                # Добавляем атрибут onchange для перезагрузки формы при изменении модели устройства
                self.fields['device_model'].widget.attrs['onchange'] = 'this.form.submit();'

    # def clean(self):
    #     cleaned_data = super().clean()
    #     device_type_id = cleaned_data.get('device_type_id')
    #
    #     if device_type_id:
    #         model_list = [(model[0], model[0]) for model in device_type_id.device_type.values_list('model_name')]
    #         self.fields['device_model'].choices = model_list
    #         cleaned_data['device_model'] = model_list
    #         print(cleaned_data,device_type_id,self.fields['device_model'].choices)
    #
    #         # Обновите device_model на основе новых choices
    #         if cleaned_data['device_model'] not in dict(model_list):
    #             self.add_error('device_model', 'Выберите допустимую модель')
    #
    #     return cleaned_data

