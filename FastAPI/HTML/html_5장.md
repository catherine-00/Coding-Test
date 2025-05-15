## 5.1 목록 만들기
### `<ul>`,`<ol>` : 목록의 종류
- 목록(list) : 연관 잇는 항목들을 정돈된 형태로 나열한 것
- 블록 레벨 요소이다.
- `<ul>` : 순서 없는 목록 (Unordered List)
- `<ol>` : 순서 있는 목록 (Ordered List)

### `<li>` : 항목을 나타내는 태그는 같다.
- `<ul>`과 `<ol>`로 목록을 생성하고 나면, 빈 블록이 생긴다.
- 안에 항목을 나타내기 위해서는 `<li>` 태그가 안에 추가되어야 한다.
    + `<li>` 하나 당 항목 하나
    + 블록 레벨 요소
- `<ul>` 안에 `<li>`가 있으면, 순서 표시 x
```html
<body>
  <h1>항목 태그는 같은 것을 쓴다</h1>
  <ul>
    <li>강아지</li>
    <li>고양이</li>
    <li>거북이</li>
    <li>햄스터</li>
  </ul>
</body>
```

<body>
    <h1>항목 태그는 같은 것을 쓴다</h1>
    <ul>
        <li>강아지</li>
        <li>고양이</li>
        <li>거북이</li>
        <li>햄스터</li>
    </ul>
</body>





- `<ol>` 안에 `<li>`가 있으면, 순서 표시 O
```html
<body>
  <h1>항목 태그는 같은 것을 쓴다</h1>
  <ol>
    <li>스타벅스</li>
    <li>커피빈</li>
    <li>파스쿠찌</li>
    <li>이디야</li>
  </ol>
</body>
```

<body>
    <h1>항목 태그는 같은 것을 쓴다.</h1>
    <ol>
        <li>스타벅스</li>
        <li>커피빈</li>
        <li>파스쿠찌</li>
        <li>이디야</li>
    </ol>
</body>




### `start`,`type` : 순서 있는 목록(`<ol>`)의 속성
- 기본 : 숫자 (1번부터)
- 원하는 경우 기호로 나타내거나 순서를 변경할 수 있다.
- `start` : 자연수를 지정해 몇 번부터 시작할 것인지 정함
-  `type` : 어떤 유형의 기호로 순서를 표시할 것인지 정함
    + 기호 종류 5개
        + `A`, `a`, `1`, `i`, `I` 
```html
<body>
  <h1>과목명 나열하기</h1>
  <ol start="3" type="a">
    <li>유체역학</li>
    <li>전자회로</li>
    <li>동역학</li>
    <li>마이크로프로세서</li>
  </ol>
</body>
```

<body>
    <h1>과목명 나열하기</h1>
    <ol start='3' type="a">
        <li>유체역학</li>
        <li>전자회로</li>
        <li>동역학</li>
        <li>마이크로프로세서</li>
    </ol>
</body>





# 5.2 표 만들기
### 표 만들기
- 표의 구성 : 행(row), 열(column), 셀(cell)
- 표를 나타내는 태그 안에 항목들을 채워 넣어서 완성할 수 있다.
- 표 만들 때 사용하는 태그들
    + `<table>` : 하나의 표를 나타내는 태그
    + `<tr>` : 표 안에서 하나의 행을 나타내는 태그
    + `<th>` : 행 안에서 제목에 해당하는 셀을 나타내는 태그
    + `<td>` : 행 안에서 항목에 해당하는 셀을 나태는 태그
```html
<body>
  <table border="1">
    <tr>
      <th>한국 선수</th>
      <th>일본 선수</th>
      <th>미국 선수</th>
    </tr>
    <tr>
      <td>김철수</td>
      <td>오오다</td>
      <td>제임스</td>
    </tr>
  </table>
</body>
```

<body>
    <table border="1">
        <tr>
            <th>한국선수</th>
            <th>일본선수</th>
            <th>미국선수</th>
        </tr>
        <tr>
            <td>김철수</td>
            <td>오오다</td>
            <td>제임스</td>
        </tr>
    </table>
