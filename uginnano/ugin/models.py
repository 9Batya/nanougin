from django.db import models

class DeviceType(models.Model):
    type_name = models.CharField(max_length=200)
    parameters = models.ManyToManyField('DeviceTypeParametr')
    def __str__(self):
        return self.type_name

class DeviceTypeParametr(models.Model):
    parametr_name = models.CharField(max_length=200)
    def __str__(self):
        return self.parametr_name

class DeviceModel(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    def __str__(self):
        return self.model_name

class Device(models.Model):
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)


class Parametr(models.Model):
    device_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    online = models.BooleanField(default = None)
    SN = models.CharField(max_length=200, default = None)
    IP = models.CharField(max_length=200, default = None)
    MAC = models.CharField(max_length=200, default = None)
    role = models.CharField(max_length=200, default = None)
    ports_number = models.IntegerField(default = None)
    camera_number = models.CharField(max_length=200, default = None)
    microphone = models.CharField(max_length=200, default = None)
    view = models.IntegerField(default = None)
    comment = models.CharField(max_length=200, default = None)
    azimut = models.IntegerField(default=None)
    camera_number = models.CharField(max_length=200,default = None)
    antenna_height = models.IntegerField(default=None)

