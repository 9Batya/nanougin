from django.apps import AppConfig
class UginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ugin'

    def ready(self):
        from . import signals


