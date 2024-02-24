from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import DeviceFormNew, DeviceForm, DeviceGetForm
from .models import DeviceType, DeviceModel, Device
import json
def index(request):
    return render(request, "ugin/ugin.html")

def new_device(request):
    context = {}
    deviceformnew = DeviceFormNew(request.GET)
    context['form'] = deviceformnew
    device_type_id = request.GET.get('device_type', None)
    if device_type_id != '---------':
        model_list = [(model[0], model[0]) for model in
                      DeviceModel.objects.filter(device_type=device_type_id).values_list('model_name')]
        deviceformnew.fields['device_model'].choices = [('---------', '---------')] + model_list
        device_model = request.GET.get('device_model', None)
        context['type'] = device_type_id
        context['model'] = device_model

    return render(request, "ugin/newdevice.html", context)

def device_add(request):
    type_id = request.POST.get("type", "Undefine")
    model = request.POST.get("model", "Undefine")
    type_name = DeviceType.objects.get(pk=type_id)
    parametr_names_dict = {param['parametr_name']: ''
                           for param in type_name.parametr_names.values('parametr_name')}
    initial_data = {'device_type_id': type_id, 'device_model': model, 'parametrs': parametr_names_dict}
    print(initial_data)
    deviceform = DeviceForm(initial=initial_data)

    data = {'form': deviceform, 'type_name': type_name,'model': model, 'type_id': type_id}
    return render(request, "ugin/deviceadd.html", context=data)

def device_save(request):
    if request.method == "POST":
        type_id = request.POST.get("type")
        type_name = DeviceType.objects.get(pk=type_id)
        parametrs = json.loads(request.POST.get("parametrs"))
        device = type_name.device_type_id.create()
        device.device_model = request.POST.get("model")
        device.parametrs =parametrs
        device.save()
    return HttpResponseRedirect("/ugin/")


def device(request, id):
    try:
        device = Device.objects.get(pk=id)
        print(device)

        if request.method == "GET":
            deviceform = DeviceGetForm(instance=device)
            return render(request, "ugin/device.html", {"device": device,"form": deviceform})
        else:
            return render(request, "ugin/device.html", {"device": device})
    except Device.DoesNotExist:
        return HttpResponseNotFound("<h2>Device not found</h2>")