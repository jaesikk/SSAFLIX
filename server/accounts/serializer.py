from community.sertializer import ReviewSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.models import Review

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

    # review_like_Data = serializers.SerializerMethodField()
    # def get_review_like_Data(self, obj):
    #     return { 'reviewData': Review.objects.value_lists(pk=obj.pk), 'likeData': obj.like_reviews.value_lists(), }
    # 내가 쓴 글 리스트 - reviews
    reviews = ReviewSerializer(read_only=True, many=True)
    # 내가 좋아요 한 글 리스트 - like_reviews
    like_reviews = ReviewSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'followData', 'point', 'reviews', 'like_reviews', )