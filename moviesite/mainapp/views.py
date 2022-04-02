from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def main_page(request):
    return HttpResponse('Страница киносайта')

def categories(request, category_name):
    return HttpResponse(f"<h1>Категории фильмов</h1><p>{category_name}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')