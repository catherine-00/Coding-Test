## 6.1 입력 태그
### `<input>` : 입력 받기
- 웹 페이지 이용자로부터 입력을 받기 위해 사용하는 태그 중 가장 대표적인 태그
- **입력 필드**를 나타내는 단일 태그
```html
<body>
  <h1>입력 필드를 만든다</h1>
  <input>
  <input>
</body>
```
<body>
  <h4>입력 필드를 만든다</h4>
  <input>
  <input>
</body>




- 인라인 레발 요소
- 웹 이용자는 키보드를 이용해 입력 필드에 텍스트를 입력할 수 있다.

### `type` : `<input>`태그의 핵심 속성 
- `type` 속성을 활용하면 다양한 형태의 입력 요소를 만들 수 있음
- `type` 속성에 지정할 수 있는 속성값만 해도 약 20가지가 넘음

#### `type="text"` : 텍스트를 입력 받는 text 유형
- 한 줄짜리 일반 텍스트를 입력할 수 있는 유형
- `<input>` 태그 요소의 기본 유형
- `type` 속성 지정하지 않아도 사용 가능
```html
<body>
  <h1>type="text"</h1>
  <input type="text" placeholder="텍스트를 입력하세요" maxlength="15" size="20">
</body>
```
<body>
  <h4>type="text"</h4>
  <input type="text" placeholder="텍스트를 입력하세요" maxlength="15" size="20">
</body>







- `placeholder` 에 작성된 내용은 입력 용소에 아무 값도 입력되지 않았을 때 표시되는 '안내문' 역할
- `maxlength` 은 입력할 수 있는 최대 문자 개수를 지정
- `size`는 입력 필드의 길이를 기정하는 속성(문자 수 기준)
- `laceholder`, `maxlength`, `size` 속성은 텍스트를 입력받는 다른 유형에서도 공통적으로 사용할 수 있는 속성

#### `type="password"` : 비밀번호를 입력받는 password 유형
- 텍스트를 입력 받으나, 웹 이용자가 입력하는 내용이 화면에 표시되지 않는다.
```html
<body>
  <h1>type="text" & type="password"</h1>
  <input type="text" placeholder="아이디를 입력하세요">
  <br>
  <input type="password" placeholder="비밀번호를 입력하세요">
</body>
```
<body>
  <h4>type="text" & type="password"</h4>
  <input type="text" placeholder="아이디를 입력하세요">
  <br>
  <input type="password" placeholder="비밀번호를 입력하세요">
</body>





#### `type="number"` : 숫자를 입력받는 number 유형
- 숫자를 입력받을 때 사용
- 웹 이용자는 입력 필드에 직접 숫자를 타이핑하거나 증감 버튼을 클릭해 숫자를 선택할 수도 있음
```html
<body>
  <h1>type="number"</h1>
  사과 <input type="number" min="0" max="10" step="1">개 주세요!
</body>
```
<body>
  <h4>type="number"</h4>
  사과 <input type="number" min="0" max="10" step="1">개 주세요!
</body>



- `min`과 `max`는 수치의 최소값과 최대값을 각각 지정할 수 있는 속성
- `step`은 증감 버튼을 클릭할 때 수치가 변경되는 간격
- 이 세 가지 속성들은 수치를 입력받는 다른 유형에서도 사용할 수 있는 속성
- 수치를 입력받는 다른 유형으로는 `data`, `time`, `range` 등이 있습니다.




#### `type="color"` : 색상을 입력받는 color 유형
- 웹 이용자에게 색상표를 제공해 색상을 선택할 수 있게 해줌
```html
<body>
  <h1>type="color"</h1>
  <input type="color">
</body>
```
<body>
  <h4>type="color"</h4>
  <input type="color">
</body>




- 텍스트를 입력받지 않고, 클릭을 통해 색상을 선택하는 방식

