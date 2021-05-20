# README_재식

## 수행

> - 환경 세팅을 한 후에, index.html에 `bootstrap`과 `font`의 link를 불러왔습니다.
> - 라우터를 이용하여 3개의 vue를 views 폴더에 생성하여 각 페이지를 만들었습니다.
> - router/index.js에 url을 router-link와 연결했습니다.

> - `.env.local`에 SERVER_URL을 저장하고 Django에서 movie db를 받아와 Home.vue에 출력하였습니다.
> - 출력을 위해 vuex에서 저장한 json을 MovieCare.vue에서 v-for문으로 사용했습니다.

## 어려웠던 점

> 초기 환경설정부터 구조적으로 설계하지 않으면 구현에 있어 상당히 헷갈리고 어수선하다는 것을 느꼈습니다. 여러 폴더와 파일을 넘나들며 데이터를 주고 받음에 있어서 어려움을 겪었습니다.
> 최적화를 위해 bootstrap과 font를 적재적소에 배치시키고, vuex를 보다 짜임있게 구성하는데 연습이 필요하다고 느꼈습니다.
> 그래도 일단은 백엔드와 프론트엔드를 연결하여 1차적으로 db를 출력하는 결과를 확인할 수 있었습니다.

