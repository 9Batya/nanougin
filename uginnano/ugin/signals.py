from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Device

@receiver(pre_save, sender=Device.ready())
def update_device_model_choices(sender, instance, **kwargs):
    instance._meta.get_field('device_model').limit_choices_to = {
        'device_type': instance.device_type_id
    }