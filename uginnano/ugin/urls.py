from django.urls import path
from . import views
app_name = "ugin"
urlpatterns = [
    path('devicetypes/&lt;int:pk&gt;/', views.DeviceTypeDetail.as_view(), name='item-detail'),
    path('device/save/', views.device_save, name="device_save"),
    path('device/edit/', views.device_edit, name="device_edit"),
    path('device/new/', views.new_device, name="devicenew"),
    path('device/<int:id>/', views.device, name="device_id"),
    path('deviceadd/', views.device_add, name="device_add"),
    path('devicetypes/', views.DeviceTypeList.as_view(), name='item-list'),
    path('', views.index, name='index'),
]
