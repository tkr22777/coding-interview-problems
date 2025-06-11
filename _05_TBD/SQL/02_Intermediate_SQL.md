# Intermediate SQL

<details>
<summary><strong>Subqueries</strong></summary>

```sql
-- Scalar subquery (returns single value)
SELECT * FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees);

-- IN subquery
SELECT * FROM employees 
WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York');

-- EXISTS subquery (more efficient than IN for large datasets)
SELECT * FROM employees e
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.id = e.department_id AND d.location = 'New York');

-- NOT EXISTS
SELECT * FROM departments d
WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.department_id = d.id);  -- Departments with no employees

-- Correlated subquery
SELECT e1.first_name, e1.last_name, e1.salary
FROM employees e1
WHERE e1.salary > (SELECT AVG(e2.salary) FROM employees e2 WHERE e2.department_id = e1.department_id);

-- Subquery in SELECT
SELECT first_name, last_name, salary,
       (SELECT AVG(salary) FROM employees) as company_avg_salary
FROM employees;

-- Subquery in FROM (derived table)
SELECT dept_stats.department_name, dept_stats.avg_salary
FROM (
    SELECT d.name as department_name, AVG(e.salary) as avg_salary
    FROM employees e
    JOIN departments d ON e.department_id = d.id
    GROUP BY d.name
) dept_stats
WHERE dept_stats.avg_salary > 60000;
```

</details>

<details>
<summary><strong>Window Functions</strong></summary>

```sql
-- ROW_NUMBER() - assigns unique numbers
SELECT first_name, last_name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) as salary_rank
FROM employees;

-- RANK() and DENSE_RANK() - handles ties differently
SELECT first_name, last_name, salary,
       RANK() OVER (ORDER BY salary DESC) as rank,
       DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;

-- Partition by department
SELECT first_name, last_name, department_id, salary,
       ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as dept_rank
FROM employees;

-- LAG() and LEAD() - access previous/next rows
SELECT first_name, last_name, salary,
       LAG(salary) OVER (ORDER BY hire_date) as prev_hire_salary,
       LEAD(salary) OVER (ORDER BY hire_date) as next_hire_salary
FROM employees;

-- Running totals with SUM()
SELECT first_name, last_name, salary,
       SUM(salary) OVER (ORDER BY hire_date ROWS UNBOUNDED PRECEDING) as running_total
FROM employees;

-- Moving averages
SELECT first_name, last_name, salary,
       AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as moving_avg_3
FROM employees;

-- FIRST_VALUE() and LAST_VALUE()
SELECT first_name, last_name, salary,
       FIRST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) as highest_in_dept,
       LAST_VALUE(salary) OVER (PARTITION BY department_id ORDER BY salary DESC 
                               ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as lowest_in_dept
FROM employees;

-- NTILE() - divide into buckets
SELECT first_name, last_name, salary,
       NTILE(4) OVER (ORDER BY salary) as salary_quartile
FROM employees;
```

</details>

<details>
<summary><strong>Common Table Expressions (CTEs)</strong></summary>

```sql
-- Basic CTE
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 70000
)
SELECT he.first_name, he.last_name, d.name as department
FROM high_earners he
JOIN departments d ON he.department_id = d.id;

-- Multiple CTEs
WITH dept_stats AS (
    SELECT department_id, AVG(salary) as avg_salary, COUNT(*) as emp_count
    FROM employees
    GROUP BY department_id
),
high_paying_depts AS (
    SELECT * FROM dept_stats WHERE avg_salary > 60000
)
SELECT d.name, hpd.avg_salary, hpd.emp_count
FROM high_paying_depts hpd
JOIN departments d ON hpd.department_id = d.id;

-- Recursive CTE (organizational hierarchy)
WITH RECURSIVE employee_hierarchy AS (
    -- Base case: top-level managers
    SELECT id, first_name, last_name, manager_id, 1 as level
    FROM employees 
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case: employees with managers
    SELECT e.id, e.first_name, e.last_name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy ORDER BY level, last_name;

-- CTE with window functions
WITH ranked_employees AS (
    SELECT first_name, last_name, department_id, salary,
           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dept_rank
    FROM employees
)
SELECT * FROM ranked_employees WHERE dept_rank <= 3;  -- Top 3 in each department
```

