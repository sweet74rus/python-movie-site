from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

movies = Movie.objects.all()

def main_page(request):
    return render(request, 'mainapp/index.html', {'title': 'Главная', 'movies': movies})

def about(request):
    return render(request, 'mainapp/about.html', {'title': 'О сайте'})

def categories(request, category_name):
    return HttpResponse(f"<h1>Категории фильмов</h1><p>{category_name}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')