#### `type="button"` : 클릭을 입력받는 button 유형
- 클릭할 수 있는 버튼을 만드는 유형
- 버튼 클릭 외에는 다른 특별한 기능이 있진 않다.
- 스타일, 기능을 추가하고 싶으면 CSS, 자바스크립트 같은 언어 사용해야한다.
```html
<body>
  <h1>type="button"</h1>
  <input type="button" value="PUSH">
</body>
```
<body>
  <h1>type="button"</h1>
  <input type="button" value="PUSH">
</body>



- button 유형의 `<input>` 태그에 표시할 텍스트는 `value` 속성을 통해 지정함

#### `type="radio"`, `type="checkbox"` : 선택지를 제공하는 유형
- `radio` : 여러 항목 중 하나의 항목만을 선택할 때 (라디오 버튼)
- `checkbox` : 여러 항목 중 몇 가지 동시에 선택할 때
```html
<body>
  <p>좋아하는 과목을 하나만 고르세요</p>
  <input type="radio" name="subject">국어 
  <input type="radio" name="subject">영어 
  <input type="radio" name="subject">수학 

  <p>좋아하는 음식을 모두 고르세요</p>
  <input type="checkbox" name="food">제육볶음 
  <input type="checkbox" name="food">돈까스 
  <input type="checkbox" name="food">떡볶이 
</body>
```
<body>
  <p>좋아하는 과목을 하나만 고르세요</p>
  <input type="radio" name="subject">국어 
  <input type="radio" name="subject">영어 
  <input type="radio" name="subject">수학 

  <p>좋아하는 음식을 모두 고르세요</p>
  <input type="checkbox" name="food">제육볶음 
  <input type="checkbox" name="food">돈까스 
  <input type="checkbox" name="food">떡볶이 
</body>

- `name`은 식별자 속성으로, 같은 속성끼리 하나로 묶이게 된다.



### `<label>`과 함께 사용하기
- `<label>` 태그는 입력 요소에 라벨을 붙이는 역할을 함
- 웹 이용자에게 좀 더 직관적인 입력 요소 제공 가능
- 2가지 형태로 사용 가능
    + `<label>` 태그 안에 입력 요소 포함시킴
    + 입력요소의 id 기반으로 `<label>` 태그와 입력 요소를 짝 지어줌
- 아래 예제는 두 가지 방법을 모두 사용한 경우
```html
<body>
  <h1>로그인 해주세요</h1>
  <label>
    아이디
    <input type="text">
  </label>
  <br>
  <label for="pw">비밀번호</label>
  <input id="pw" type="password">
</body>
```
<body>
  <h1>로그인 해주세요</h1>
  <label>
    아이디
    <input type="text">
  </label>
  <br>
  <label for="pw">비밀번호</label>
  <input id="pw" type="password">
</body>



## 6.2 입력 요소를 만드는 또 다른 태그들
### 드롭다운 메뉴를 만드는 `<select>`
- 웹 이용자가 여러가지 항목 중 원하는 항목을 선택할 수 있도록 '드롭다운 메뉴'를 제공하는 태그
- 드롭다운 : 요소를 클릭했을 때, 선택 가능한 항목들이 아래로 펼쳐지는 메뉴
- `<option>` 태그로 메뉴의 개별 항목을 추가할 수 있다.
```html
<body>
  <select>
    <option>커피</option>
    <option>콜라</option>
    <option>쥬스</option>
    <option>생수</option>
  </select>
</body>
```
<body>
  <select>
    <option>커피</option>
    <option>콜라</option>
    <option>쥬스</option>
    <option>생수</option>
  </select>
</body>



#### `<select>`와 `<option>`에 속성 추가하기
- `<select>`에 추가할 수 있는 속성들
    - `size` : 화면에 표시될 메뉴 항목의 개수를 지정, 드롭다운 메뉴의 형태를 변경
    - `multiple` : 여러 개의 항목을 함께 선택할 수 있도록 함
        + boolean 속성명을 입력하면 적용되고 쓰지 않으면 적용 안된다.
    ```html
    <body>
    <select size="3" multiple>
        <option>커피</option>
        <option>콜라</option>
        <option>쥬스</option>
        <option>생수</option>
        <option>녹차</option>
        <option>맥주</option>
    </select>
    </body>
    ```

     <body>
    <select size="3" multiple>
        <option>커피</option>
        <option>콜라</option>
        <option>쥬스</option>
        <option>생수</option>
        <option>녹차</option>
        <option>맥주</option>
    </select>
    </body>


