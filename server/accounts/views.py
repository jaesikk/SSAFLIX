from django.shortcuts import render
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User

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


@api_view(['GET'])
def id_check(request):
    # id 데이터를 request에서 꺼내기
    request_username = request.data.get('username')
    if User.objects.filter(username=request_username):
        return Response({'error': '중복된 ID입니다. 다른 ID를 입력해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'accept': '중복되지 않은 ID 입니다. 사용 가능합니다.'}, status=status.HTTP_200_OK)
