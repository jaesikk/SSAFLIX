from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 커스텀 유저 모델이지만 기본 UserAdmin을 통해 기본 속성을 보여주거나 관리 가능
admin.site.register(User, UserAdmin)
