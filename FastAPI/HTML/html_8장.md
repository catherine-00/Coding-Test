# 8.1 의미론적인 태그
## 시맨틱(semantic) 태그
- 시맨틱 태그 = 의미론적인 태그
    + 이름만으로 해당 태그가 문서에서 어떤 역할을 하는지 쉽게 파악할 수 있는 태그
- `<mark>`, `<strong>`, `<em>`, `<iframe>`, `<progress>` 등 모두 시맨틱 태그임
- 추가적인 시맨틱 태그 알아보자

## 문서 구조를 위한 시맨틱 태그
- `<div>` 처럼 출력 화면에는 나타나지 않음
- 시맨틱 태그를 이용해 머릿말, 본문, 보조 정보 등을 나눠 놓으면 관리하기 쉬움
### `<section>` : 영역 구분
- 연관딘 콘텐츠를 묶어 영역을 구분하는데 사용
### 영역 구분을 위한 `<article>`
- 독립적으로 사용할 수 있는 연관 콘텐츠를 구분할 때 사용
- `<section>`보다 구체적인 내용을 담는 태그
### 보조 정보를 위한 `<aside>`
- 본문 내용과 연관성이 적거나 관게가 없는 보조 정보를 나타내기 위해 사용하는 태그
- 본문 옆에 간단하게 표시되는 사이드바를 만들거나 광고 배너 등을 포함하는데 사용
### 머릿말을 지정하는 `<header>`
- 웹 페이지에 대한 대표적인 설명글 또는 머릿말 등을 나타낼 때 사용
- 검색 엔진의 검색에 참고가 되는 중요한 자료로써 사용됨
- 여러 번, 다른 섹션 안에 써도 됨
### 네비게이션 링크 `<nav>`
- 링크로 이어지는 사이트 탐색 정보, 즉 네비게이션 메뉴를 표쇠함
```html
<body>
  <header>
    <nav>
      <ul>
        <li><a href="home.html">홈</a></li>
        <li><a href="news.html">뉴스</a></li>
        <li><a href="finance.html">증권</a></li>
        <li><a href="land.html">부동산</a></li>
      </ul>
    </nav>
  </header>
</body>
```
<body>
  <header>
    <nav>
      <ul>
        <li><a href="home.html">홈</a></li>
        <li><a href="news.html">뉴스</a></li>
        <li><a href="finance.html">증권</a></li>
        <li><a href="land.html">부동산</a></li>
      </ul>
    </nav>
  </header>
</body>

#### 요약글을 나타내는 `<footer>`
- 페이지를 만든 사람, 저작권 정보, 연관 링크 등을 표시하는 역할을 함

# 8.2 메타데이터
## `<meta>` : 문서 정보 추가하기
- 메타데이터를 표현하기 위해 사용하는 태그
- 메타데이터 : 데이터에 대한 데이터. 즉, HMTL문서에 대한 데이터
- 문서 정보를 나타내므로 `<head>` 태그 내부에 추가해줘야 한다.
```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <!-- 이미 사용해 본 적 있는 meta 태그 -->
    <meta charset="utf-8">
    <title>문서의 제목</title>
  </head>
  <body>
  </body>
</html>
```
- `<meta charset="utf-8">` : 문서의 문자셋 정보를 추가해 다양한 문자를 인코딩할 수 있도록 설정한 것
- `<meta>`는 주로 결과 화면이 아닌 브라우저에 문서의 정보를 전달하는 역할을 한다.
- 함께 쓸 수 있는 속성
    + `name` : 지정할 메타데이터의 이름(유형)을 지정합니다.
    + `content` : 메타데이터 설정 값을 지정합니다. name과 짝을 이루어 적용되곤 합니다.
    + `charset` : 문자 인코딩을 나타내는 "문자 집합 선언"을 지정합니다.
    + `http-equiv` : HTTP 헤더가 제공하는 정보와 동일한 "프래그마 지시문"을 설정합니다.
- `<meta>` 태그를 이용하면, 웹 페이지의 서비스 품질을 올릴 수 있다. 검색 엔진이 웹 페이지를 검색하는데 유용한 정보로 활용한다. 브라우저 호환성 이슈를 해결하거나 웹 접근성 향상시킴

## 표준 메타데이터 사용 예
- 표준 메타데이터 : HTML 표준 명세를 비롯한 웹 페이지 관련 명세에는 사용가능한 메타데이터 이름과 값들이 정의되어 있다.
    + 명세 : 사용법을 정리한 문서
### 문서 제작자 정보를 나타내는 `name="author"`
- 문서를 작성한 사람에 대한 정보를 추가하는 메타데이터 이름
```html
<meta name="author" content="my name">
```
### 웹페이지에 대한 설명을 추가하는 `name="description"`
- 페이지에 대한 짧고 정확한 요약을 추가하는 메타데이터.
- 여러 브라우저에서 즐겨찾기 페이지의 기본 설명값으로 description의 값을 사용하기도
```html
<meta name="description" content="강윤호의 일상 이야기를 담고 있는 블로그입니다.">
```
### 키워드 목록을 추가하는 `name="keywords"`
- 웹 페이지의 콘텐츠와 관련된 키워드를 원하는 개수만큼 추가할 수 있음
- 키워드 간 구분을 위해 쉼표 이용
```html
<meta name="keywords" content="animal, cat, dog, puppy, kitty">
```

### 모바일기기에서 사용을 위한 `name="viewport"`
- PC 화면에서 보이는 페이지를 모바일 기기에서 보기 위해 추가하는 정보
- `viewport` : 기기의 화면 상에서 콘텐츠가 표시되는 영역
- PC 화면과 모바일 화면은 뷰포트 크기 자체가 다름, 또 그 안에서 화소(픽셀)를 표현하는 규모 또한 다름
- 이런 문제를 해결하는 메타데이터임
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
- `device-width` : 기기의 너비에 맞춤
- `initial-scale` : 초기 화면 배율. 보통 1
- 보통 `content="width=device-width, initial-scale=1.0"`로 많이 설정함
- 기타 속성값
    + `height` : 웹 페이지를 렌더링 하고자 하는 viewport의 높이
    + `maximum-scale` : 가능한 최대 확대 비율
    + `minimum-scale` : 가능한 최소 확대 비율.
    + `user-scalable` : 사용자가 웹 페이지를 확대할 수 있는지 여부 지정하기. yes 또는 no로 결정합니다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="author" content="강윤호">
  <meta name="description" content="예시를 위해 만들어 본 페이지입니다.">
  <meta name="keywords" content="메타데이터, meta, HTML, 프론트엔드, 웹 개발">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>메타데이터란 이런 것이다</title>
</head>
<body>
  <h1>표준 메타데이터 이름</h1>
  <p>
    &lt;meta&gt; 태그는 name 속성을 메타데이터의 이름으로, content 속성을 값으로 하여 메타데이터를 추가합니다. HTML 표준 명세를 비롯한 웹 페이지 관련 명세에는 사용 가능한 메타데이터 이름과 값들이 정의되어 있는데, 이를 '표준 메타데이터'라 합니다. 여기에서는 대표적인 표준 메타데이터 몇 가지를 알아보겠습니다.
  </p>
</body>
</html>
```