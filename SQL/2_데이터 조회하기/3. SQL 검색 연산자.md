# SQL 검색 연산자

| 연산자 | 의미 |
|---|---|
| `BETWEEN A AND B` | A 이상 B 이하 |
| `NOT BETWEEN A AND B` | A 이상 B 이하의 범위가 아닌 값 |
| `IN (값1, 값2, ...)` | 목록 중 하나와 일치 |
| `NOT IN (값1, 값2, ...)` | 목록에 포함되지 않음 |
| `LIKE` | 특정 문자열 패턴과 일치 |
| `NOT LIKE` | 특정 문자열 패턴과 일치하지 않음 |
| `IS NULL` | NULL인 데이터 |
| `IS NOT NULL` | NULL이 아닌 데이터 |


<details>
<summary><h2>연습문제</h2></summary>

### 01

2000년에서 2005년 사이에 설립된 학과들의 학과번호, 학과명, 설립연도를 설립연도 내림차순으로 조회하시오.

```sql
SELECT id, dname, established
FROM departments
WHERE established BETWEEN 2000 AND 2005
ORDER BY established DESC;
```

### 02

컴퓨터공학과(101) 또는 소프트웨어학과(102)에 소속된 교수들의 교수번호, 이름, 학과번호를 조회하시오.

```sql
SELECT id, name, department_id
FROM professors
WHERE department_id IN (101, 102);
```

### 03

보직수당(comm)을 받지 않는 교수들의 교수번호, 이름, 급여, 보직수당을 조회하시오.

```sql
SELECT id, name, sal, comm
FROM professors
WHERE comm IS NULL;
```

### 04

학생들 중에서 키가 170cm에서 180cm 사이인 학생들의 이름, 키, 학년을 키의 오름차순으로 조회하시오.

```sql
SELECT name, height, grade
FROM students
WHERE height BETWEEN 170 AND 180
ORDER BY height ASC;
```

### 05

'김'씨 성을 가진 학생들 중 이메일 주소가 없는 학생의 이름, 학년, 이메일을 조회하시오.

```sql
SELECT name, grade, email
FROM students
WHERE name LIKE '김%' AND email IS NULL;
```

</details>
