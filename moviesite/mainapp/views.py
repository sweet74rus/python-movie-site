from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

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


def about(request):
    context['title'] = 'О сайте'
    context['current_genre'] = 'О сайте'
    return render(request, 'mainapp/about.html', context)


def add_movie(request):
    context['title'] = 'Добавить фильм'
    context['current_genre'] = 'Добавить фильм'

    if request.method == 'POST':
        form = AddMovieForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('home')

    else:
        form = AddMovieForm()

    context['form'] = form
    return render(request, 'mainapp/add_movie.html', context)


def show_movie(request, movie_slug):
    movie = get_object_or_404(Movie, slug=movie_slug)
    context['movies'] = movie
    context['current_genre'] = movie.genre

    return render(request, 'mainapp/movie_info.html', context)

class MovieGenre(ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['movies'] = Movie.objects.filter(genre__slug=self.kwargs['genre_slug'])
        context['title'] = context['movies'][0].genre
        context['current_genre'] = context['movies'][0].genre

        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
