# OUTER JOIN

### OUTER JOIN이란?
두 테이블을 JOIN할 때, **기준 테이블의 모든 행을 결과에 포함**

### 종류
- LEFT OUTER JOIN
- RIGHT OUTER JOIN
- FULL OUTER JOIN (성능에 불리, 거의 사용하지 않음)

### 구문
```sql
SELECT ...
FROM ...
LEFT/RIGHT JOIN ... ON ...
```

# UNION
두 개 이상의 SELECT 결과를 수직으로 합쳐 하나의 결과로 만듦  
중복된 행은 자동으로 제거됨
- 성능에 불리하므로 사용하지 않음

---

<details>
<summary><h2>연습문제</h2></summary>

### 01

`professors`와 `subjects`를 조인하여, 과목을 담당하지 않는 교수의 이름만 출력하세요.

```sql
SELECT p.name AS 교수이름
FROM professors p
LEFT OUTER JOIN subjects sb ON p.id = sb.professor_id
WHERE sb.id IS NULL;
```

### 02

`departments`와 `subjects`를 조인하여, 학과명과 과목 수를 출력하세요.  
모든 학과가 포함되어야 하며, 과목이 없는 학과도 출력되어야 합니다.

```sql
SELECT d.dname AS 학과명, COUNT(sb.id) AS 과목수
FROM departments d
LEFT OUTER JOIN subjects sb ON d.id = sb.department_id
GROUP BY d.id;
```

### 03

담당 과목이 없는 교수도 포함하여, 교수 이름과 담당 과목명을 출력하세요.  
모든 교수를 출력하되, 과목을 맡지 않은 교수의 과목명은 NULL로 표시되도록 하세요.

```sql
SELECT p.name AS 교수이름, sb.name AS 담당과목
FROM professors p
LEFT OUTER JOIN subjects sb ON p.id = sb.professor_id;
```

### 04

모든 학생의 이름과 수강신청한 과목명을 출력하세요. 단, 수강신청을 하지 않은 학생도  
모두 포함되어야 하며, 수강신청이 없는 경우 과목명은 NULL로 표시됩니다.

```sql
SELECT s.name AS 학생이름, sb.name AS 과목명
FROM students s
LEFT OUTER JOIN enrollments e ON s.id = e.student_id
LEFT OUTER JOIN subjects sb ON e.subject_id = sb.id;
```

### 05

`students`와 `enrollments`를 조인하여, 수강 신청을 한 번도 하지 않은 학생의 이름을  
출력하세요.

```sql
SELECT s.name AS 학생이름
FROM students s
LEFT OUTER JOIN enrollments e ON s.id = e.student_id
WHERE e.student_id IS NULL;
```
