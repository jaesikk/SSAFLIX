from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Review, ReviewComment
from .sertializer import ReviewCommentSerializer, ReviewSerializer

@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def review_list_create(request):
    if request.method == 'GET':
        review_list = request.user.reviews
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    else: # POST
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else: # DELETE
        review.delete()
        return Response({ 'id': review_pk })


@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comment_list = review.reviewcomment_set.all()
        serializer = ReviewCommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else: # POST
        serializer = ReviewCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def review_comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(ReviewComment, pk=comment_pk)
    serializer = ReviewCommentSerializer(comment)
    if request.method == 'GET':
        return Response(serializer.data)
    if request.user == comment.user:
        comment.delete()
        return Response({ 'id': comment_pk })
    else:
        return Response({'error': '작성자와 같은 유저가 아닙니다.'})
