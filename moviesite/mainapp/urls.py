from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('about/', about, name='about'),
    path('movie/<slug:movie_slug>/', show_movie, name='movie'),
    path('genre/<int:genre_id>/', show_genre, name='genre')
]