import requests
import json

API_KEY = '031b6156fbe52ee9595fddf7b81190fa'
BASE_URL = 'https://api.themoviedb.org/3/movie/'


def get_movie_data(url_string, range_cnt, save_movieList_name, save_videoList_name):
    movie_list = []
    video_list = []
    for i in range(1, range_cnt):  
        # request로 데이터 요청
        response = requests.get(BASE_URL + f'{url_string}', { 'api_key': API_KEY, 'language': 'ko', 'page': i, 'region': 'kr' })
        # response.encoding='utf-8'
        
        # 받아온 데이터 json 파일을 딕셔너리 화
        json_data = response.json() # Movie data
        # print(json_data)

        # 응답 받아온 데이터를 원하는 모양으로 formatting
        for data in json_data.get('results'):
            tmdb_id = data.get('id')
            res = requests.get(BASE_URL + f'{tmdb_id}/videos', { 'api_key': API_KEY, 'language': 'ko-KR' })
            res_json = res.json()
        
            for res_data in res_json.get('results'):
                video = {
                    'model': 'movies.video',
                    'fields': {
                        'tmdb_id': res_json.get('id'),
                        'name': res_data.get('name'),
                        'key': res_data.get('key'),
                        'site': res_data.get('site'),
                    }
                }
                video_list.append(video)
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
                    'tmdb_id': data.get('id'),
                }
            }
            # print(movie)
            # print(movie_list)
            movie_list.append(movie)

    # formatting한 데이터를 json 파일로 저장
    with open(f'{save_movieList_name}', 'w', encoding='utf-8') as f:
        f.write(json.dumps(movie_list, ensure_ascii=False))
        # json.dump(movie_list, f, ensure_ascii=False)
    # formatting한 데이터를 json 파일로 저장
    with open(f'{save_videoList_name}', 'w', encoding='utf-8') as f:
        f.write(json.dumps(video_list, ensure_ascii=False))
        # json.dump(movie_list, f, ensure_ascii=False)


get_movie_data('popular', 3, 'popular_movies.json', 'popular_videos.json')
get_movie_data('top_rated', 2, 'top_rated_movies.json', 'top_rated_videos.json')
get_movie_data('upcoming', 2, 'upcoming_movies.json', 'upcoming_videos.json')


# # movies.json으로 변환시켜 넣을 리스트
# movie_list = []


# for i in range(1, 4):  
#     # request로 데이터 요청
#     response = requests.get(BASE_URL + 'popular', { 'api_key': API_KEY, 'language': 'ko', 'page': i, 'region': 'kr' })
#     # response.encoding='utf-8'
    
#     # 받아온 데이터 json 파일을 딕셔너리 화
#     json_data = response.json() # Movie data
#     # print(json_data)

#     # 응답 받아온 데이터를 원하는 모양으로 formatting
#     for data in json_data.get('results'):
#         movie = {
#             'model': 'movies.movie',
#             'fields': {
#                 'title': data.get('title'),
#                 'overview': data.get('overview'),
#                 'poster_path': data.get('poster_path'),
#                 'release_date': data.get('release_date'),
#                 'popularity': data.get('popularity'),
#                 'vote_count': data.get('vote_count'),
#                 'vote_average': data.get('vote_average'),
#             }
#         }
#         # print(movie)
#         # print(movie_list)
#         movie_list.append(movie)



# # formatting한 데이터를 json 파일로 저장
# with open('movies.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(movie_list, ensure_ascii=False))
#     # json.dump(movie_list, f, ensure_ascii=False)


# popular_movie_list = []
# videos = []

# for i in range(1, 2):  
#     # request로 데이터 요청
#     response = requests.get(BASE_URL + 'top_rated', { 'api_key': API_KEY, 'language': 'ko', 'page': i, 'region': 'kr' })
#     # response.encoding='utf-8'
    
#     # 받아온 데이터 json 파일을 딕셔너리 화
#     json_data = response.json() # Movie data
#     # print(json_data)

#     # 응답 받아온 데이터를 원하는 모양으로 formatting
#     for data in json_data.get('results'):
#         tmdb_id = data.get('id')
#         res = requests.get(BASE_URL + f'{tmdb_id}/videos', { 'api_key': API_KEY, 'language': 'ko-KR' })
#         res_json = res.json()
    
#         for res_data in res_json.get('results'):
#             video = {
#                 'movie': res_json.get('id'),
#                 'name': data.get('name'),
#                 'key': data.get('key'),
#                 'site': data.get('site'),
#             }
#             videos.append(video)
#         movie = {
#             'model': 'movies.movie',
#             'fields': {
#                 'title': data.get('title'),
#                 'overview': data.get('overview'),
#                 'poster_path': data.get('poster_path'),
#                 'release_date': data.get('release_date'),
#                 'popularity': data.get('popularity'),
#                 'vote_count': data.get('vote_count'),
#                 'vote_average': data.get('vote_average'),
#                 'tmdb_id': data.get('id'),
#             }
#         }
#         # print(movie)
#         # print(movie_list)
#         popular_movie_list.append(movie)



# # formatting한 데이터를 json 파일로 저장
# with open('top_rated_movies.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(popular_movie_list, ensure_ascii=False))
#     # json.dump(movie_list, f, ensure_ascii=False)

# upcoming_movie_list = []

# for i in range(1, 2):  
#     # request로 데이터 요청
#     response = requests.get(BASE_URL + 'upcoming', { 'api_key': API_KEY, 'language': 'ko', 'page': i, 'region': 'kr' })
#     # response.encoding='utf-8'
    
#     # 받아온 데이터 json 파일을 딕셔너리 화
#     json_data = response.json() # Movie data
#     # print(json_data)

#     # 응답 받아온 데이터를 원하는 모양으로 formatting
#     for data in json_data.get('results'):
#         movie = {
#             'model': 'movies.movie',
#             'fields': {
#                 'title': data.get('title'),
#                 'overview': data.get('overview'),
#                 'poster_path': data.get('poster_path'),
#                 'release_date': data.get('release_date'),
#                 'popularity': data.get('popularity'),
#                 'vote_count': data.get('vote_count'),
#                 'vote_average': data.get('vote_average'),
#             }
#         }
#         # print(movie)
#         # print(movie_list)
#         upcoming_movie_list.append(movie)



# # formatting한 데이터를 json 파일로 저장
# with open('top_rated_movies.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(upcoming_movie_list, ensure_ascii=False))
#     # json.dump(movie_list, f, ensure_ascii=False)