from django.urls import path
from . import views
app_name = 'movies'

urlpatterns = [
    # ~/movies/
    path('', views.movies, name="movies"),
    path('<int:movie_pk>/', views.movie_detail, name="movie_detail"),
]
