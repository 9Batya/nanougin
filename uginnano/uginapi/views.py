from ugin.models import DeviceType, DeviceModel, Device
from .serializers import DeviceTypeSerializer, DeviceModelSerializer, DeviceSerializer
from rest_framework import mixins, viewsets

#Представления, List дает представлении о всех экземплярах, Detail о конкретном, соответствуют своим сериализаторам
class ReadOnlyDeviceViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class ReadOnlyDeviceModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer

class ReadOnlyDeviceTypeViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer