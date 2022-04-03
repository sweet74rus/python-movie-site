from django.db import models

class Movie(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название фильма')
    movie_image = models.ImageField(verbose_name='Обложка фильма')
    rating = models.FloatField(verbose_name='Рейтинг фильма')
    genre = models.CharField(max_length=255, verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание фильма')

    def __str__(self):
        return self.title