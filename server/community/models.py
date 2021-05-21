from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# 영화 리뷰 게시글 모델
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 기본 평점 5 최소 0 최대 10
    rank = models.PositiveIntegerField(default=5, validators=[MinValueValidator(0), MaxValueValidator(10)])

# 영화 리뷰 게시글의 댓글 모델
class ReviewComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)