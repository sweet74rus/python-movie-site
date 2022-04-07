from django import forms
from .models import *


class AddMovieForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название фильма')
    slug = forms.SlugField(max_length=255, label='URL')
    rating = forms.FloatField(label='Рейтинг')
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанр')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 60,
        'rows': 10,
    }), label='Описание фильма')