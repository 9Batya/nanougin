from django.urls import path, include, re_path
from . import views
#путь на самом деле будет 127.0.0.1:8000/flussonic, т.к. находится в urls приложения flussonic
app_name = "ugin"
urlpatterns = [
    path('device/new/', views.new_device, name="devicenew"),
    path('', views.index, name='index'),
]
