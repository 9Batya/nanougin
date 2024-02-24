from django.shortcuts import render
from .forms import DeviceForm
def index(request):
    return render(request, "ugin/ugin.html")

def new_device(request):
    if request.method == 'POST':
        deviceform = DeviceForm(request.POST)
        if deviceform.is_valid():
            deviceform.save()
        else:
            print(deviceform.errors)
    else:
        deviceform = DeviceForm()

    return render(request, "ugin/newdevice.html", {'form': deviceform})

