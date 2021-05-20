import requests
import json

API_KEY = '031b6156fbe52ee9595fddf7b81190fa'
BASE_URL = 'https://api.themoviedb.org/3/movie/popular/'

# movies.json으로 변환시켜 넣을 리스트
movie_list = []


for i in range(1, 4):  
    # request로 데이터 요청
    response = requests.get(BASE_URL, { 'api_key': API_KEY, 'language': 'ko-KR', 'page': i })
    # response.encoding='utf-8'
    
    # 받아온 데이터 json 파일을 딕셔너리 화
    json_data = response.json() # Movie data
    # print(json_data)

    # 응답 받아온 데이터를 원하는 모양으로 formatting
    for data in json_data.get('results'):
        movie = {
            'model': 'movies.movie',
            'fields': {
                'title': data.get('title'),
                'overview': data.get('overview'),
                'poster_path': data.get('poster_path'),
                'release_date': data.get('release_date'),
                'popularity': data.get('popularity'),
                'vote_count': data.get('vote_count'),
                'vote_average': data.get('vote_average'),
            }
        }
        # print(movie)
        # print(movie_list)
        movie_list.append(movie)



# formatting한 데이터를 json 파일로 저장
with open('movies.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(movie_list, ensure_ascii=False))
    # json.dump(movie_list, f, ensure_ascii=False)