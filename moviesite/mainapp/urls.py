from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('categories/<slug:category_name>/', categories),
    path('about/', about, name='about')
]