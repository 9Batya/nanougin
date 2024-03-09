from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from .forms import DeviceFormNew, DeviceForm, DeviceSearch
from .models import DeviceType, DeviceModel, Device
from .validparams import valid
import json


# главная страница приложения
def ugin(request):
    return render(request, "ugin/ugin.html")


# view для выбора device_type и device_model
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


# view для редактирования параметров после выбора типа и модели устройства
def device_add(request):
    type_id = request.POST.get("type", "Undefine")
    model = request.POST.get("model", "Undefine")
    type_name = DeviceType.objects.get(pk=type_id)
    parametr_names_dict = {param['parametr_name']: ''
                           for param in type_name.parametr_names.values('parametr_name')}
    initial_data = {'device_type_id': type_id, 'device_model': model, 'parametrs': parametr_names_dict}
    deviceform = DeviceForm(initial=initial_data)
    data = {'form': deviceform, 'type_name': type_name, 'model': model, 'type_id': type_id}
    return render(request, "ugin/deviceadd.html", context=data)


# view для сохранения, используется в html deviceadd
def device_save(request):
    if request.method == "POST":
        values_to_remove = ['csrfmiddlewaretoken', 'type', 'model', 'initial-parametrs']
        parametrs = {key: request.POST.get(key)
                     for key in request.POST if key not in values_to_remove}
        type_id = request.POST.get("type")
        type_name = DeviceType.objects.get(pk=type_id)
        model = request.POST.get("model")
        check_errors = valid(type_name, parametrs, model)
        check_errors.convert()
        try:
            check_errors.validation()
            if check_errors.validation()['status'] == 'sucsess':
                device = type_name.device_type_id.create()
                device.device_model = model
                device.parametrs = parametrs
                device.save()
                return HttpResponseRedirect("/ugin/")
        except Exception as exp:
            return HttpResponse(f'Неверно введены параметры {exp}')


# view для сохранения, используется в device.html
def device_edit(request):
    if request.method == "POST":
        device_id = request.POST.get("device")
        device = Device.objects.get(pk=device_id)
        values_to_remove = ['csrfmiddlewaretoken', 'device', 'model', 'initial-parametrs']
        parametrs = {key: request.POST.get(key)
                     for key in request.POST if key not in values_to_remove}
        device.parametrs = parametrs
        check_errors = valid(device.device_type_id, parametrs, device.device_model)
        check_errors.convert()
        try:
            check_errors.validation()
            if check_errors.validation()['status'] == 'sucsess':
                device.save()
                return HttpResponseRedirect("/ugin/")
        except Exception as exp:
            return HttpResponse(f'Неверно введены параметры {exp}')


# view для уже созданного устройства, в device.html
def device(request, id):
    try:
        device = Device.objects.get(pk=id)
        devicemodel = device.device_model
        devicetype = device.device_type_id
        data = {"device": device, "devicemodel": devicemodel, "devicetype": devicetype}
        deviceform = DeviceForm(instance=device)
        data['form'] = deviceform
        return render(request, "ugin/device.html", context=data)
    except Device.DoesNotExist:
        return HttpResponseNotFound("<h2>Device not found</h2>")


# view для поиска устройства по его ip адресу
def device_search(request):
    devicesearch_form = DeviceSearch()
    if request.method == "POST":
        device_ip = request.POST.get("device_ip")
        devices = Device.objects.filter(parametrs__ip=device_ip)
        if devices:
            # Возвращает список device.id, у которых такой ip адрес
            id = [device.id for device in devices]
            data = {'id': id, 'form': devicesearch_form}
            return render(request, "ugin/devicesearch.html", context=data)
        else:
            return HttpResponse(f'Устройства с адресом {device_ip} не существует')
    else:
        return render(request, "ugin/devicesearch.html", {'form': devicesearch_form})
