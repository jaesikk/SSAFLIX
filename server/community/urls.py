from django.urls import path
from . import views

app_name = 'community'

# ~/community/
urlpatterns = [
    # 리뷰 리스트 전체 조회, 생성
    path('create/', views.review_list_create),
    # 리뷰 상세 페이지 조회, 수정, 삭제
    path('<int:review_pk>/', views.review_update_delete),
    # 해당 게시글에 달린 댓글 목록 조회, 생성
    path('<int:review_pk>/comments/', views.review_comment_create),
    # 해당 게시글에 달린 특정 댓글 조회, 삭제
    path('<int:review_pk>/comments/<int:comment_pk>/', views.review_comment_delete),
    # 해당 게시글에 좋아요 기능
    path('<int:review_pk>/like', views.like),]
