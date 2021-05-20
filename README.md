# README



## 210520



### 오전 

- 데이터 모델링, 기본적인 환경 변수 세팅, 데이터를 가져올 api 선택 중



- ERD 구축 - https://www.erdcloud.com/d/LQHA3fD8cx32DukCx



### 기본 개발 환경 설정

사용 개발 툴 - vscode, chrome browser

개발 환경 - windows 10 64bit

#### 프론트엔드

- 사용 버전
  - vue - 2.6.11
  - node.js - v14.16.1
  - vue/cli - 4.5.13

```bash
# 프론트엔드 세팅
$ vue create client
$ cd client
$ vue add router
$ vue add vuex
$ npm install axios
$ npm install lodash
```



#### 백엔드

- 사용 버전
  - python 3.8.7
  - requirements.txt에 있음 (참고)

```bash
# 백엔드 세팅
$ django-admin startproject server
$ cd server
$ python -m venv venv
$ source venv/Scripts/activate
$ pip install django djangorestframework djangorestfreamework-jwt django-cors-headers
$ pip freeze > requirements.txt
```

- settings.py에 기본 세팅



### 오후

- ERD를 기반으로한 모델 구성 (User, Movie, community, comment)
- User - custom user model + serializer, 세팅에 등록, admin 등록
- Movie - model 생성 + serializer 등록, admin 등록, movies페이지로 잘 보여주나 확인
- loaddata를 위한 get_movies.py 완성 - 도중에 한글이 유니코드로 나오는 이슈 발생 - 해결 (ensure_ascii=False)

```python
# formatting한 데이터를 json 파일로 저장
with open('movies.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(movie_list, ensure_ascii=False))
    # json.dump(movie_list, f, ensure_ascii=False)
```



