# 7.1 오디오와 비디오
## `<audio>` : 오디오
- `<audio>` 태그와 함께 사용하는 속성들
    + 주로 boolean 속성
    + `controls` : 오디오 파일의 컨트롤 패널을 표시
    + `autoplay` : 오디오를 자동으로 재생
    + `muted` : 오디오를 음소거로 처리
    + `loop` : 반복 재생 기능을 추가
```html
<body>
    <!--- 컨트롤 패널로 재생할 수 있는 오디오--->
    <audio src="./happydog.mp3" controls></audio>
    <!--자동으로 재생되고 반복 재생되는 오디오--->
    <audio src="./happydog.mp3" autoplay loop></audio>
</body>
```

<body>
    <audio src="./happydog.mp3" controls></audio>
</body>


### `<source>` : 다양한 형식의 오디오 중 선택하기
- 대부분 웹 브라우저에서 `.mp3`를 지원한다.
- 하지만 다른 형식의 오디오 형식만 지원하는 경우도 있다.
- `<source>` 태그를 함께 사용해 다양한 파일 형식을 지정할 수 있다.
```html
<body>
  <audio controls>
    <source src="happydog.ogg">
    <source src="happydog.mp3">
  </audio>
</body>
```
<body>
  <audio controls>
    <source src="happydog.ogg">
    <source src="happydog.mp3">
  </audio>
</body>

- `.oog` 형식을 지원하지 않는 브라우저에서는 해당 코드를 무시하고 아래 코드를 사용한다.


## `<video>` : 비디오
- `<audio>`에서 사용한 boolean 속성들을 써서 비디오 재상 방식을 설정할 수 있다.
```html
<body>
  <video src="my-cat.mp4" controls></video>
</body>
```

<body>
    <video src="my-cat.mp4" controls></video>
</body>

- `controls`가 없으면 비디오 재싱할 때 일시 정지하기가 불편하다. 그럴 때는 자동재생(`autoplay`)를 하거나 음소거(`muted`)를 해놓는 게 좋다.
- `<source>`를 이용해서 파일 형식 지정도 가능
```html
<body>
  <video muted autoplay>
    <source src="my-cat.mp4">
    <source src="my-cat.webm">
    <source src="my-cat.ogv">
  </video>
</body>
```
<body>
  <video muted autoplay>
    <source src="my-cat.mp4">
    <source src="my-cat.webm">
    <source src="my-cat.ogv">
  </video>
</body>

# 7.2 외부 파일 및 문서 삽입
## 외부 파일 삽입하기 `<object>`, `<embed>`
- HTML5를 지원하지 않는 브라우저에서는 오디오, 비디오를 위한 추가 플러그인을 사용하는 경우가 많다.
- 플러그인 태그는 `<object>`, `<embed>`가 있다.

### 외부 리소스를 표현하는  `<object>`
- 이미지, 중첩된 브라우저 컨텍스트, 플러그인에 의해 표시되는 콘텐츠 등 다양한 외부 리소스를 나타내는 요소를 만듦
- 함께 사용하는 속성
    + `data` : 외부 파일의 경로를 지정하는 속성
    + `type` : 포함시킨 내용의 유형을 지정
    + `name` : 다른 요소들과 구분할 수 있는 식별자 역할
- `<img>`, `<video>`, `<audio>` 등의 태그에 `src` 속성을 지정하지 않으면 태그가 제 역할을 할 수 없었던 것처럼, `<object> `태그를 사용할 때는 `data` 또는 `type`을 사용해 주어야 태그가 본연의 역할(콘텐츠 표시)을 수행
```html
<body>
  <!-- 예제 출처 : MDN -->
  <object type="application/pdf"
      data="/media/examples/In-CC0.pdf"
      width="250"
      height="200">
  </object>
</body>
```
<body>
  <!-- 예제 출처 : MDN -->
  <object type="application/pdf"
      data="/media/examples/In-CC0.pdf"
      width="250"
      height="200">
  </object>
</body>

### 외부 리소스를 표현하는 `<embed>`
- HTML5를 지원하지 않는 브라우저에서 재생할 수 없는 콘텐츠를 삽입할 때 사용
- 함께 사용하는 속성
    + `src` : 외부 파일의 경로를 지정하는 속성입니다.
    + `type` : 포함시킨 내용의 유형을 지정하는 속성입니다.
    + `width` : 요소의 너비를 지정하는 속성입니다. `<object>`에도 사용 가능.
    + `height` : 요소의 높이를 지정하는 속성입니다. `<object>`에도 사용 가능.
```html
<body>
  <!-- 예제 출처 : MDN -->
  <embed type="video/quicktime" src="movie.mov" width="640" height="480">
</body>
```
<body>
  <!-- 예제 출처 : MDN -->
  <embed type="video/quicktime" src="movie.mov" width="640" height="480">
</body>


## `<iframe>` : HTML 문서 삽입하기
- 웹 페이지 않에 공간을 마련해 그 안에 또 다른 웹 페이지 표시 가능
- `src` 속성에 삽입하고자 하는 웹 문서의 URL 입력
```html
<body>
  <!-- 예제 출처 : MDN -->
  <h3>지도 가져오기</h3>
  <iframe id="inlineFrameExample"
      title="Inline Frame Example"
      width="300"
      height="200"
      src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&layer=mapnik">
  </iframe>
  <p>잘 가져온 것 같네요 ^^</p>
</body>
```
<body>
  <!-- 예제 출처 : MDN -->
  <h3>지도 가져오기</h3>
  <iframe id="inlineFrameExample"
      title="Inline Frame Example"
      width="300"
      height="200"
      src="https://www.openstreetmap.org/export/embed.html?bbox=-0.004017949104309083%2C51.47612752641776%2C0.00030577182769775396%2C51.478569861898606&layer=mapnik">
  </iframe>
  <p>잘 가져온 것 같네요 ^^</p>
</body>
