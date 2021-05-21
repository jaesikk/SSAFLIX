from django.db.models import fields
from rest_framework import serializers
from .models import Review, ReviewComment

class ReviewCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewComment
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    reviewcomment_set = ReviewCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Review
        fields = '__all__'

