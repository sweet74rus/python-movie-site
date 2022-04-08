from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', MovieHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('movie/<slug:movie_slug>/', show_movie, name='movie'),
    path('genre/<slug:genre_slug>/', MovieGenre.as_view(), name='genre'),
    path('addmovie/', add_movie, name='add_movie')
]