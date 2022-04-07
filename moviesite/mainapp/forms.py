from django import forms
from .models import *


class AddMovieForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название фильма', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    slug = forms.SlugField(max_length=255, label='URL', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    rating = forms.FloatField(label='Рейтинг', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label='Жанр', empty_label='Жанр не выбран', widget=forms.Select(attrs={
        'class':'form-control',
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 60,
        'rows': 10,
        'class': 'form-control'
    }), label='Описание фильма')