</body>




- `border` 속성 : 테두리의 두께를 입력하는 속성
    + 따로 지정하지 않으면 테두리 없이 출력됨

### 표에 제목(자막) 추가하기
#### `<caption>` : 제목(자막)을 추가
- `<caption>` : `<table>` 태그 안에서 제목, 또는 표에 대한 설명을 나타내는 역할
    + 기본 : 가로 길이를 기준으로 가운데 정렬
```html
<body>
  <table border="1">
    <caption>
      <strong>국가대표 선수 명단</strong>
      <br>
      남자 마라톤
    </caption>
    <tr>
      <th>한국 선수</th>
      <th>일본 선수</th>
      <th>미국 선수</th>
    </tr>
    <tr>
      <td>김철수</td>
      <td>오오다</td>
      <td>제임스</td>
    </tr>
  </table>
</body>
```

<body>
  <table border="1">
    <caption>
      <strong>국가대표 선수 명단</strong>
      <br>
      남자 마라톤
    </caption>
    <tr>
      <th>한국 선수</th>
      <th>일본 선수</th>
      <th>미국 선수</th>
    </tr>
    <tr>
      <td>김철수</td>
      <td>오오다</td>
      <td>제임스</td>
    </tr>
  </table>
</body>




#### `<figure>` : 독립적인 콘텐츠를 나타내는
- 앞에서 학습한 `<figure>`와 `<figcaption>`이 함께 쓰일 수 있었다.
- 표를 나타낼 때도 함께 사용 가능
- 가운데 정렬이 되지 않음.
```html
<body>
  <figure>
    <figcaption>
      <strong>국가대표 선수 명단</strong>
    </figcaption>
    <table border="1">
      <tr>
        <th>한국 선수</th>
        <th>일본 선수</th>
        <th>미국 선수</th>
      </tr>
      <tr>
        <td>김철수</td>
        <td>오오다</td>
        <td>제임스</td>
      </tr>
    </table>
  </figure>
</body>
```

<body>
  <figure>
    <figcaption>
      <strong>국가대표 선수 명단</strong>
    </figcaption>
    <table border="1">
      <tr>
        <th>한국 선수</th>
        <th>일본 선수</th>
        <th>미국 선수</th>
      </tr>
      <tr>
        <td>김철수</td>
        <td>오오다</td>
        <td>제임스</td>
      </tr>
    </table>
  </figure>
</body>


### 표의 구조를 나타내는 태그들
- `cell`은 표시된 콘텐츠의 성격이나 표의 구조에 따라 여러 개의 셀을 묶어서 관리할 수도 있음.
    - `<thead>` : 표의 제목을 나타내는 영역
    - `<tbody>` : 표의 본문을 나타내는 영역
    - `<tfoot>` : 표의 요약 부분을 나타내는 영역
- 화면에는 위 태그들을 쓰나 안 쓰나 차이는 없음
- 개발자가 보기 좋게 하는 것
- 웹 접근성이 향상됨
    - 웹 접근성 : 장애가 있는 사람, 없는 사람 모두 웹사이트를 이용할 수 있음을 의미함. HTML 코드 구조가 명확할수록 시각장애를 가진 사람이 음성낭독기로 웹사이트를 이용할 때의 사용성이 향상됨.
```html
<body>
  <table border="1">
    <thead>
      <tr>
        <th>한국 선수</th>
        <th>일본 선수</th>
        <th>미국 선수</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>김철수</td>
        <td>오오다</td>
        <td>제임스</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>세계 랭킹 5위</td>
        <td>세계 랭킹 8위</td>
        <td>세계 랭킹 2위</td>
      </tr>
    </tfoot>
  </table>
</body>
```
<body>
  <table border="1">
    <thead>
      <tr>
        <th>한국 선수</th>
        <th>일본 선수</th>
        <th>미국 선수</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>김철수</td>
        <td>오오다</td>
        <td>제임스</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>세계 랭킹 5위</td>
        <td>세계 랭킹 8위</td>
        <td>세계 랭킹 2위</td>
      </tr>
    </tfoot>
  </table>
</body>






