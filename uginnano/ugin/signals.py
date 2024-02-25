from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Device

"""
Сигнал реагирует на сохранение, позволяет менять поле device_model (model_list в коде), добавлять параметры
в зависимости от типа устройства (instance.parametrs.update). Но адекватно применить это успел (осилил) только
в админке django
"""
@receiver(pre_save, sender=Device)
def update_device_model_choices(sender, instance, **kwargs):
    if instance.device_type_id:
        model_list = [(model[0], model[0]) for model in instance.device_type_id.device_type.values_list('model_name')]
        sender._meta.get_field('device_model').choices = model_list
    if instance.pk:
        original_instance = sender.objects.get(pk=instance.pk)
        if original_instance.device_type_id != instance.device_type_id:
            instance.parametrs = {}
        # возвращает кортедж из parametr_name, т.к. значение одно, берем [0] и формируем словарь
        parametr_names_dict = {param[0]: ''
                               for param in instance.device_type_id.parametr_names.values_list('parametr_name')}
        if instance.parametrs == {}:
            instance.parametrs.update(parametr_names_dict)