</details>

<details>
<summary><strong>Advanced Joins</strong></summary>

```sql
-- FULL OUTER JOIN
SELECT e.first_name, e.last_name, d.name as department
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;

-- Self JOIN (employees and their managers)
SELECT e.first_name as employee, m.first_name as manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Multiple table joins
SELECT e.first_name, e.last_name, d.name as department, p.project_name
FROM employees e
JOIN departments d ON e.department_id = d.id
JOIN employee_projects ep ON e.id = ep.employee_id
JOIN projects p ON ep.project_id = p.id;

-- JOIN with aggregates and conditions
SELECT d.name, COUNT(e.id) as employee_count, AVG(e.salary) as avg_salary
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.name
HAVING AVG(e.salary) > 50000 OR COUNT(e.id) = 0;

-- Cross JOIN (Cartesian product)
SELECT e1.first_name as emp1, e2.first_name as emp2
FROM employees e1
CROSS JOIN employees e2
WHERE e1.id < e2.id;  -- Avoid duplicate pairs

-- LATERAL JOIN (PostgreSQL specific)
SELECT e.first_name, e.last_name, recent_projects.project_name
FROM employees e
LEFT JOIN LATERAL (
    SELECT p.project_name
    FROM employee_projects ep
    JOIN projects p ON ep.project_id = p.id
    WHERE ep.employee_id = e.id
    ORDER BY ep.start_date DESC
    LIMIT 3
) recent_projects ON true;
```

</details>

<details>
<summary><strong>CASE Statements & Conditional Logic</strong></summary>

```sql
-- Simple CASE
SELECT first_name, last_name, salary,
       CASE 
           WHEN salary < 40000 THEN 'Low'
           WHEN salary < 70000 THEN 'Medium'
           ELSE 'High'
       END as salary_category
FROM employees;

-- CASE with multiple conditions
SELECT first_name, last_name, department_id, salary,
       CASE 
           WHEN department_id = 1 AND salary > 80000 THEN 'Senior Engineer'
           WHEN department_id = 1 AND salary > 60000 THEN 'Engineer'
           WHEN department_id = 1 THEN 'Junior Engineer'
           WHEN department_id = 2 AND salary > 70000 THEN 'Senior Sales'
           WHEN department_id = 2 THEN 'Sales Rep'
           ELSE 'Other'
       END as job_level
FROM employees;

-- CASE in aggregations
SELECT department_id,
       COUNT(*) as total_employees,
       COUNT(CASE WHEN salary > 60000 THEN 1 END) as high_earners,
       COUNT(CASE WHEN hire_date > '2020-01-01' THEN 1 END) as recent_hires
FROM employees
GROUP BY department_id;

-- COALESCE (handle NULLs)
SELECT first_name, last_name, 
       COALESCE(phone, email, 'No contact info') as contact
FROM employees;

-- NULLIF
SELECT first_name, last_name,
       NULLIF(salary, 0) as salary  -- Convert 0 to NULL
FROM employees;
```

</details>

<details>
<summary><strong>UNION & Set Operations</strong></summary>

