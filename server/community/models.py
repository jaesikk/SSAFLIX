from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# 영화 리뷰 게시글 모델
class Review(models.Model):
    title = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 기본 평점 5 최소 0 최대 10
    rank = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])