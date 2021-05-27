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



## 210523

- 코드 주석 추가 100%는 아님
- 좋아요 기능 만들기 시작
- 리뷰 데이터 이슈 해결





## 210524

- 세세한 오타 수정
- 좋아요 기능 완성



- vuex-persistedstate를 통해 외부 관리 시작 (vuex에 유저 정보 유지하도록)
- axios.defaults.headers.common['Authorization'] vuex로 관리 시에 등록이 안되는 문제 발생
  - vuex의 actions에서 context로 데이터를 접근해서 바꿈
  - console.log로 출력시 안되는 이유 - vuex에서 값을 넣는 시간보다 출력시간이 더빠름 
- ReviewDetail에 수정, 삭제 기능 추가
- 팔로워 기능 개발 시작 - 모델, 시리얼라이저, 뷰 작성





## 210525

- 코드에 주석 추가
- 랜덤 추천 페이지 작성
- 영화 상세 페이지 뷰 작성 (django)
- 프로필 페이지 수정 (기본 제공 틀에서)
- 유저 디테일 뷰 작성
- 팔로우 정보를 담아주는 팔로우 데이터을 유저 시리얼라이저에 추가, 프로필과 연결
- movie 모델 - tmdb_id 추가, video 모델 작성, 새롭게 데이터 뽑도록 수정 (get_movies.py) 
  - 인기영화, 평점 높은 영화, 개봉예정 영화 3개 파트 + 영화에 들어간 영상 정보를 video 모델에 작성
  - 문제점 - video에 movie.tmdb_id를 외래키로 삼으려고 했는데 loaddata할 때 고유키 문제와 video에 연결이 안되는 문제 -> 그냥 별도의 video 모델로 두고 사용



## 210526

- 영화 상세 페이지 작성
- 영화 상세 페이지에서 동영상 기능 추가 (carousel) 
  - 문제가 많음
- vuex store를 userStore, movieStore로 모듈화
  - 문제가 많이 발생;
  - mapState 사용시 ...mapState(store_name, ['store_state_name']) 으로 사용해야함 혹시 중복된 state이름이 나오면 어떻게 될지는 모르겠음
  - dispatch 사용시 $store.dispatch('store_name/action_name', parameter) 로 사용
  - commit 하는 부분에 데이터를 2개 이상 보내려면 payload로 보내야됨 (commit_name, {data1: data, data2: data}) 이런식으로 사용할 때도 payload.data1, payload.data2 이런식으로 접근해서 사용



## 210527

- 프로젝트 마무리
  - 포인트 제도 추가
  - 