```sql
-- UNION (removes duplicates)
SELECT 'Current' as status, first_name, last_name FROM employees
UNION
SELECT 'Former' as status, first_name, last_name FROM former_employees;

-- UNION ALL (keeps duplicates - faster)
SELECT department_id FROM employees
UNION ALL
SELECT id FROM departments;

-- INTERSECT (common records)
SELECT first_name, last_name FROM employees
INTERSECT
SELECT first_name, last_name FROM managers;

-- EXCEPT (records in first query but not second)
SELECT first_name, last_name FROM employees
EXCEPT
SELECT first_name, last_name FROM managers;

-- Complex UNION with ORDER BY
(SELECT 'High earner' as category, first_name, last_name, salary 
 FROM employees WHERE salary > 80000)
UNION ALL
(SELECT 'Recent hire' as category, first_name, last_name, salary 
 FROM employees WHERE hire_date > '2023-01-01')
ORDER BY salary DESC;
```

</details>

<details>
<summary><strong>Performance & Indexing Concepts</strong></summary>

```sql
-- EXPLAIN query execution plan
EXPLAIN SELECT * FROM employees WHERE salary > 50000;
EXPLAIN ANALYZE SELECT * FROM employees e JOIN departments d ON e.department_id = d.id;

-- Index creation
CREATE INDEX idx_employees_salary ON employees(salary);
CREATE INDEX idx_employees_dept_salary ON employees(department_id, salary);
CREATE UNIQUE INDEX idx_employees_email ON employees(email);

-- Partial index
CREATE INDEX idx_employees_high_salary ON employees(salary) WHERE salary > 100000;

-- Index usage patterns
-- Good: Uses index
SELECT * FROM employees WHERE salary = 50000;
SELECT * FROM employees WHERE salary > 50000;

-- Bad: Doesn't use index
SELECT * FROM employees WHERE salary + 1000 = 51000;  -- Function on column
SELECT * FROM employees WHERE UPPER(first_name) = 'JOHN';  -- Function on column

-- Query optimization tips
-- Use LIMIT when possible
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;

-- Use EXISTS instead of IN for subqueries
SELECT * FROM employees e 
WHERE EXISTS (SELECT 1 FROM departments d WHERE d.id = e.department_id AND d.active = true);

-- Avoid SELECT * in subqueries
SELECT * FROM employees e 
WHERE e.department_id IN (SELECT d.id FROM departments d WHERE d.active = true);
```

</details>

<details>
<summary><strong>Data Types & Constraints</strong></summary>

