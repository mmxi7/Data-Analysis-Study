# JOIN

### JOIN이란?

RDBMS에서 두 개 이상의 테이블을 연결하여 관련 데이터를 하나의 결과 집합으로 조회
테이블 간의 **공통된 컬럼**을 기준으로 데이터를 연결  
중복된 데이터를 줄이고 데이터 무결성 유지, 다양한 정보 연결 가능

### JOIN문 종류

- INNER JOIN
- LEFT [OUTER] JOIN
- RIGHT [OUTER] JOIN
- EQUI JOIN
- CROSS JOIN
- SELF JOIN

# INNER JOIN

### INNER JOIN이란?

양쪽 테이블 모두에 존재하는 값만 결과로 출력 (교집합)  
**참조키의 값이 일치하는 경우**를 조건으로 설정해야 함

### 구문
```sql
SELECT ...
FROM ...
INNER JOIN ... ON ...
```
<details>
<summary><h2>연습문제</h2></summary>

### 01

학생 이름과 지도 교수 이름을 함께 출력하시오.

```sql
SELECT s.name AS 학생이름, p.name AS 지도교수
FROM students s
INNER JOIN professors p ON s.professor_id = p.id;
```

### 02

수강신청한 학생의 이름과 수강한 과목명을 출력하시오.

```sql
SELECT s.name AS 학생이름, sb.name AS 과목명
FROM enrollments e
INNER JOIN students s ON e.student_id = s.id
INNER JOIN subjects sb ON e.subject_id = sb.id;
```

### 03

학생이 수강한 과목과 그 과목의 학과명을 출력하시오.

```sql
SELECT s.name AS 학생이름, sb.name AS 과목명, d.dname AS 개설학과
FROM enrollments e
INNER JOIN students s e ON e.student_id = s.id
INNER JOIN subjects sb ON e.subject_id = sb.id
INNER JOIN departments d ON sb.department_id = d.id;
```

### 04

2024년 이후 입사한 교수의 이름과 소속 학과명을 출력하시오.

```sql
SELECT p.name AS 교수이름, d.dname AS 학과명
FROM professors p
INNER JOIN departments d ON p.department_id = d.id
WHERE p.hiredate >= '2024-01-01';
```

### 05

4과목 이상 수강신청한 학생에 대해서 학생별로 학생의 이름과 수강신청한 과목 수, 평균 점수를 평균점수가 높은 순으로 조회하시오.

```sql
SELECT s.name AS 학생이름, COUNT(sb.name) AS 수강과목수, AVG(score) AS 평균점수
FROM enrollments e
INNER JOIN students s ON e.student_id = s.id
GROUP BY s.id
HAVING COUNT(e.subject_id) >= 4
ORDER BY 평균점수 DESC;
```

</details>
