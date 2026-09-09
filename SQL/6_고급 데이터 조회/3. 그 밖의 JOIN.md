# 그 밖의 JOIN

## EQUI JOIN
기본적으로 **INNER JOIN**과 동일한 형태

```sql
SELECT
FROM 테이블1, 테이블2, ...
WHERE JOIN조건 AND 검색조건
```

<br>

## CROSS JOIN (카티션 곱)
EQUI JOIN에서 JOIN조건이 제외된 경우
- 성능에 불리하므로 사용 권장하지 않음

<br>

## SELF JOIN (재귀)
예)
- 황진우 학생과 같은 학년의 학생 이름, 학년, 성별을 조회하시오.

```sql
SELECT s2.name AS 학생이름, s2.grade AS 학년, s2.gender AS 성별
FROM students s1
JOIN students s2 ON s1.grade = s2.grade
WHERE s1.name = '황진우' AND s2.name != '황진우';
```

- **사용 이유**

|목적|설명|
|---|---|
|계층 구조 표현|상위-하위 구조, 직원-상사, 제품 카테고리 관계 등|
|같은 집단 내 비교|같은 학년, 팀, 부서 등 내부 조건 비교|
|중복 이름, 값 찾기|동일한 값 가진 다른 행 찾기|

<details>
<summary><h2>연습문제</h2></summary>

### 01

EQUI JOIN을 사용하여 학생 이름과 지도 교수 이름을 함께 조회하시오.

```sql

```

### 02

EQUI JOIN을 사용하여 수강신청한 학생의 이름과 수강한 과목명을 출력하시오.

```sql

```

### 03

EQUI JOIN을 사용하여 학생이 수강한 과목과 그 과목의 학과명을 출력하시오.

```sql

```

### 04

EQUI JOIN을 사용하여 2024년 이후 입사한 교수의 이름과 소속 학과명을 출력하시오.

```sql

```

### 05

같은 학년에 재학 중인 학생 쌍을 모두 조회하시오. 단, 학생 번호가 작은 사람을 먼저 표시하고, 자기 자신과의 비교는 제외하세요.  
→ 출력: 학생1_이름, 학생2_이름, 학년

```sql

```

</details>
