from django.db import models
from django.core.exceptions import ValidationError
from django.core.signals import request_finished
from django.db.models.signals import pre_save
from django.dispatch import receiver

def callback(sender, **kwargs):
    print("Setting changed!")
class DeviceType(models.Model):
    type_name = models.CharField(max_length=200)
    parameters = models.ManyToManyField('Parametr')
    def __str__(self):
        return self.type_name

class Parametr(models.Model):
    parametr_name = models.CharField(max_length=200)
    parametr_type = models.CharField(max_length=200, default=None)
    def __str__(self):
        return self.parametr_name

class DeviceModel(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name

class Device(models.Model):
    device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE, default=None)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    parametrs = models.JSONField(default=dict, null=True, blank=True)

    def clean(self):
        if self.device_model != None:
            if self.device_type_id != self.device_model.device_type:
                raise ValidationError('Выбранный тип устройства не соответствует модели устройства')
    def save(self):
        parameters_dict = {param.parametr_name: '' for param in self.device_type_id.parameters.all()}
        if self.parametrs=={}:
            self.parametrs.update(parameters_dict)

        return models.Model.save(self)

    def __str__(self):
        return str(self.id)





