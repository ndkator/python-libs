from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Определяет функции, которые получают запросы пользователей, обрабатывают их и возвращают ответ

def index(request):
    data = {'header': "Hello Django", 'message': "Welcome to Python"}
    return render(request, "boom/index.html", context=data)

def about(request):
    data = {'header': "Hello Django", 'message': "Welcome to Python"}
    return render(request, "boom/about.html", context=data)

def creators(request):
    return HttpResponse('<h2> Создатели </h2>')

def search(request):
    return HttpResponse('<h2> На данной странице выводятся результаты поиска.</h2>')


''' ФУНКЦИИ  ВЫШЕ  УЖЕ НЕ ИСПОЛЬЗУЮТСЯ '''


