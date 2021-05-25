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
        # 전체 리뷰 리스트 반환
        review_list = Review.objects.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(serializer.data)
    else: # POST
        # 현재 들어온 요청 리뷰 데이터를 기반으로 유효성 검사 후 새롭게 생성
        serializer = ReviewSerializer(data=request.data)
        # print(serializer)
        # print(request.data)
        # print(serializer.is_valid())
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
# 리뷰 게시글 상세 조회 (버튼 누르면), 수정, 삭제
# 단 수정, 삭제는 작성 유저와 동일일 때
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    print(request.user)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        # 수정하려면 작성자 본인만 가능
        if request.user == review.user:
            # 원본 리뷰 객체 (id 식별)에 현재 데이터를 집어넣기
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({'error': '작성자와 같은 유저가 아닙니다.'}, status=status.HTTP_400_BAD_REQUEST)
    else: # DELETE
        if request.user == review.user:
            review.delete()
            return Response({ 'id': review_pk })
        else:
            return Response({'error': '작성자와 같은 유저가 아닙니다.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def review_comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        # 해당 리뷰에 달린 댓글 전체 조회
        comment_list = review.reviewcomment_set.all()
        serializer = ReviewCommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else: # POST
        serializer = ReviewCommentSerializer(data=request.data)
        # 유효성 검사, 통과못하면 400 에러
        if serializer.is_valid(raise_exception=True):
            # user, review는 외래키로 관리하고, request user부분과 review 부분에서 식별이 가능하므로 이렇게 적어야함.
            # 시리얼라이저는 두개를 읽는 용으로만 사용하므로 개발자가 직접 넣어줘야함.
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(ReviewComment, pk=comment_pk)
    serializer = ReviewCommentSerializer(comment)
    if request.method == 'GET':
        return Response(serializer.data)
    else: # DELETE
        # 작성자 본인일때만 삭제 가능
        if request.user == comment.user:
            comment.delete()
            return Response({ 'id': comment_pk })
        else:
            return Response({'error': '작성자와 같은 유저가 아닙니다.'})

@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    # GET - 좋아요 여부 반환
    if request.method == 'GET':
        # print(review.like_users.filter(pk=request.user.pk).exists())
        return Response({'isLike': review.like_users.filter(pk=request.user.pk).exists()})
    else: # POST - 좋아요 기능 
        # 작성글 유저와 현재 접속한 유저가 다를 때만 좋아요 기능 활성화
        if request.user != review.user:
            # 기존에 요청이 들어온 Like의 반대로 보냄
            # 지금 좋아요를 누른 상태면 삭제
            if review.like_users.filter(pk=request.user.pk).exists():
                review.like_users.remove(request.user)
                return Response({'isLike': False})
            # 좋아요를 누르지 않은 상태면 추가
            else :
                review.like_users.add(request.user)
                return Response({'isLike': True})
        # 작성글 유저와 접속한 유저가 같음 = 본인이므로 좋아요 못하게 막음
        return Response({'error': '본인 글에는 좋아요를 할 수 없습니다.'})
    