from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 커스텀 유저 모델은 기존 유저모델에서 상속받아 재생성 
# (추후에 유저 모델을 커스텀 할 필요가 있을 것 같으면 반드시 프로젝트 초기에 미리 설정할 것을 권장)
class User(AbstractUser):
    pass

