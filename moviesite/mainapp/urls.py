from django.urls import path
from mainapp.views import *

urlpatterns = [
    path('', main_page),
    path('categories', categories)
]