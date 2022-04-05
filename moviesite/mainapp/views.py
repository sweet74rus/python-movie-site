from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *

context = {
    'title': '',
    'movies': Movie.objects.all(),
    'categories': ['Ужасы', 'Боевики', 'Комедии'],
    'genre': Genre.objects.all()
}


def main_page(request):
    context['title'] = 'Главная'
    return render(request, 'mainapp/index.html', context)


def about(request):
    context['title'] = 'О сайте'
    return render(request, 'mainapp/about.html', context)


def show_movie(request, movie_id):
    return HttpResponse(f'Отображение фильма с id = {movie_id}')


def show_genre(request, genre_id):
    context['movies'] = Movie.objects.filter(genre_id=genre_id)

    if len(context['movies']) == 0:
        raise Http404()

    return render(request, 'mainapp/index.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
