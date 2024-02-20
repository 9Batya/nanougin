from django.db import models

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
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    device_type_id = models.ForeignKey(DeviceType, on_delete=models.CASCADE,default=None)
    parametrs = models.JSONField(default=dict, null=True, blank=True)

    def save(self):
        parameters_dict = {param.parametr_name: '' for param in self.device_type_id.parameters.all()}
        if self.parametrs=={}:
            self.parametrs.update(parameters_dict)

        return models.Model.save(self)

    def __str__(self):
        return str(self.id)





