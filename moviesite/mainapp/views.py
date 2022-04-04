from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

context = {
    'title': '',
    'movies': Movie.objects.all(),
    'categories': ['Ужасы', 'Боевики', 'Комедии'],
}

def main_page(request):
    context['title'] = 'Главная'
    return render(request, 'mainapp/index.html', context)

def about(request):
    context['title'] = 'О сайте'
    return render(request, 'mainapp/about.html', context)

def show_movie(request, movie_id):
    return HttpResponse(f'Отображение фильма с id = {movie_id}')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')