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
        queryset2 = Parametr.objects.values()
        print([device_type for device_type in queryset1])
        print(queryset1, queryset2)

