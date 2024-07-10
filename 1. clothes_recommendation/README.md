온도에 따른 옷 추천 어플리케이션

- 목표
    - MVC를 통한 프로젝트 관리 | X
    - 프론트, 백 간 연결 구현 및 이해 | O
    - api를 활용하여 gpt 실습 | O

- 프로젝트 개요
    - https://concho.tistory.com/46 참조
    - 네이버 날씨를 crawling하여 온도 확인
    - gpt api로 사용자의 input 분석 및 옷 추천
    - dalle2로 추천받은 옷을 이미지로 생성
    - vue, flask를 통해 프론트, 백 구현

- 개선점
    - 에러 처리를 하지 않음
    - 온도를 받아올 때 현재 시각 이후의 시간만 가능. ex) 현재 시각이 23시 1분 일 때 에러
    - gpt를 통해 추천을 받을 때 날씨(맑음, 비 등)를 제외한 온도만 고려

- 참조
    - https://concho.tistory.com/46
    - https://wikidocs.net/232187