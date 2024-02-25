from django.test import TestCase
from .models import DeviceType, Device, DeviceModel, Parametr

# Здесь тесты для проверки выводимых данных, но можно использовать и как проверку queryset
class ModelTest(TestCase):

    def setUp(self):
        # Модели для тестов
        DeviceType.objects.create(type_name='Коммутатор')
        DeviceType.objects.create(type_name='Камера')
        Parametr.objects.create(parametr_name='ports', parametr_type='int')
        Parametr.objects.create(parametr_name='online', parametr_type='bool')
        Parametr.objects.create(parametr_name='SN', parametr_type='str')


    def test_queryset(self):
        queryset2 = Parametr.objects.values()
        type_id = DeviceType.objects.get(pk=1)
        p1 = Parametr.objects.get(pk=1)
        p3 = Parametr.objects.get(pk=3)
        type_id.parametr_names.add(p1)
        type_id.parametr_names.add(p3)
        device = type_id.device_type_id.create()
        devicemodel = type_id.device_type.create(model_name='Hiwatch')
        device.device_model = devicemodel
        queryset1 = DeviceType.objects.values_list('pk','type_name')
        queryset3 = DeviceType.objects.values_list('parametr_names')
        model = device.device_model
        print(queryset1, queryset2, device, queryset3, devicemodel, model)


