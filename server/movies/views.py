
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Video
from .serializer import MovieSerializer, VideoSerializer
# Create your views here.

from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(['GET', 'POST'])
def movies(request):
    # print(request.GET)
    print(request.data)
    # print(request)
    # print(request.body)
    
    # 특정 영화 리스트를 가져온다.
    if request.data['query'] == 'popular':
        movie_list = get_list_or_404(Movie.objects.order_by('-popularity'))[:30]
        # movie_list = Movie.objects.values_list('popularity', flat=True).order_by('-popularity').distinct()[:30]
    elif request.data['query'] == 'topRated':
        movie_list = get_list_or_404(Movie.objects.order_by('-vote_average'))[:15]
    elif request.data['query'] == 'upcoming':
        movie_list = get_list_or_404(Movie.objects.order_by('-release_date'))[:15]
    else:
        return Response({'error': '잘못된 쿼리 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)
    # 해당 리스트를 직렬화 하여 json 화 한다. (many - 데이터가 1개가 아닌 여러 개)
    serializer = MovieSerializer(movie_list, many=True)
    # 요청에 대한 응답으로 json화 된 데이터를 보내준다.
    return Response(serializer.data)

@api_view(['GET'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
# 인증 여부 판단
@authentication_classes([JSONWebTokenAuthentication])
# 인증 확인 되었을 때만 권한 부여
@permission_classes([IsAuthenticated])
def videos(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    video_list = get_list_or_404(Video, tmdb_id=movie.tmdb_id)
    serializer = VideoSerializer(video_list, many=True)
    return Response(serializer.data)