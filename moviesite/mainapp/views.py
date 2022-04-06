from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from .models import *

context = {
    'title': '',
    'movies': Movie.objects.all(),
    'current_genre': 'Все жанры',
}


def main_page(request):
    context['title'] = 'Главная'
    context['movies'] = Movie.objects.all()
    context['current_genre'] = 'Все жанры'

    return render(request, 'mainapp/index.html', context)


def about(request):
    context['title'] = 'О сайте'
    return render(request, 'mainapp/about.html', context)


def show_movie(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context['movies'] = movie
    context['current_genre'] = movie.genre

    return render(request, 'mainapp/movie_info.html', context)


def show_genre(request, genre_id):
    context['movies'] = Movie.objects.filter(genre_id=genre_id)
    context['current_genre'] = Genre.objects.all()[genre_id - 1]

    if len(context['movies']) == 0:
        raise Http404()

    return render(request, 'mainapp/index.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