```sql
-- Table creation with constraints
CREATE TABLE employees_new (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    salary DECIMAL(10,2) CHECK (salary > 0),
    hire_date DATE DEFAULT CURRENT_DATE,
    department_id INTEGER REFERENCES departments(id),
    manager_id INTEGER REFERENCES employees_new(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Alter table operations
ALTER TABLE employees ADD COLUMN phone VARCHAR(20);
ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary >= 0);
ALTER TABLE employees DROP CONSTRAINT chk_salary;
ALTER TABLE employees ALTER COLUMN salary SET NOT NULL;

-- JSON data type (PostgreSQL)
CREATE TABLE user_preferences (
    user_id INTEGER,
    preferences JSONB
);

INSERT INTO user_preferences VALUES 
(1, '{"theme": "dark", "language": "en", "notifications": true}');

SELECT user_id, preferences->>'theme' as theme 
FROM user_preferences 
WHERE preferences->>'language' = 'en';

-- JSONB Advanced Operations & Indexing
-- JSONB operators: -> returns JSON, ->> returns text
SELECT user_id, 
       preferences->'settings' as settings_json,        -- Returns JSONB
       preferences->>'theme' as theme_text              -- Returns TEXT
FROM user_preferences;

-- Nested JSON access
CREATE TABLE user_profiles (
    user_id INTEGER,
    profile JSONB
);

INSERT INTO user_profiles VALUES 
(1, '{"personal": {"name": "John", "age": 30}, "work": {"company": "Tech Corp", "salary": 75000}}'),
(2, '{"personal": {"name": "Jane", "age": 28}, "preferences": {"theme": "light", "notifications": {"email": true, "sms": false}}}');

-- Deep nested access
SELECT user_id,
       profile->'personal'->>'name' as name,
       profile->'work'->>'company' as company,
       profile->'preferences'->'notifications'->>'email' as email_notifications
FROM user_profiles;

-- JSONB indexing for performance
-- 1. GIN index for general JSONB queries (most common)
CREATE INDEX idx_user_preferences_gin ON user_preferences USING GIN (preferences);

-- 2. Functional index for specific JSON paths
CREATE INDEX idx_user_theme ON user_preferences ((preferences->>'theme'));
CREATE INDEX idx_user_language ON user_preferences ((preferences->>'language'));

-- 3. GIN index with specific operators
CREATE INDEX idx_user_profiles_path ON user_profiles USING GIN (profile jsonb_path_ops);

-- Efficient JSONB queries
-- These queries will use the GIN index:
SELECT * FROM user_preferences WHERE preferences ? 'theme';                    -- Key exists
SELECT * FROM user_preferences WHERE preferences ?& ARRAY['theme', 'language']; -- All keys exist
SELECT * FROM user_preferences WHERE preferences ?| ARRAY['theme', 'color'];    -- Any key exists
SELECT * FROM user_preferences WHERE preferences @> '{"theme": "dark"}';        -- Contains JSON
SELECT * FROM user_preferences WHERE preferences <@ '{"theme": "dark", "language": "en", "extra": "value"}'; -- Contained by

-- These queries will use functional indexes:
SELECT * FROM user_preferences WHERE preferences->>'theme' = 'dark';
SELECT * FROM user_preferences WHERE preferences->>'language' = 'en';

-- JSONB aggregation and manipulation
-- Merge JSONB objects
UPDATE user_preferences 
SET preferences = preferences || '{"new_setting": "value"}'::jsonb 
WHERE user_id = 1;

-- Remove keys
UPDATE user_preferences 
SET preferences = preferences - 'old_setting' 
WHERE user_id = 1;

-- JSONB aggregation functions
SELECT jsonb_agg(preferences) as all_preferences
FROM user_preferences;

SELECT jsonb_object_agg(user_id::text, preferences->>'theme') as user_themes
FROM user_preferences;

-- Complex JSONB queries
-- Find users with specific nested values
SELECT user_id FROM user_profiles 
WHERE profile @> '{"personal": {"age": 30}}';

-- Find users with salary in range (type casting)
SELECT user_id, (profile->'work'->>'salary')::integer as salary
FROM user_profiles 
WHERE (profile->'work'->>'salary')::integer BETWEEN 50000 AND 100000;

-- JSONB array operations
CREATE TABLE user_tags (
    user_id INTEGER,
    tags JSONB  -- Array of tags
);

INSERT INTO user_tags VALUES 
(1, '["developer", "python", "sql"]'),
(2, '["designer", "ui", "ux", "figma"]');

-- Query JSONB arrays
SELECT * FROM user_tags WHERE tags ? 'python';                    -- Contains element
SELECT * FROM user_tags WHERE tags @> '["python"]';               -- Contains array element
SELECT user_id, jsonb_array_length(tags) as tag_count FROM user_tags;

-- *** PERFORMANCE TIPS FOR JSONB ***
-- 1. Use GIN indexes for complex queries involving @>, ?, ?&, ?|
-- 2. Use functional indexes for frequent equality checks on specific paths
-- 3. Avoid deep nesting - consider flattening frequently queried data
-- 4. Use JSONB over JSON for better performance (binary format)
-- 5. Consider partial indexes for common query patterns:
--    CREATE INDEX idx_active_users ON user_preferences USING GIN (preferences) WHERE preferences->>'status' = 'active';

-- Array data type (PostgreSQL)
CREATE TABLE employee_skills (
    employee_id INTEGER,
    skills TEXT[]
);

INSERT INTO employee_skills VALUES (1, ARRAY['Python', 'SQL', 'Git']);
SELECT * FROM employee_skills WHERE 'Python' = ANY(skills);
```

</details> 