# 웹 프로그래밍
- 보통 사이트나 게시판 만들기를 떠올림
- 그 외에도 게임이나 인공지능 분야에도 적용 가능하다.
- 공부해두면 도움이 될 것



# 점프 투 FastAPI 머릿말
- 업무에서 사용하는 프로그램과 서비스의 연관성
- 이 부분에 대한 책임



# 이 책을 읽기 전에

## 사전지식
- 파이썬 기초지식 : <점프투파이썬> 책 정도의 내용
- HTML 기초 지식 : `<table>, <div>, <form>`태그가 무엇인지 알고 있다면 OK
- CSS 기초 지식 - 스타일시트 파일을 작성해본적이 있다면 ok
- 자바스크립트 기초 지식 - 자바스크립트를 작성해본 경험
- 폼(form)에 대한 지식 - 브라우저가 서버에 요청을 보낼 때 사용하는 GET, POST 방식의 차이점
- (권장) 데이터베이스에 대한 기초 지식 - 테이블이 무엇인지, SQL 쿼리가 무엇을 의미하는지
  
 ## 버전
 - FastAPI 0.85.1
 - Pyton 3.10
 - Svelte 3.49.0
 - 부트스트랩 5.1.3
 
 
## 챕터 별 소스
[소스 자료](https://github.com/pahkey/fastapi-book)

소스 찾는 방법은 [여기](https://wikidocs.net/177373)를 참고하자.



---

# chatGPT와 사전지식 공부하기
(안해도 될 것 같은 건 pass함.)

## 1. 파이썬 기초 지식

### 01. 변수와 자료형 (`int`, `str`, `list`, `dict`)
(pass)


### 02. 조건문, 반복문(`if`,` for`, `while`)
(pass)


### 03. 함수 정의 (`def`, `return`)
(pass)


### 04. 클래스 및 객체 지향 기본

#### 1) 클래스(class)란?
- 객체를 만들기 위한 설계도
- 객체 : 클래스(설계도)를 통해 만들어진 인스턴스(실제 데이터)이다.
- 예제

```python
# 클래스 정의: 책을 표현하기 위한 설계도
class Book:
    # 생성자 함수 (__init__) : 객체가 생성될 때 자동으로 호출됨
    def __init__(self, title, author):
        self.title = title      # self.title은 인스턴스 변수 (객체마다 다름)
        self.author = author    # self.author도 마찬가지

    # info 메서드: 책 정보를 출력하는 기능
    def info(self):
        print(f"제목: {self.title}, 저자: {self.author}")  # f-string으로 문자열 내 변수 사용
        

# 객체 생성: Book이라는 설계도를 기반으로 실체(인스턴스)를 만든다
my_book = Book("점프 투 파이썬", "박응용")

# 메서드 호출: 객체가 가진 기능을 실행
my_book.info()
```

#### (1) 클래스 변수(Class Variable)
- 모든 인스턴스(객체)가 공유하는 변수
- 클래스명, 변수명으로 접근함
```python
class Dog:
    species = "개"  # 클래스 변수: 모든 개는 '개'다

    def __init__(self, name):
        self.name = name  # 인스턴스 변수: 개별 이름

dog1 = Dog("초코")
dog2 = Dog("해피")

print(dog1.species)  # 개
print(dog2.species)  # 개

# 클래스 변수를 바꾸면 전체 객체에 영향
Dog.species = "강아지"
print(dog1.species)  # 강아지
print(dog2.species)  # 강아지
```

#### (2) 클래스 메서드 (@classmethod)
- 클래스 자체를 첫 번째 인자로 받음
- `cls`는 클래스를 의미. 클래스 변수에 접근할 때 유용
- 어떤 조건이 발생했을 때 전체의 변수를 재정의해야할 때.
```python
class Counter:
    count = 0  # 클래스 변수

    def __init__(self):
        Counter.count += 1  # 객체가 생성될 때마다 카운트 증가

    @classmethod
    def show_count(cls):
        print(f"총 생성된 객체 수: {cls.count}")  # cls로 클래스 변수 접근

# 객체 여러 개 생성
c1 = Counter()
c2 = Counter()
c3 = Counter()

# 클래스 메서드 호출
Counter.show_count()  # 출력: 총 생성된 객체 수: 3

```

#### (4) 정적 메서드(@staticmethod)
- 클래스나 인스턴스 정보에 접근하지 않는 독립적인 함수
- `self`나 `cls`인자를 사용 x
```python
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# 객체 없이도 호출 가능
print(Calculator.add(3, 5))      # 8
print(Calculator.multiply(4, 6)) # 24

```

- 문제 풀어보기
    + 문제 설명 : 어떤 대학에서는 학생 정보를 관리하는 프로그램을 만들고자 합니다. 이를 위해   `Student`클래스를 다음 조건에 맞게 구현하시오.

    + 조건
        - 클래스 변수
            - school_name: 모든 학생이 다니는 학교 이름 (초기값 "코딩대학교")
        - 생성자
            - `__init__(self, name: str, major: str)`
            - 각 학생은 이름(name)과 전공(major) 정보를 가짐
        - 클래스 메서드
            - `change_school(cls, new_name: str)`→ 학교 이름을 새로운 이름으로 변경
        - 정적 메서드
            - `is_valid_major(major: str) -> bool` → 전공명이 2글자 이상이면 True, 아니면 False를 반환
        - 인스턴스 메서드
            - `introduce(self)`→ 다음과 같이 출력
            - `안녕하세요. 저는 코딩대학교의 컴퓨터공학과 학생 홍길동입니다.`

```python
class Student: #모든 학생이 다니는 학교 이름
    school_name = "코딩대학교"

    def __init__(self, name:str, major:str):
        self.name = name
        self.major = major

    
    
    @classmethod
    def change_school(cls, new_name:str):
        cls.school_name = new_name

    @staticmethod
    def is_valid_major(major:str) -> bool :
        if len(major) >= 2 :
            print("True")
        else:
            print("False")

    def introduce(self):
        print(f"안녕하세요, 저는 {Student.school_name}의 {self.major} 학생 {self.name}입니다.")


# 객체 생성
s1 = Student("홍길동", "컴퓨터공학과")
s2 = Student("김민지", "AI")

# 클래스 메서드 사용
Student.change_school("파이썬대학교")

# 정적 메서드 사용
print(Student.is_valid_major("수학"))  # True
print(Student.is_valid_major("수"))    # False

# 소개 출력
s1.introduce()
s2.introduce()

```




### 05. `import`와 모듈 사용
- 모듈 : `.py`확장자를 가진 파이썬 파일
- 모듈 안에는 변수, 함수, 클래스 등 정의 가능
- 다른 파일에서 `import`로 불러와서 사용 가능

#### 예시
- project 폴더에 main.py, student.py라는 파일이 있다고 하자.
- 파일 예시 구조
```plaintext
project/
├── main.py         ← 메인 실행 파일
└── student.py      ← 모듈 파일 (학생 클래스 정의)

```

- 각 `.py`내용을 다음과 같다.

- `student.py` 내용(모듈)
```python
# student.py

class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"{self.name}님 안녕하세요!")

```

- `main.py` 내용 (사용자)
```python
# main.py에서 student.py 파일의 Student함수를 사용하고 싶을 때

# student 모듈에서 Student 클래스 import
from student import Student

# 객체 생성 및 사용
s = Student("홍길동")
s.hello()  # 출력: 홍길동님 안녕하세요!

```

#### `import`문법 종류
| 문법                      | 설명                     |
| ----------------------- | ---------------------- |
| `import 모듈명`            | 모듈 전체 가져오기             |
| `import 모듈명 as 별칭`      | 모듈에 별칭 부여              |
| `from 모듈 import 함수/클래스` | 모듈 내 특정 항목만 가져오기       |
| `from 모듈 import *`      | 모듈 내 모든 항목 가져오기 (`비추`) |

```python
# math 모듈 전체를 가져오기
import math
print(math.sqrt(9))  # 3.0

# 특정 함수만 가져오기
from math import sqrt
print(sqrt(16))      # 4.0

# 별칭 사용
import math as m
print(m.pow(2, 3))   # 8.0

```

#### 모듈과 패키지
- 모듈은 `.py`파일 하나
- 패키지는 폴더 + `__init__.py`파일
- 예 : `import numpy` : numpy는 수많은 모듈이 모인 패키지.


#### 문제
`greeting.py` 라는 파일을 생성하여 다음 함수를 정의하세요.
```python
def say_hello(name):
    print(f"{name}님 안녕하세요!")

def say_goodbye(name):
    print(f"{name}님 안녕히 가세요.")

```

`main.py`에서 `from greeting import say_hello`를 사용하여 `say_hello("홍길동")`을 실행하세요. `say_goodbye`는 사용하지 마세요.

#### 답
```python
# main.py

from greeting import say_hello

say_hello("홍길동")

```









### 06.예외 처리 (`try`, `except`)
#### 예외 처리란?
- 프로그램 실행 중 **오류(Exception)**가 발생하면 강제 종료됩니다.

- 이를 방지하고 오류를 우아하게 처리하는 게 `try`, `except`입니다.

#### 기본 문법
```python
try:
    # 예외가 발생할 수 있는 코드
except 예외타입:
    # 예외 발생 시 실행할 코드
```

- 예시
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
```

#### 전체 구조
```python
try:
    # 예외가 발생할 수 있는 코드
except 예외타입1:
    # 예외 1 처리
except 예외타입2:
    # 예외 2 처리
else:
    # 예외가 발생하지 않았을 때 실행
finally:
    # 예외 발생 여부와 상관없이 항상 실행
```

- 예시
```python
try:
    num = int(input("숫자를 입력하세요: "))
except ValueError:
    print("정수만 입력 가능합니다.")
else:
    print(f"입력한 숫자는 {num}입니다.")
finally:
    print("프로그램 종료.")
```

- 예외 객체 사용
```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"에러 메시지: {e}")
    # 출력 : 에러 메시지: division by zero
```

#### 예외 종류
| 예외 이름                 | 언제 발생하는가?           | 예시                      |
| --------------------- | ------------------- | ----------------------- |
| `SyntaxError`         | 문법이 잘못됐을 때          | `if True print("Hi")`   |
| `NameError`           | 정의되지 않은 변수 사용       | `print(x)` (x 정의 안 됨)   |
| `TypeError`           | 자료형이 맞지 않을 때        | `"1" + 2`               |
| `ValueError`          | 자료형은 맞지만 값이 안 맞을 때  | `int("abc")`            |
| `ZeroDivisionError`   | 0으로 나눴을 때           | `10 / 0`                |
| `IndexError`          | 리스트 인덱스 초과          | `[1, 2][5]`             |
| `KeyError`            | 딕셔너리에 없는 키 접근       | `my_dict["없는키"]`        |
| `AttributeError`      | 객체에 없는 속성이나 메서드 사용  | `5.append()`            |
| `ImportError`         | 모듈을 불러올 수 없을 때      | `import 없음`             |
| `ModuleNotFoundError` | 존재하지 않는 모듈 import   | `import not_a_module`   |
| `FileNotFoundError`   | 파일이 존재하지 않을 때 열기 시도 | `open("없음.txt")`        |
| `IndentationError`    | 들여쓰기 오류             | `if True:\nprint("hi")` |
| `RuntimeError`        | 실행 중 알 수 없는 에러      | 반복 재귀 초과 등              |
| `RecursionError`      | 재귀가 너무 깊을 때         | 무한 재귀 함수                |



### 07. `@decorator` 문법 (FastAPI에서 자주 사용)
#### 데코레이터란?
- 데코레이터는 **함수(또는 클래스)**에 기능을 덧붙이는 문법
    + `@` 기호를 이용해서 사용
    + 함수나 클래스 정의 바로 위에 붙여서, 기존 코드를 수정하지 않고 기능을 확장할 수 있습니다.

#### 기본 문법 구조
```python
def decorator_func(func):
    def wrapper():
        print("시작합니다.")
        func() # 여기에 호출 함수가 들어감
        print("끝났습니다.")
    return wrapper

@decorator_func  # <- 이게 데코레이터
def say_hello():
    print("안녕하세요!")

say_hello()
```

```plaintext
시작합니다.
안녕하세요!
끝났습니다.
```

- 매개 변수가 있는 함수에 적용하기
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):  # 어떤 인자든 받아서
        print(f"[로그] 함수 {func.__name__} 호출됨")
        return func(*args, **kwargs)  # 원래 함수 실행
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(3, 5))
```

```csharp
[로그] 함수 add 호출됨
8
```

### 08. 타입 힌트: `def add(x: int, y: int) -> int`




---




## 2. HTML 기초 지식
FastAPI에서는 프론트엔드를 만들거나 `form` 데이터를 처리할 때 HTML을 알아야 합니다.

### 01. `<form>`: 사용자 입력을 서버에 전송
### 02. `<input>`, `<button>`: 폼 요소
### 03. `<table>`: 테이블 구조 표시
### 04. `<div>`: 블록 단위로 나눔


## 3. CSS 기초 지식
FastAPI로 만든 웹 페이지에 디자인을 입히려면 CSS가 필요합니다.
### 01. 선택자(`.class`, `#id`, `tag`)
### 02. 속성: `color`, `margin`, `padding`, `font-size`
### 03. 외부 스타일시트 연결 방법: `<link rel="stylesheet" href="style.css" />`


## 4. 자바스크립트 기초지식
자바스크립트는 FastAPI에서 프론트엔드와 상호작용할 때 주로 사용됩니다.
### 01. 변수, 함수 선언
### 02. 이벤트 처리 (`onclick`, `onchange`)
### 03. DOM 조작: `document.getElementById()`
### 04. fetch API를 통한 데이터 요청



## 5. 폼(form)과 HTTP 요청 방식
FastAPI에서는 클라이언트가 서버에 정보를 전송할 때 GET/POST 요청을 사용합니다.
### 01. GET: URL을 통해 데이터 전달 (쿼리 스트링)
### 02. POST: 요청 본문을 통해 데이터 전달
### 03. `action`과 `method` 속성 이해


## 6. 데이터베이스 기초 (권장)
FastAPI는 SQLAlchemy 또는 ORM을 이용해 DB와 연결됩니다.
### 01. 테이블, 행(row), 열(column)
### 02. 기본 SQL 문법: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
### 03. 기본키(primary key), 외래키(foreign key)
