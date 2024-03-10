from .views import ReadOnlyDeviceViewSet, ReadOnlyDeviceModelViewSet, ReadOnlyDeviceTypeViewSet
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'devices', ReadOnlyDeviceViewSet, basename='device')
router.register(r'device-models', ReadOnlyDeviceModelViewSet, basename='device-model')
router.register(r'device-types', ReadOnlyDeviceTypeViewSet, basename='device-type')

urlpatterns = router.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Micro-Ugin API",
      default_version='v1',
      description="Система учета оборудования",
   ),
   public=True,
)


urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




