from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from . import views

# 앱이름 - 일종의 별명으로 지어서 다른 앱과 url 구분 (같은 url 명이라도 구분 가능하게 해줌)
app_name = 'accounts'

# ~/accounts/
urlpatterns = [
    # 토큰 부여를 위한 url
    path('api-token-auth/', obtain_jwt_token),
    # 해당 토큰이 유효한지 체크하는 url
    path('api-token-verify/', verify_jwt_token),
    # 회원 가입 url
    path('signup/', views.signup),
    # id 중복 체크 url
    path('id-check/', views.id_check),
    # 해당 유저에 팔로우
    path('<int:user_pk>/follow/', views.follow),
]
