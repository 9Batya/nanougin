from ugin.models import DeviceType, DeviceModel, Device
from .serializers import DeviceTypeSerializer, DeviceModelSerializer, DeviceSerializer
from rest_framework import generics

# Create your views here.
class DeviceTypeList(generics.ListCreateAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer

class DeviceTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer

class DeviceModelList(generics.ListCreateAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer

class DeviceModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceModel.objects.all()
    serializer_class = DeviceModelSerializer

class DevicelList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer