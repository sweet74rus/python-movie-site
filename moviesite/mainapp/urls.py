from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', MovieHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('movie/<slug:movie_slug>/', ShowMovie.as_view(), name='movie'),
    path('genre/<slug:genre_slug>/', MovieGenre.as_view(), name='genre'),
    path('addmovie/', AddMovie.as_view(), name='add_movie'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout')
]