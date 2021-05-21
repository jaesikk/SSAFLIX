import requests
import json

API_KEY = '031b6156fbe52ee9595fddf7b81190fa'
BASE_URL = 'https://api.themoviedb.org/3/genre/movie/list'

# movies.json으로 변환시켜 넣을 리스트
gerne_list = []

# request로 데이터 요청
response = requests.get(BASE_URL, { 'api_key': API_KEY, 'language': 'ko-KR'})
# response.encoding='utf-8'

# 받아온 데이터 json 파일을 딕셔너리 화
json_data = response.json() # Movie data
# print(json_data)

# 응답 받아온 데이터를 원하는 모양으로 formatting
for data in json_data.get('genres'):
    genre = {
        'model': 'movies.genre',
        'fields': {
            'name': data.get('name'),
            'genre_code': data.get('id'),
        }
    }
    gerne_list.append(genre)



# formatting한 데이터를 json 파일로 저장
with open('genres.json', 'w', encoding='utf-8') as f:
    # f.write(json.dumps(gerne_list, ensure_ascii=False))
    json.dump(gerne_list, f, ensure_ascii=False)