from django.urls import path
from . import views

app_name = 'community'

# ~/community/
urlpatterns = [
    path('create/', views.review_list_create),
    path('<int:review_pk>/', views.review_update_delete),
    path('<int:review_pk>/comments/', views.review_comment_create),
    path('<int:review_pk>/comments/<int:comment_pk>/', views.review_comment_delete),
]