- `<option>`에 추가할 수 있는 속성들
    + `selected` : 화면에 표시될 때 기본으로 선택되어 있을 항목을 지정.
        + boolean 속성임.
    + `value` : 항목을 선택했을 때 최종적으로 반영될 값을 지정
        + 최종적으로 반영됨의 의미 : 웹 이용자가 선택한 값을 웹 서버에서 처리할 때 서버가 실제로 사용할 값
```html
<body>
  <select>
    <option value="coffee">커피</option>
    <option value="coke">콜라</option>
    <option value="juice">쥬스</option>
    <option value="water" selected>생수</option>
    <option value="tea">녹차</option>
    <option value="beer">맥주</option>
  </select>
</body>
```
<body>
  <select>
    <option value="coffee">커피</option>
    <option value="coke">콜라</option>
    <option value="juice">쥬스</option>
    <option value="water" selected>생수</option>
    <option value="tea">녹차</option>
    <option value="beer">맥주</option>
  </select>
</body>



- 위 예제에서 생수를 선택하면 웹 서버로 넘어가는 값은 "생수"가 아니라 "water"



### 여러 줄의 텍스트를 입력받는 `<textarea>`
- `<input>` 요소는 텍스트를 입력받을 때 한 줄 짜리 텍스트만 입력받을 수 있다
- `<textarea>` 태그를 이용해 만든 '텍스트 영역'은 여러 줄의 텍스트를 입력받을 수 있어 편지를 쓰거나 건의 사항을 제출하는 페이지를 만들 때 활용
- 함께 쓸 수 있는 속성
    + `cols` : 텍스트 영역의 가로 너비를 지정합니다. 이때 수치는 문자의 개수를 기준으로 합니다.
    + `rows` : 텍스트 영역의 세로 너비를 지정합니다. 기준은 cols와 동일하게 문자의 개수입니다.
- 텍스트가 세로로 더 길어질 경우 텍스트 영역 내에 세로 스크롤이 생깁니다.
- `<textarea>` 태그는 `<input>` 태그와 달리 여는 태그와 닫는 태그가 함께 사용되는데, 코드 작성 시 여는 태그와 닫는 태그 사이에 텍스트를 입력하면 웹 페이지에 렌더링될 때 이미 텍스트가 입력되어 있는 상태로 렌더링됩니다.

### 진척도를 표시하는 `<progress>`
- 작업이 얼마 정도 진행되었는지를 나타낼 때 사용하는 태그
- 함께 쓸 수 있는 속성
    + `max` : 작업 완료를 위해 필요한 작업량을 지정합니다. 지정하는 경우, 반드시 0보다 크고 유효한 부동소수점 숫자여야 합니다. 기본값은 1입니다.
    + `value` : 화면에 표시할 진척도를 지정합니다. max의 값보다 작거나 같아야 합니다.
```html
<body>
  <p>작업 진행 중... 60%...</p>
  <progress value="60" max="100"></progress>
</body>
```
<body>
  <p>작업 진행 중... 60%...</p>
  <progress value="60" max="100"></progress>
</body>



### 버튼 만드는 또 다른 방법 `<button>`
- `<input>` 태그의 type을 변경해 버튼을 만들었었는데, `<input>`이 아닌 `<button>` 태그를 이용해도 같은 모습의 버튼을 만들 수 있다.
- `<input type="button">`과 `<button>`을 통해 만든 요소는 형태나 기능 면에서 차이가 없다
- `<button>` 태그의 경우에는 코드 작성 시 여는 태그와 닫는 태그 사이에 콘텐츠를 입력해 버튼에 표시될 콘텐츠를 지정할 수 있다.
```html
<body>
  <!-- value 속성에 콘텐츠를 써 줍니다. -->
  <input type="button" value="PUSH">

  <!-- 태그 사이에 콘텐츠를 써 줍니다. -->
  <button>PUSH</button>
</body>
```
<body>
  <!-- value 속성에 콘텐츠를 써 줍니다. -->
  <input type="button" value="PUSH">

  <!-- 태그 사이에 콘텐츠를 써 줍니다. -->
  <button>PUSH</button>
