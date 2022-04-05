from django.db import models
from django.urls import reverse


class Movie(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название фильма')
    movie_image = models.ImageField(verbose_name='Обложка фильма')
    rating = models.FloatField(verbose_name='Рейтинг фильма')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание фильма')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', kwargs={'movie_id': self.pk})

    class Meta:
        verbose_name_plural = 'Фильмы'


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Жанр')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'
        ordering = ['id']