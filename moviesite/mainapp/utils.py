from .models import *


class DataMixin:
    paginate_by = 8

    def get_user_context(self, **kwargs):
        context = kwargs

        if 'current_genre' not in context:
            context['current_genre'] = 'Все жанры'

        return context