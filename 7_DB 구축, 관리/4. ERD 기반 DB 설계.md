# ERD 기반 DB 설계

## 데이터베이스의 설계 단계

### 데이터 모델링 3단계

| 개념적 모델링 | 논리적 모델링 | 물리적 모델링 |
|---|---|---|
| 고객의 비즈니스 프로세스 분석<br>업무 전체에 대해 데이터 모델링 수행<br>추상화 수준이 가장 높음<br>주요 부분 위주로 모델링<br>전사적 관점에서 기업의 데이터를 모델링 (업무적 관점에서 수행)<br>기술적 용어는 지양<br>엔터티(Entity)와 속성(Attribute)을 도출<br>개념적 ERD를 작성 | 개념적 모델링을 논리적 모델링으로 변환<br>식별자를 도출하고 필요한 모든 릴레이션을 정의<br>정규화를 수행해서 데이터 모델의 독립성을 확보하고 재사용성을 높임 | 데이터베이스를 실제 구축<br>특정 데이터베이스(DBMS) 모델에 종속<br>속성 이름을 컬럼이름으로 변경하고, 데이터 타입을 명시한다.<br>각종 제약조건들을 정의<br>성능, 보안, 가용성을 고려해서 구축 |
> **데이터베이스 설계 과정 = 데이터 모델링**

데이터 모델링의 특징: **추상화, 단순화, 명확성**

<br>

## ERD의 이해

### ERD(Entity Relationship Diagram, 개체-관계 다이어그램)

데이터베이스의 구조를 시각적으로 표현한 다이어그램

- 테이블(Entity) 간의 관계, 속성, 제약조건 등을 도형으로 나타냄
- 시스템 분석·설계 단계에서 DB 구조 설계 및 이해에 필수적

### ERD 구성 요소

| 구성요소 | 설명 | 예시 |
|---|---|---|
| **Entity (개체)** | 저장할 데이터 단위(테이블) → 네모 상자로 표현 | 회원, 도서 |
| **Attribute (속성)** | 엔터티가 가지는 정보(컬럼) → 개체 안에 속성을 기입함 | 이름, 이메일 |
| **Relationship (관계)** | 엔터티 간의 연결(외래키) → 개체와 개체를 선으로 연결함 | 회원 - 대출 관계 |

### ERD를 사용하는 이유

- 현실 세계의 데이터를 논리적 구조로 체계화하여 데이터베이스의 구조를 한눈에 파악
  - 개발자, 기획자, 디자이너 간의 소통 원활
- 중복 데이터를 방지하고, 데이터 무결성을 확보
  - 프로그램의 오류를 줄이고 논리적 설계 기반을 마련

<br>

## 개념적 모델링 ERD

비즈니스 요구 사항을 통해 수집한 정보를 기반으로 만들어지는 가장 간단한 모델

- 개념적 ERD로 모델링된 엔티티 및 관계는 비즈니스 요구에 따라 정의됨
- 데이터베이스 설계에 필요한 사항을 충족시킬 필요는 없음
- **개체(엔터티, Entity)와 개체의 관계만 표현하는 단계**

<br>

## 논리적 모델링 ERD

비즈니스 요구 사항에서 수집한 정보를 통해 모델링

- 데이터베이스에서 속성(Attribute)으로 식별되는 컬럼(Column)에 대한 데이터 형식을 설정하기 때문에 개념적 모델보다 복잡한 형태를 가짐
- 컬럼에 대한 데이터 형식을 설정하는 것은 선택 사항이지만, 각 컬럼에 데이터 유형을 설정함으로써 비즈니스 분석에 도움이 됨
- 하지만 실제 데이터베이스 생성과는 아직 무관함
- 개체의 수행할 작업을 모델링하기 위해 새로운 엔티티를 추가할 수 있음

<br>

## 물리적 모델링 ERD

관계형 데이터베이스의 **실제 설계 도면**

- DBMS에서 실제 데이터의 구성을 나타내므로 실제 ERD를 설계할 때 사용하는 DBMS의 규칙과 제한을 적용해야 함
- 개체(Entity)에 대한 속성(Attribute), 즉 컬럼에 정확한 데이터 유형을 설정
- 개체 및 속성 이름을 지정함에 있어 예약어 사용을 피해야 함
- 기본키, 외래키, 제약조건에 관한 세부 내용을 모델에 추가함

> 실무에서는 개념·논리 모델링을 생략하고 바로 물리 모델링을 수행하는 경우가 많음

<br>

## DBML 소개

### DBML(Database Markup Language)

데이터베이스의 구조(Schema)를 정의하는 마크업 언어

- **ERD로 변환 가능**
- 가볍고 읽기 쉬운 문법을 제공하여 테이블과 관계를 간단한 텍스트 파일로 정의 가능
- 문서화, 협업, 형상관리(Git 연동)에 용이

### 주요 특징

| 특징 | 설명 |
|---|---|
| **경량 언어** | 간단한 문법, 마크다운처럼 직관적 |
| **가독성 우수** | 누구나 읽고 이해하기 쉬움 |
| **버전관리 가능** | Git 등 형상관리 도구와 연동 쉬움 |
| **ERD 자동화** | 도구를 통해 시각화 가능 |
| **데이터베이스 생성 가능** | SQL 코드로 변환해 실제 DB 생성 가능 |

<br>

## DBML 구문 형식

### 테이블 정의

