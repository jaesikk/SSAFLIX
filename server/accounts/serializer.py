from rest_framework import serializers
from django.contrib.auth import get_user_model


# 현재 어떤 유저 모델인지 개발마다 다르기 때문에 get_user_model이라는 함수로 명확히 가져올 수 있도록함
User = get_user_model()

# 커스텀 유저 모델을 기반으로 직렬화 모델을 만드는데, 
# password는 보여줘선 안되는 부분이므로 사용만 가능하게끔 (read는 불가)
# 로그인 용
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)

# 로그인 외에도 팔로우 수나 포인트 등 다양한 기능
class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    # 팔로우 데이터를 얻기위해 커스텀 시리얼라이저 메소드로 가져오기
    # followData = serializers.DictField(child=serializers.CharField(), read_only=True)
    followData = serializers.SerializerMethodField()
    def get_followData(self, obj):
        return { 'followerCnt': obj.followers.count(), 'followingCnt': obj.followings.count(), }

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'followData', 'point')