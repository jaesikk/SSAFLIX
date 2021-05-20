# README



## 210520

- 오전 - 데이터 모델링, 기본적인 환경 변수 세팅, 데이터를 가져올 api 선택 중



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



