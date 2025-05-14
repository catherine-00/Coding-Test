## 4.1 이미지 태그
### `<img>` : 이미지 표시하기
- 웹 문서에 이미지를 추가할 때 사용
- 단일 태그 
    + = 닫는 태그 없음
    + 콘텐츠 입력 x
- `<img>` 태그를 사용해 표시할 이미지를 지정할 때는 `src` 속성에 이미지의 URL을 입력하는 방식을 사용
```html
<img src="IMAGE_URL">
```
- 이미지를 표시하기 위해선
    + 표시할 이미지가 실제로 존재해야 함
    + 해당 이미지가 존재하는 위치와 이미지 파일의 이름 등을 입력해야 함
```html
<body>
  <h1>위키독스 소개글 대표이미지</h1>
  <img src="https://wikidocs.net/images//book/wikidocs_1_5nYDT0Q.png">
  <p>위키독스라는 훌륭한 플랫폼을 알게되어 영광입니다 ㅎㅎ 이미지는 아마도 화분인 것 같습니다!</p>
</body>
```

### 파일 위치 지정하기
- `src` 속성에 웹 서버 주소가 아니라, 사용자의 컴퓨터에 저장되어 있는 이미지 파일위 위치를 지정하는 경우도 있다.
- 정확하게 위치를 지정해줘야한다.

#### 이미지가 웹 문서와 같은 폴더 내에 있을 때
- 이미지 위치 = 웹 문서의 위치
- 이미지 파일의 이름만 작성 or
- `./` 문자열을 사용해서 '동일한 폴더에 있다'는 표시를 해줌
```html
<img src="penguin.png">  
<img src="./penguin.png">  
```

#### 이미지가 웹 문서의 상위 폴더 또는 하위 폴더에 있을 때
- 이미지 위치 != 웹 문서 위치
- 상대 경로로 지정
    - 이미지가 웹 문서보다 **상위 폴더**에 있을 때
        + 이미지 파일명 앞에 `../`을 입력
        ```html
        <img src="../penguin.png">  
        ```
    - 이미지가 웹 문서보다 **하위 폴더**에 있을 때
        + 이미지 파일명 앞에 `하위 폴더명`을 입력
        ```html
        <img src="하위폴더명/penguin.png">  
        <img src="./하위폴더명/penguin.png">  
        ```
- 절대 경로로 지정
    + 이미지 파일 위치가 웹 문서 위치와 너무 동떨어져 있을 때 절대경로로 지정
    ```html
    <img src="C:\images\penguin.png">  
    ```

### `alt` : 대체 텍스트 추가하기
- `alt` 속성은 이미지의 대체 텍스트를 입력하는 속성
- 대체 텍스트 : 이미지가 아직 로드되지 않았거나 이미지 로드에 실패한 경우 이미지를 대신해 표시될 텍스트
```html
<body>
  <img src="penguin.png" alt="이미지를 대신해 내가 등장!"> 
  <img src="no_penguin.png" alt="이미지를 대신해 내가 등장!"> 
</body>
```

### `width`, `height` : 이미지 크기 정하기
- `<img>` 태그는 기본적으로 이미지는 원본 크기로 출력한다.
- 이미지 크기를 정하고 싶을 때, `width`와 `height` 속성을 사용해 크기를 변경할 수 있다.
- 속성값은 **정수값**을 입력한다.
- 각각에 대해 픽셀(px) 단위로 적용된다.
```html
<body>
  <img src="penguin.png" width="250" height="100"> 
  <img src="penguin.png" width="100" height="100"> 
</body>
```


## 4.2 이미지를 표시하는 새로운 방법
### `<figure>`, `<figcaption>` : 자막이 있는 이미지 만들기
- 자막을 담당하는 `<figcaption>` 태그와 콘텐츠(이미지) `<img>`태그가 `<figure>` 태그에 포함되는 방식으로 사용
    + 자막과 콘텐츠를 함께 관리하기 좋음
    + `<figure>` 태그를 이용해 표시한 콘텐츠는 왼편에 조금의 여백이 추가됨
