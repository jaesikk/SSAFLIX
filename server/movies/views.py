
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializer import MovieSerializer
# Create your views here.


@api_view(['GET'])
def movies(request):
    # 전체 영화 리스트를 가져온다.
    movie_list = get_list_or_404(Movie)
    # 해당 리스트를 직렬화 하여 json 화 한다. (many - 데이터가 1개가 아닌 여러 개)
    serializer = MovieSerializer(movie_list, many=True)
    # 요청에 대한 응답으로 json화 된 데이터를 보내준다.
    return Response(serializer.data)