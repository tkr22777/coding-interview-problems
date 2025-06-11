# Beginner SQL

<details>
<summary><strong>Basic SELECT & Filtering</strong></summary>

```sql
-- Select all columns
SELECT * FROM employees;

-- Select specific columns
SELECT first_name, last_name, salary FROM employees;

-- WHERE clause with conditions
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'Engineering';
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 80000;
SELECT * FROM employees WHERE first_name IN ('John', 'Jane', 'Bob');
SELECT * FROM employees WHERE first_name LIKE 'J%';        -- Starts with J
SELECT * FROM employees WHERE email LIKE '%@gmail.com';    -- Ends with @gmail.com
SELECT * FROM employees WHERE phone IS NOT NULL;

-- Multiple conditions
SELECT * FROM employees WHERE salary > 50000 AND department = 'Engineering';
SELECT * FROM employees WHERE department = 'Sales' OR department = 'Marketing';
SELECT * FROM employees WHERE NOT (salary < 40000);
```

</details>

<details>
<summary><strong>Sorting & Limiting</strong></summary>

```sql
-- ORDER BY (ascending by default)
SELECT * FROM employees ORDER BY salary;
SELECT * FROM employees ORDER BY salary ASC;
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple column sorting
SELECT * FROM employees ORDER BY department, salary DESC;
SELECT * FROM employees ORDER BY hire_date DESC, last_name ASC;

-- LIMIT results
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;     -- Top 10 highest paid
SELECT * FROM employees ORDER BY hire_date LIMIT 5;        -- 5 earliest hires

-- OFFSET (skip rows)
SELECT * FROM employees ORDER BY salary DESC LIMIT 10 OFFSET 10;  -- Rows 11-20
```

</details>

<details>
<summary><strong>Aggregate Functions</strong></summary>

```sql
-- Basic aggregates
SELECT COUNT(*) FROM employees;                             -- Total count
SELECT COUNT(DISTINCT department) FROM employees;           -- Unique departments
SELECT AVG(salary) FROM employees;                          -- Average salary
SELECT MIN(salary), MAX(salary) FROM employees;            -- Min and max salary
SELECT SUM(salary) FROM employees;                          -- Total payroll

-- Aggregates with conditions
SELECT COUNT(*) FROM employees WHERE department = 'Engineering';
SELECT AVG(salary) FROM employees WHERE hire_date > '2020-01-01';
SELECT MAX(salary) FROM employees WHERE department = 'Sales';

-- NULL handling
SELECT COUNT(phone) FROM employees;                         -- Excludes NULLs
SELECT COUNT(*) - COUNT(phone) AS missing_phones FROM employees;
```

</details>

<details>
<summary><strong>GROUP BY & HAVING</strong></summary>

```sql
-- Basic grouping
SELECT department, COUNT(*) FROM employees GROUP BY department;
SELECT department, AVG(salary) FROM employees GROUP BY department;
SELECT department, MIN(salary), MAX(salary) FROM employees GROUP BY department;

-- Multiple column grouping
SELECT department, EXTRACT(YEAR FROM hire_date) as hire_year, COUNT(*)
FROM employees 
GROUP BY department, EXTRACT(YEAR FROM hire_date);

-- HAVING (filter groups)
SELECT department, COUNT(*) FROM employees 
GROUP BY department 
HAVING COUNT(*) > 5;                                        -- Departments with >5 employees

SELECT department, AVG(salary) FROM employees 
GROUP BY department 
HAVING AVG(salary) > 60000;                                 -- High-paying departments

-- ORDER BY with GROUP BY
SELECT department, COUNT(*) as emp_count FROM employees 
GROUP BY department 
ORDER BY emp_count DESC;
```

</details>

<details>
<summary><strong>Basic Joins</strong></summary>

```sql
-- Sample tables for examples
-- employees: id, first_name, last_name, department_id, salary
-- departments: id, name, location

-- INNER JOIN (most common)
SELECT e.first_name, e.last_name, d.name as department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- LEFT JOIN (include all from left table)
SELECT e.first_name, e.last_name, d.name as department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;         -- Shows employees even without dept

-- RIGHT JOIN (include all from right table)
SELECT e.first_name, e.last_name, d.name as department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;        -- Shows all departments

-- Join with WHERE conditions
SELECT e.first_name, e.last_name, d.name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > 50000 AND d.location = 'New York';

-- Join with aggregates
SELECT d.name, COUNT(e.id) as employee_count, AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name;
```

</details>

<details>
<summary><strong>String Functions</strong></summary>

```sql
-- String manipulation
SELECT UPPER(first_name), LOWER(last_name) FROM employees;
SELECT CONCAT(first_name, ' ', last_name) as full_name FROM employees;
SELECT LENGTH(first_name) FROM employees;
SELECT SUBSTRING(email, 1, POSITION('@' IN email) - 1) as username FROM employees;

-- String search and replace
SELECT * FROM employees WHERE UPPER(first_name) = 'JOHN';
SELECT REPLACE(phone, '-', '.') as formatted_phone FROM employees;
SELECT TRIM(first_name) FROM employees;                     -- Remove whitespace

-- Pattern matching
SELECT * FROM employees WHERE first_name LIKE 'A%';         -- Starts with A
SELECT * FROM employees WHERE last_name LIKE '%son';        -- Ends with son
SELECT * FROM employees WHERE email LIKE '%_gmail.com';     -- _ matches single char
```

</details>

<details>
<summary><strong>Date Functions</strong></summary>

```sql
-- Current date/time
SELECT CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP;
SELECT NOW();                                               -- PostgreSQL/MySQL

-- Date arithmetic
SELECT hire_date, CURRENT_DATE - hire_date as days_employed FROM employees;
SELECT * FROM employees WHERE hire_date > CURRENT_DATE - INTERVAL '30 days';

-- Extract date parts
SELECT EXTRACT(YEAR FROM hire_date) as hire_year FROM employees;
SELECT EXTRACT(MONTH FROM hire_date) as hire_month FROM employees;
SELECT DATE_PART('dow', hire_date) as day_of_week FROM employees;  -- PostgreSQL

-- Date formatting
SELECT TO_CHAR(hire_date, 'YYYY-MM-DD') FROM employees;     -- PostgreSQL
SELECT DATE_FORMAT(hire_date, '%Y-%m-%d') FROM employees;   -- MySQL
```

</details>

<details>
<summary><strong>Basic Data Modification</strong></summary>

```sql
-- INSERT single row
INSERT INTO employees (first_name, last_name, email, department_id, salary)
VALUES ('John', 'Doe', 'john.doe@company.com', 1, 55000);

-- INSERT multiple rows
INSERT INTO employees (first_name, last_name, department_id, salary)
VALUES 
    ('Jane', 'Smith', 2, 60000),
    ('Bob', 'Johnson', 1, 52000),
    ('Alice', 'Brown', 3, 58000);

-- UPDATE records
UPDATE employees SET salary = 57000 WHERE id = 1;
UPDATE employees SET salary = salary * 1.1 WHERE department_id = 1;  -- 10% raise
UPDATE employees SET email = LOWER(email);                           -- Normalize emails

-- DELETE records
DELETE FROM employees WHERE id = 1;
DELETE FROM employees WHERE salary < 30000;
DELETE FROM employees WHERE hire_date < '2018-01-01';

-- TRUNCATE (faster than DELETE for all rows)
TRUNCATE TABLE temp_employees;
```

</details> 