```html
<body>
  <figure>
    <img src="penguin.png">
    <figcaption>귀여운 펭귄의 따봉</figcaption>
  </figure>
</body>
```
- `<figcaption>` 요소로 자막을 추가할 때는 `<br>`을 추가하지 않아도 줄바꿈이 된다.

### `<picture>`, `<source>` : 여러 이미지 중 선택하게 하기
- `<picture>` : 이미지 소스를 감싸는 역할
- `<source>` : `<picture>` 태그 안에 여러 개의 `<source>` 태그를 사용해 화면 크기 별로 사용할 수 있는 여러 개의 이미지를 포함시킬 수 있음.
```html
<body>
  <picture>
    <source media="(max-width: 375px)" srcset="image1.png">
    <source media="(max-width: 768px)" srcset="image2.png">
    <source media="(max-width: 1024px)" srcset="image3.png">
  </picture>
</body>
```
- 예제에 하나의 `<picture>` 태그의 안에 세 개의 `<source>` 태그를 포함하면, 결과가 렌더링되는 화면의 크기에 따라 세 이미지 중 하나의 이미지 만이 선택되어 화면에 표시됨
    + `media` : 화면 크기에 대한 조건을 지정하는 속성
    + `max-width` : 최대 크기. 최대 크기가 375px인 것은 375px 이하라는 조건을 의미
    + `srcset` : 이미지의 URL을 지정할 수 있는 속성
    + 즉, 375px 이하의 화면에서는 image1.png를, 375px 이상 768px 이하의 화면에서는 image2.png를 화면에 표시

- 오래된 브라우저에서는 `<picture>`이 사용 불가한 경우가 있다.
    + 그럴때는 내부에 `<img>`를 추가해주면, `<picture>`와 `<source>`를 무시하고 `<img>`를 토대로 출력한다.
    + 따라서, `<picture>` 안에 `<img>`를 하나씩 추가해주는 습관을 들이면 좋다.




## 4.3 링크 만들기
### `<a>`, `href` : 문서의 이동
- 연결 링크 요소를 만들어주는 태그
- 인라인 요소
- 다른 페이지나 같은 페이지의 어느 위치, 파일, 이메일 주소와 그 외 다른 URL로 연결
- `<a>` 태그 내부에 포함된 콘텐츠를 클릭하면, 지정된 위치로 이동하는 방식
- `href` 속성 : hypertext reference
    + 요소를 통해 연결하고자 하는 문서나 사이트 주소 등을 입력하는 속성
```html
<body>
  <h1>
    네이버 홈페이지로 이동하려면 
    <a href="https://www.naver.com/">여기</a>
    를 클릭 
  </h1>
</body>
```

### `target` : 새 탭에서 열기
- `target` 속성의 기본값 : `_self`
    + `_self` : 현재 탭에서 열기
- `_blank` : 새 탭에서 열기
```html
<body>
  <h1>두 링크의 차이를 비교해보세요</h1>
  <a href="https://www.naver.com/" target="_self">
    현재 탭에서 열기
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.naver.com/" target="_blank">
    새 탭에서 열기
  </a>
</body>
```

### `href` : 전화 걸기(`tel:`)와 메일 보내기(`mailto:`)
- `href` 속성은 URL 문서 외에 전화번호나 메일 주소를 지정할 수 있다.
- 전화번호를 지정했을 경우, 모바일에서 열고 링크를 클릭하면 해당 번호로 전화가 간다
- 이메일을 지정했을 경우, 별도의 메일 작성 프로그램이 열리게 된다.
```html
<body>
  <a href="tel:010-1234-5678">
    전화 걸기
  </a>
  <a href="mailto:eansdrawer@naver.com">
    메일 보내기
  </a>
</body>
```







