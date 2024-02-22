from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch import receiver
import ipaddress
import re
class DeviceType(models.Model):
    type_name = models.CharField(max_length=200)
    parametr_names = models.ManyToManyField('Parametr')
    def __str__(self):
        return self.type_name

class Parametr(models.Model):
    type_list = [
        ('int', 'int'),
        ('str', 'str'),
        ('bool', 'bool'),
    ]
    parametr_name = models.CharField(max_length=200)
    parametr_type = models.CharField(max_length=200, default=None, choices=type_list)
    def __str__(self):
        return self.parametr_name

class DeviceModel(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE,
                                    related_name='device_type')
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name

class Device(models.Model):
    model_list = str

    device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE,
                                       related_name='device_type_id', default=None)
    device_model = models.CharField(max_length=200, default=None, choices=model_list, null=True, blank=True)
    parametrs = models.JSONField(default=dict, null=True, blank=True)

    def clean(self):
        # if self.device_model:
        #     if self.device_type_id != self.device_model.device_type:
        #         raise ValidationError('Выбранный тип устройства не соответствует модели устройства')

        regexmac = re.compile(r'^[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:[a-z0-9]{2}:'
                              r'[a-z0-9]{2}:[a-z0-9]{2}$')

        data = self.device_type_id.parametr_names.values_list('parametr_name','parametr_type')
        name_type_dict = dict(data)
        for key, value in self.parametrs.items():
            if value:
                # чтобы при ошибке не удалялось значение device_model
                self.device_model = self.device_model
                if key in name_type_dict:
                    if name_type_dict[key] == 'int' and not isinstance(value, int):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть числом')
                    elif name_type_dict[key] == 'str' and not isinstance(value, str):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть строкой')
                    elif name_type_dict[key] == 'bool' and not isinstance(value, bool):
                        raise ValidationError(f'Значение для параметра "{key}" должно быть булевым')
                if key == 'MAC':
                    match = regexmac.search(value)
                    if not match:
                        raise ValidationError(f'Значение "{value}" не соответствует виду aa:aa:aa:aa:aa:aa')
                elif key == 'ip':
                    try:
                        ipaddress.ip_address(value)
                    except Exception as exp:
                        raise ValidationError(f'Ошибка: "{exp}"')

    def save(self):
        return models.Model.save(self)

    def __str__(self):
        return str(self.id)





