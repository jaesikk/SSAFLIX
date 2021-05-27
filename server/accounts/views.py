from django.shortcuts import render, get_object_or_404
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth import get_user_model

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# id 중복 확인 체크 기능

# 회원 가입은 POST 요청으로만 진입 가능(회원 가입이므로)
@api_view(['POST'])
def signup(request):
    # 비밀번호와 비밀번호 확인을 client 요청 데이터에서 꺼내기
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
    is_id_check = request.data.get('idCheck')

    # id 중복을 확인하지 않았다 -> 확인하라고 돌려보냄
    if not is_id_check:
        return Response({'error': 'ID 중복 확인이 되지 않았습니다. 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)

    # 비밀번호와 비밀번호 확인, 다르다 -> 잘못 입력
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다. 다시 입력해 주세요.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 직렬화 작업(외부 데이터를 가져왔을 땐 딕셔너리 화를 통해 적절히 처리해줌)
    serializer = UserSerializer(data=request.data)

	# 유효성 검사 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        # 비밀번호 해싱 - 암호화(이것을 사용하지 않으면 관리자 페이지에서 알 수 없는 알고리즘이라고 뜸 
        # - 장고의 암호화 알고리즘에 맞게 패스워드를 변환) 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 write_only 이므로 직렬화 과정에는 포함 되지만 표현(response)할 때는 나타나지 않는다. 
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def id_check(request):
    # id 데이터를 request에서 꺼내기
    request_username = request.data.get('username')
    # 현재 user 테이블 안에 같은 유저 id명이 존재할 경우
    if User.objects.filter(username=request_username):
        return Response({'error': '중복된 ID입니다. 다른 ID를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
    else:   
        return Response({'accept': '중복되지 않은 ID 입니다. 사용 가능합니다.'}, status=status.HTTP_200_OK)

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
        # 'userId': user.pk
    }

@api_view(['GET', 'POST'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    # 현재 팔로우 될 유저 객체(요청 받은 아이디 = 대상)
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 현재 팔로우 할 유저 객체(현재 접속 중인 유저 = 나)
    user = request.user
    if request.method == 'GET':
        # 현재 해당 유저의 팔로우 여부 반환
        return Response({'isFollow': person.followers.filter(pk=user.pk).exists()})
    else: # POST
        # 현재 접속한 유저가 자신에게 팔로우하는 것을 막기
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                isFollow = False
            else:
                person.followers.add(user)
                isFollow = True
            followData = {
                # 'follow' : follow,
                'fiCnt' : user.followers.count(),
                'fwCnt' : user.followings.count(),
            }
            # return Response(response_data, status=200)
            return Response({'isFollow': isFollow, 'followData': followData})
        return Response({'error': '본인 계정에는 팔로우를 할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def user_detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    followData = {
        # 'follow' : follow,
        'fiCnt' : user.followers.count(),
        'fwCnt' : user.followings.count(),
    }
    print(UserSerializer)
    # serializer = UserSerializer(user, followData=followData)
    serializer = UserSerializer(user)
    print(serializer)
    return Response(serializer.data)