```text
Table 테이블이름 {
    컬럼이름1 데이터타입 [제약조건 및 설명]
    컬럼이름2 데이터타입 [제약조건 및 설명]
    ...

    note: "테이블 자체에 대한 설명"
}
```

### SQL과 DBML 비교

**SQL**

```sql
CREATE TABLE members (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '회원 번호',
    name VARCHAR(50) NOT NULL COMMENT '회원 이름'
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='회원';
```

**DBML**

```text
Table members {
    id INT
    name VARCHAR(50)
    note: "회원"
}
```

<br>

## DBML 제약조건 표현

`[]` 안에 여러 제약조건을 **쉼표(,)**로 구분하여 나열한다.

| SQL 제약조건 | DBML 문법 표기 | 예시 |
|---|---|---|
| `NOT NULL` | `[not null]` | `name varchar(10) [not null]` |
| `DEFAULT` | `[default: 값]` | `status varchar(10) [default: "active"]` |
| `UNIQUE` | `[unique]` | `email varchar(150) [unique]` |
| `PRIMARY KEY` | `[pk]` | `id int [pk]` |
| `AUTO_INCREMENT` | `[increment]` | `id int [pk, increment]` |
| `COMMENT` | `[note: "설명"]` | `email varchar(150) [note: "사용자 이메일"]` |

> `DEFAULT` 값 사용 시 쌍따옴표 사용에 주의한다.


## ENUM(열거형) 형식 정의

```text
Enum 열거형이름 {
    값1 [note: "설명"]
    값2 [note: "설명"]
}
```
- 정의된 열거형은 테이블 정의에서 데이터 타입으로 사용할 수 있음

<br>

## 참조키 설정

```text
Table 테이블이름 {
    컬럼이름1 데이터타입 [제약조건, 설명, ref: > 부모테이블.기본키]
    컬럼이름2 데이터타입 [제약조건 및 설명]
    ...

    note: "테이블 자체에 대한 설명"
}
```

<br>

<details>
<summary><h2>연습문제</h2></summary>

### 01

`myschool` 데이터베이스의 ERD를 작성해 보세요.

```dbml
Enum gender {
        A [note: "남"]
        B [note: "여"]
}

Enum student_status {
        A [note: "재학"]
        B [note: "휴학"]
        C [note: "졸업"]
        D [note: "퇴학"]
        }

Table students {
    id int [pk, increment, note: "학생번호"]
    name varchar(50) [not null, note: "이름"]
    user_id varchar(50) [not null, note: "아이디"]
    grade int [not null, note: "학년"]
    idnum char(64) [not null, note: "주민등록번호(SHA2해시)"]
    birthdate datetime [not null, note: "생년월일"]
    phone varchar(13) [not null, note: "전화번호"]
    height int [not null, note: "키"]
    weight int [not null, note: "몸무게"]
    status student_status [not null, note: "학적상태(A=재학,B=휴학,C=졸업,D=퇴학)"]
    gender gender [note: "성별(A=남,B=여)"]
    email varchar(100) [note: "이메일 주소"]
    photo_url varchar(255) [note: "프로필 사진 경로"]
    admission_date date [note: "입학일"]
    graduation_date date [note: "졸업일"]
    department_id int [not null, note: "소속 학과번호", ref: > departments.id]
    professor_id int [note: "지도교수번호", ref: > professors.id]
}

Table departments {
    id int [pk, increment, not null, note: "학과번호"]
    dname VARCHAR(100) [not null, note: "학과명"]
    loc VARCHAR(100) [not null, note: "위치"]
    phone VARCHAR(15) [not null, note: "전화번호"]
    email VARCHAR(100) [not null, note: "이메일 주소"]
    established int [not null, note: "설립 연도"]
    homepage VARCHAR(255) [note: "홈페이지 주소"]
    note: "학과" 
}

Table subjects {
    id int [pk, increment, not null, note: "과목번호"]
    name VARCHAR(100) [not null, note: "과목"]
    credit int [not null, note: "학점"]
    department_id int [not null, note: "개설 학과", ref: > departments.id]
    professor_id int [note: "담당 교수", ref: > professors.id]
    note: "과목" 
}

Table enrollments {
    student_id int [pk, not null, note: "학생번호", ref: > students.id]
    subject_id int [pk, not null, note: "과목번호", ref: > subjects.id]
    enroll_date date [not null, note: "수강신청일"]
    score int [note: "성적 점수"]
    note: "수강" 
}

Enum position {
    A [note: "교수"]
    B [note: "부교수"]
    C [note: "조교수"]
    D [note: "전임강사"]
}

Enum professor_status {
    A [note: "재직"]
    B [note: "휴직"]
    C [note: "퇴직"]
}

Table professors {
    id int [pk, increment, note: "교수번호"]
    name VARCHAR(50) [not null, note: "이름"]
    user_id VARCHAR(50) [not null, note: "아이디"]
    position position [not null, note: "직급(A=교수,B=부교수,C=조교수,D=전임강사)"]
    sal int [not null, note: "급여"]
    hiredate datetime [not null, note: "입사일"]
    comm int [note: "보직수당"]
    email VARCHAR(100) [note: "이메일 주소"]
    phone VARCHAR(15) [note: "전화번호"]
    photo_url VARCHAR(255) [note: "프로필 사진 URL"]
    status professor_status [not null, note: "재직상태(A=재직,B=휴직,C=퇴직)"]
    department_id int [not null, note: "소속 학과번호", ref: > departments.id]
    note: "교수" 
}
```

</details>
