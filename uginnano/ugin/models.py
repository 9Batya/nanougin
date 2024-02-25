from django.db import models
from .validparams import valid

"""
Модель с типом устройства, связан many to many с параметрами, т.к. у разных параметров могут быть разные типы
устройств и у разных типов устройств могут быть разные параметры, также дает возможность динамично изменять
параметры для определенного типа устройства в админке
"""
class DeviceType(models.Model):
    type_name = models.CharField(max_length=200)
    parametr_names = models.ManyToManyField('Parametr')
    def __str__(self):
        return self.type_name

#Параметры устройств, parametr_type нужен для валидации вводимых данных
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

#Модель устройства, связан внешним ключом с devicetype
class DeviceModel(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE,
                                    related_name='device_type')
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name
"""
Модель устройства, есть валидация как по типу вводимых данных, так и по MAC и ip (clean), валидацию убрана в отдельный класс,
т.к. используется и в формах. Связан ключом с DeviceType, model_list формируется через сигналы
"""
class Device(models.Model):
    model_list = list

    device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE,
                                       related_name='device_type_id', default=None)
    device_model = models.CharField(max_length=200, default=None, choices=model_list, null=True, blank=True)
    parametrs = models.JSONField(default=dict, null=True, blank=True)


    def clean(self):
        check_errors = valid(self.device_type_id, self.parametrs, self.device_model)
        check_errors.validation()


    def save(self, *args, **kwargs):
        super(Device, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id)





