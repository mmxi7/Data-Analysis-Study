# GROUP BY

기준 컬럼의 값이 같은 데이터끼리 **하나의 그룹으로 묶는 기능**

주로 그룹별 통계를 구하기 위해 **집계 함수**와 함께 사용

### 기본 문법

```sql
SELECT * (컬럼 AS ...)
FROM
WHERE
GROUP BY 기준1, 기준2, ...
ORDER BY
LIMIT;
```

- 기준 컬럼 값이 여러 개인 경우 첫 번째 기준으로 그룹화 후, 그 안에서 두 번째 기준으로 다시 그룹을 나눈다
- `SELECT` 절에서 지정한 별칭을 사용할 수 있다.


### GROUP BY와 집계 함수

`GROUP BY`는 그룹별 통계를 구하기 위해 `COUNT()`, `SUM()`, `AVG()` 등의 집계 함수와 함께 사용

<br>

# HAVING

그룹화된 결과에 **조건을 지정**할 때 사용

### 기본 문법

```sql
SELECT * (컬럼 AS ...)
FROM
WHERE
GROUP BY 기준1, 기준2, ...
HAVING
ORDER BY
LIMIT;
```

### WHERE와 HAVING의 차이

| 구분 | WHERE | HAVING |
| --- | --- | --- |
| 조건 적용 대상 | 그룹화 전 데이터 | 그룹화된 결과 |
| 집계 함수 조건 | 사용할 수 없음 | 사용할 수 있음 |
| GROUP BY 필요 여부 | 없어도 사용 가능 | GROUP BY와 함께 사용 |


<br>

# DISTINCT

조회 결과에서 **중복된 행을 제거**

### 기본 문법

```sql
SELECT DISTINCT ...
FROM;
```

### COUNT()와 DISTINCT

`DISTINCT`와 `COUNT()`를 함께 사용하면 중복을 제외한 값의 개수를 구할 수 있음


<details>
<summary><h2>연습문제</h2></summary>

### 01

교수의 직급(position)별 교수 수를 출력하시오.

```sql
SELECT position AS 직급, COUNT(*) AS 교수수
FROM professors
GROUP BY position;
```

### 02

학생들의 성별(gender)에 대한 평균 몸무게를 계산하시오.

```sql
SELECT gender AS 성별, AVG(weight) AS '평균 몸무게'
FROM students
GROUP BY gender;
```

### 03

학생 수가 10명 초과인 학년과 학생수를 조회하시오.

```sql
SELECT grade AS 학년, COUNT(*) AS 학생수
FROM students
GROUP BY grade
HAVING 학생수 > 10;
```

### 04

수강신청일 기준으로 연도별 신청 건수와 평균 점수를 구하시오.

```sql
SELECT
    YEAR(enroll_date) AS 수강년도,
    COUNT(*) AS 신청 건수,
    AVG(score) AS 평균 점수
FROM enrollments
GROUP BY 수강년도;
```

### 05

`students` 테이블에서 학적상태(status)별로 학생 수와 평균 키를 구하고, 평균 키가 165cm 이상인 상태만 출력하시오. 평균 키가 높은 순으로 정렬하시오.

```sql
SELECT
    status AS '학적 상태',
    COUNT(*) AS 학생수,
    AVG(height) AS 평균키
FROM students
GROUP BY status
HAVING 평균키 >= 165
ORDER BY 평균키 DESC;
```

</details>
