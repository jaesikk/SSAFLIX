from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Movie
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'popularity', 'vote_count', 'vote_average', 'overview', 'poster_path', 'tmdb_id']


admin.site.register(Movie, MovieAdmin)