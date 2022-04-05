from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'genre')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'genre')

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
