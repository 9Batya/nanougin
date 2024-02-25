from django.urls import path
from . import views
app_name = "uginapi"
#Маршруты для api
urlpatterns = [
    path('devices/<int:pk>/', views.DeviceDetail.as_view(), name='devices-detail'),
    path('devicetypes/<int:pk>/', views.DeviceTypeDetail.as_view(), name='devicetype-detail'),
    path('devicemodels/<int:pk>/', views.DeviceModelDetail.as_view(), name='devicemodel-detail'),
    path('devicetypes/', views.DeviceTypeList.as_view(), name='devicetype-list'),
    path('devicemodels/', views.DeviceModelList.as_view(), name='devicemodel-list'),
    path('devices/', views.DevicelList.as_view(), name='devices-list'),
]
