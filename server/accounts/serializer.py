from rest_framework import serializers
from django.contrib.auth import get_user_model


# 현재 어떤 유저 모델인지 개발마다 다르기 때문에 get_user_model이라는 함수로 명확히 가져올 수 있도록함
User = get_user_model()

# 커스텀 유저 모델을 기반으로 직렬화 모델을 만드는데, 
# password는 보여줘선 안되는 부분이므로 사용만 가능하게끔 (read는 불가)
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password',)