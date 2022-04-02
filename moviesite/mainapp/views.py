from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return HttpResponse('Страница киносайта')

def categories(request):
    return HttpResponse('<h1>Категории фильмов</h1>')