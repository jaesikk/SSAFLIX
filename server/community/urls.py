from django.urls import path
from . import views

app_name = 'community'

# ~/community/
urlpatterns = [
    path('create/', views.review_list_create),
    path('<int:review_pk>/', views.review_update_delete),
]
