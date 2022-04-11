from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs

        if 'movies' not in context:
            context['movies'] = Movie.objects.all()

        if 'current_genre' not in context:
            context['current_genre'] = 'Все жанры'

        return context