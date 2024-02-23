
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path("ugin/", include("ugin.urls")),
    path("admin/", admin.site.urls),
    path('', views.index),
]
