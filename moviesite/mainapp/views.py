from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class MovieHome(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная')

        return context | c_def


class MovieGenre(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['movies'][0].genre,
            movies=Movie.objects.filter(genre__slug=self.kwargs['genre_slug']),
            current_genre=Movie.objects.filter(genre__slug=self.kwargs['genre_slug'])[0].genre
        )

        return context | c_def


class ShowMovie(DataMixin, DetailView):
    model = Movie
    template_name = 'mainapp/movie_info.html'
    slug_url_kwarg = 'movie_slug'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['movies'],
            current_genre=context['movies'],
            movies=context['movies']
        )

        return context | c_def

class AddMovie(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMovieForm
    template_name = 'mainapp/add_movie.html'
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Добавить фильм',
            current_genre='Добавить фильм'
        )

        return context | c_def

def about(request):
    return render(request, 'mainapp/about.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