</body>



## 6.3 입력 폼 만들기
### `<form>` : 폼 요소
- 웹 이용자가 입력 요소에 입력한 값들을 서버로 전송해주는 역할을 하는 '폼 요소(양식)'을 만드는 태그
- `<form>` 태그에는 폼 요소가 역할을 수행하는 방식이나 처리할 작업 등을 지정하는 몇 가지 속성들을 추가할 수 있는데, 대표적인 속성들은 다음과 같습니다.
    + `action` : 폼 요소에 입력된 값들을 전달받아 처리할 서버의 프로그램을 지정합니다(URL).
    + `method` : 사용자가 입력한 내용들을 서버로 전송할 때의 방식을 지정합니다.
        + `get` : 입력 후 전송한 값이 주소창에 표시됨
        + `post`: 입력 후 전송한 값이 주소창에 표지되지 않음.
```html
<body>
  <form method="post" action="fake_server.php">
    <label for="id">아이디</label>
    <input type="text" id="id">
    <br>
    <label for="pw">비밀번호</label>
    <input type="password" id="pw">
    <br>
    <input type="button" value="로그인">
  </form>
</body>
```
<body>
  <form method="post" action="fake_server.php">
    <label for="id">아이디</label>
    <input type="text" id="id">
    <br>
    <label for="pw">비밀번호</label>
    <input type="password" id="pw">
    <br>
    <input type="button" value="로그인">
  </form>
</body>



- 폼 요소에 이용자가 정보를 입력하면, 값들이 서버로 전송

### 이름을 지어주세요
- 폼 요소 안에 포함되는 각 입력 요소에는 `name` 속성을 추가하여 각 입력 항목의 역할을 구별
```html
<body>
  <form method="post" action="fake_server.php">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="age">나이</label>
    <input type="number" id="age" name="age">
    <br>
    <label for="character">성격</label>
    <textarea id="character" name="character"></textarea>
    <br>
    <input type="button" value="전송">
  </form>
</body>
```
<body>
  <form method="post" action="fake_server.php">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="age">나이</label>
    <input type="number" id="age" name="age">
    <br>
    <label for="character">성격</label>
    <textarea id="character" name="character"></textarea>
    <br>
    <input type="button" value="전송">
  </form>
</body>


- 폼 요소에서 `name`의 역할은 무척 중요
- 각 입력 요소에 지정된 `name` 속성은 폼 안에서 입력 요소를 구분하는 역할을 함과 동시에, 서버에 전송된 입력 값의 이름으로 사용되기도

### `submit` 타입 사용하기
- 폼의 요소들을 사용자들에게 받은 후, 해당 값들을 서버로 보내는 작업을 해줘야한다.
- `<input>` 태그의`submit` 유형을 이용하면 클릭 한 번으로 작업을 손쉽게 할 수 있음
```html
<body>
  <form method="post" action="fake_server.php">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="age">나이</label>
    <input type="number" id="age" name="age">
    <br>
    <label for="character">성격</label>
    <textarea id="character" name="character"></textarea>
    <br>
    <!-- 클릭하면 입력 값들이 서버로 전송됩니다 -->
    <input type="submit" value="전송">
  </form>
</body>
```
<body>
  <form method="post" action="fake_server.php">
    <label for="name">이름</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="age">나이</label>
    <input type="number" id="age" name="age">
    <br>
    <label for="character">성격</label>
    <textarea id="character" name="character"></textarea>
    <br>
    <!-- 클릭하면 입력 값들이 서버로 전송됩니다 -->
    <input type="submit" value="전송">
  </form>
</body>


- `type="button"`과 `type="submit"`은 화면 상에서 아무런 차이가 없습니다.
