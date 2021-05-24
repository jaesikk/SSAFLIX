from django.db.models import fields
from rest_framework import serializers
from .models import Review, ReviewComment

# exclude와 fields는 둘 중에 하나만 사용해야 한다.

class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        # fields = '__all__'
        # 유저는 외래키이고, 우리가 별도로 입력해서 넣는 것이 아닌 
        # request.user를 통해 해당 유저를 식별해서 넣을 것이므로 관리 X
        exclude = ('user', )

class ReviewSerializer(serializers.ModelSerializer):

    reviewcomment_set = ReviewCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Review
        # fields = ('id', 'title', 'movie_title', 'content', 'rank',)
        # fields = '__all__'
        # 유저는 외래키이고, 우리가 별도로 입력해서 넣는 것이 아닌 
        # request.user를 통해 해당 유저를 식별해서 넣을 것이므로 관리 X
        exclude = ('user', 'like_users',)

