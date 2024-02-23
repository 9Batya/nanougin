from django.shortcuts import render
from .forms import DeviceForm
def index(request):
    return render(request, "ugin/ugin.html")

def new_device(request):
    model_list = str
    deviceform = DeviceForm()
    deviceform.fields['device_model'].choices = model_list
    return render(request, "ugin/newdevice.html",{'form':deviceform})

