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





## 210521

### 오전

- 회원가입 기능 구현, jwt를 통한 인증 토큰 발급, 검증 구현
- 장르 모델 생성 및 tmdb에서 데이터를 가져와 db에 넣음
- id check 기능 추가 리뷰 게시글 모델 작성 (리뷰 게시글 평점 validator 기능으로 최소 0 최대 10으로 제한을 둠)



### 오후

- 게시글 조회, 생성 기능 (review_list_create)
- 게시글 상세 조회, 수정, 삭제 기능 (review_update_delete)
- 리뷰 댓글 모델 작성, 시리얼라이저 작성, 리뷰 시리얼라이저에 댓글 목록도 함께 넘겨주도록 구성
- 리뷰 댓글, 리뷰 모델 모두 유저 추가
- 리뷰 댓글 목록 조회, 생성 기능 (review_comment_create)
- 리뷰 댓글 하나 조회, 삭제 기능 (review_comment_delete)
- 현재 문제점 - 세션을 따로 발급하지 않고 토큰으로만 관리하므로 어떤 유저인지 확실히 분간을 하지 못하는 거같음.. verify로 검증을 해야하나?
  - 즉 다른 유저가 어떤 사람이 쓴 리뷰나 댓글을 수정, 삭제가 가능한 문제가 있음 - 해결법 필요

