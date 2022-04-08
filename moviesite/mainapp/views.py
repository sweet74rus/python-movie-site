from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

context = {
    'title': '',
    'movies': Movie.objects.all(),
    'current_genre': 'Все жанры',
}


class MovieHome(ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Главная'
        context['movies'] = Movie.objects.all()
        context['current_genre'] = 'Все жанры'

        return context


class MovieGenre(ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['movies'] = Movie.objects.filter(genre__slug=self.kwargs['genre_slug'])
        context['title'] = context['movies'][0].genre
        context['current_genre'] = context['movies'][0].genre

        return context


class ShowMovie(DetailView):
    model = Movie
    template_name = 'mainapp/movie_info.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['movies']
        context['current_genre'] = context['movies']
        return context

class AddMovie(CreateView):
    form_class = AddMovieForm
    template_name = 'mainapp/add_movie.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Добавить фильм'
        context['current_genre'] = 'Добавить фильм'

        return context

def about(request):
    context['title'] = 'О сайте'
    context['current_genre'] = 'О сайте'
    return render(request, 'mainapp/about.html', context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
