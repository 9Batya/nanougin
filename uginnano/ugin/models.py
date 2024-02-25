from django.db import models
from .validparams import valid
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





