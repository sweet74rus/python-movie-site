from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .forms import *
from .models import *
from .utils import *


class MovieHome(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Главная',
        )

        return context | c_def

    def get_queryset(self):
        return Movie.objects.all().select_related('genre')


class MovieGenre(DataMixin, ListView):
    model = Movie
    template_name = 'mainapp/index.html'
    context_object_name = 'movies'
    allow_empty = False

    def get_queryset(self):
        return Movie.objects.filter(genre__slug=self.kwargs['genre_slug']).select_related('genre')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['movies'][0].genre,
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'mainapp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Регистрация',
            current_genre='Регистрация'
        )
        return context | c_def


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mainapp/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Авторизация',
            current_genre='Авторизация'
        )
        return context | c_def

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

def about(request):
    return render(request, 'mainapp/about.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена :(</h1>')
