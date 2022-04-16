from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'get_html_image', 'genre')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'genre')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'genre', 'rating', 'movie_image', 'get_html_image', 'description')
    readonly_fields = ('get_html_image',)
    save_on_top = True

    def get_html_image(self, object):
        return mark_safe(f"<img src='{object.movie_image.url}' width=80>")

    get_html_image.short_description = 'Обложка'
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

admin.site.site_title = 'Админ-панель киносайта'
admin.site.site_header = 'Админ-панель киносайта'