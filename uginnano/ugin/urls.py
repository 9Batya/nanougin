from django.urls import path
from . import views
app_name = "ugin"
urlpatterns = [
    path('device/save/', views.device_save, name="device"),
    path('device/new/', views.new_device, name="devicenew"),
    path('device/<int:id>/', views.device, name="device"),
    path('deviceadd/', views.device_add, name="device"),
    path('', views.index, name='index'),
]
