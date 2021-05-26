from django.db import models
import uuid

# 장르 코드와 이름을 가진 장르 테이블
class Genre(models.Model):
    name = models.CharField(max_length=50)
    genre_code = models.IntegerField()

# Movie 모델 생성
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    # tmdb_id = models.IntegerField(unique=True, default=uuid.uuid4)
    tmdb_id = models.IntegerField()
    # genres = models.ManyToManyField(Genre)
    
class Video(models.Model):
    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE, to_field='tmdb_id', db_column='movie_tmdb_id')
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=200)
    site = models.CharField(max_length=50)