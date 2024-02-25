from django.shortcuts import render

# Представление главной страницы приложения
def index(request):
    return render(request, "index.html")