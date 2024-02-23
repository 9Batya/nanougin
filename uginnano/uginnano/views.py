from django.shortcuts import render
from django.http import HttpResponse
# Представление главной страницы приложения
def index(request):
    return render(request, "index.html")