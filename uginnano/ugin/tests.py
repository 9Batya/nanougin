from django.test import TestCase
from .models import DeviceType, Device, DeviceModel, Parametr
class ModelTest(TestCase):
    def setUp(self):
        # Создайте объекты модели для использования в тестах
        DeviceType.objects.create(type_name='Коммутатор')
        DeviceType.objects.create(type_name='Камера')
        Parametr.objects.create(parametr_name='ports', parametr_type='int')
        Parametr.objects.create(parametr_name='online', parametr_type='bool')
        Parametr.objects.create(parametr_name='SN', parametr_type='str')


    def test_queryset(self):
        queryset1 = DeviceType.objects.values_list('pk','type_name')
        queryset3 = DeviceType.objects.values_list('parametr_names')
        queryset2 = Parametr.objects.values()
        type_id = DeviceType.objects.get(pk=1)
        device = type_id.device_type_id.create()
        devicemodel = type_id.device_type.create(model_name='Hiwatch')
        model = DeviceModel.objects.filter(device_type=type_id).values_list('model_name')
        # print(devicemodel)
        # device_values = Device.objects.values()
        # print([device_type for device_type in queryset1])
        # print(queryset1, queryset2, devicemodel, device_values, device, queryset3)
        print(model)

