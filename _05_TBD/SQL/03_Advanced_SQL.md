# Advanced SQL

<details>
<summary><strong>Advanced Performance Optimization</strong></summary>

```sql
-- Query plan analysis
EXPLAIN (ANALYZE, BUFFERS, FORMAT JSON) 
SELECT e.first_name, e.last_name, d.name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE e.salary > 50000;

-- Advanced indexing strategies
-- Partial index for active records only
CREATE INDEX idx_active_employees_salary ON employees(salary) 
WHERE status = 'active';

-- Composite index with included columns
CREATE INDEX idx_employees_dept_salary_inc ON employees(department_id, salary) 
INCLUDE (first_name, last_name, hire_date);

-- Functional index
CREATE INDEX idx_employees_email_lower ON employees(LOWER(email));

-- Hash index for equality comparisons
CREATE INDEX CONCURRENTLY idx_employees_id_hash ON employees USING HASH(id);

-- Query optimization techniques
-- Use materialized CTEs for expensive operations
WITH expensive_calculation AS MATERIALIZED (
    SELECT department_id, 
           percentile_cont(0.5) WITHIN GROUP (ORDER BY salary) as median_salary
    FROM employees
    GROUP BY department_id
)
SELECT e.*, ec.median_salary
FROM employees e
JOIN expensive_calculation ec ON e.department_id = ec.department_id;

-- Efficient pagination with cursor-based approach
SELECT * FROM employees
WHERE (salary, id) > (50000, 123)  -- cursor from previous page
ORDER BY salary, id
LIMIT 20;

-- Batch processing for large updates
DO $$
DECLARE
    batch_size INTEGER := 1000;
    processed INTEGER := 0;
BEGIN
    LOOP
        UPDATE employees 
        SET updated_at = CURRENT_TIMESTAMP
        WHERE id IN (
            SELECT id FROM employees 
            WHERE updated_at IS NULL
            LIMIT batch_size
        );
        
        GET DIAGNOSTICS processed = ROW_COUNT;
        EXIT WHEN processed = 0;
        
        COMMIT;  -- Commit each batch
        RAISE NOTICE 'Processed % rows', processed;
    END LOOP;
END $$;
```

</details>

<details>
<summary><strong>Advanced Data Types & Operations</strong></summary>

```sql
-- Advanced JSON operations (PostgreSQL)
CREATE TABLE event_logs (
    id SERIAL PRIMARY KEY,
    event_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Complex JSON queries
SELECT 
    event_data->>'user_id' as user_id,
    event_data->>'event_type' as event_type,
    event_data->'metadata'->>'source' as source,
    jsonb_array_length(event_data->'tags') as tag_count
FROM event_logs
WHERE event_data->>'event_type' = 'login'
  AND event_data->'metadata'->>'source' = 'mobile'
  AND event_data->'user_data'->>'premium' = 'true';

-- JSON aggregation
SELECT event_data->>'event_type',
       jsonb_agg(event_data->'metadata') as all_metadata,
       jsonb_object_agg(
           event_data->>'user_id', 
           event_data->'user_data'
       ) as user_data_map
FROM event_logs
GROUP BY event_data->>'event_type';

-- Array operations (PostgreSQL)
CREATE TABLE survey_responses (
    user_id INTEGER,
    selected_options INTEGER[],
    tags TEXT[]
);

-- Array queries
SELECT user_id, selected_options
FROM survey_responses
WHERE 1 = ANY(selected_options)  -- Contains option 1
  AND NOT (2 = ANY(selected_options))  -- Doesn't contain option 2
  AND array_length(selected_options, 1) >= 3;  -- At least 3 selections

-- Array aggregation and manipulation
SELECT 
    array_agg(DISTINCT user_id) as all_users,
    array_agg(selected_options) as all_selections,
    unnest(array_agg(tags)) as individual_tags
FROM survey_responses;

-- Range types (PostgreSQL)
CREATE TABLE event_schedules (
    event_id INTEGER,
    time_range TSRANGE,
    price_range NUMRANGE
);

INSERT INTO event_schedules VALUES 
(1, '[2024-01-01 09:00, 2024-01-01 17:00)', '[100, 500)');

SELECT * FROM event_schedules
WHERE time_range @> '2024-01-01 14:00'::timestamp  -- Contains time
  AND price_range && '[200, 300)'::numrange;       -- Overlaps price range
```

</details>

<details>
<summary><strong>Pivot & Unpivot Operations</strong></summary>

```sql
-- Manual PIVOT using CASE statements
SELECT 
    department_id,
    SUM(CASE WHEN EXTRACT(MONTH FROM hire_date) = 1 THEN 1 ELSE 0 END) as jan_hires,
    SUM(CASE WHEN EXTRACT(MONTH FROM hire_date) = 2 THEN 1 ELSE 0 END) as feb_hires,
    SUM(CASE WHEN EXTRACT(MONTH FROM hire_date) = 3 THEN 1 ELSE 0 END) as mar_hires
FROM employees
GROUP BY department_id;

-- PostgreSQL CROSSTAB (requires tablefunc extension)
SELECT * FROM crosstab(
    'SELECT department_id, EXTRACT(MONTH FROM hire_date), COUNT(*)
     FROM employees 
     GROUP BY department_id, EXTRACT(MONTH FROM hire_date)
     ORDER BY 1,2',
    'VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10), (11), (12)'
) AS pivot_table(dept_id int, jan int, feb int, mar int, apr int, may int, jun int, 
                 jul int, aug int, sep int, oct int, nov int, dec int);

-- UNPIVOT using UNION ALL
WITH monthly_data AS (
    SELECT department_id, 10 as jan, 15 as feb, 8 as mar FROM dept_monthly_stats
)
SELECT department_id, 'Jan' as month, jan as hires FROM monthly_data
UNION ALL
SELECT department_id, 'Feb' as month, feb as hires FROM monthly_data  
UNION ALL
SELECT department_id, 'Mar' as month, mar as hires FROM monthly_data;

-- Dynamic pivot with arrays (PostgreSQL)
SELECT department_id, 
       array_agg(hire_count ORDER BY hire_month) as monthly_hires
FROM (
    SELECT department_id, 
           EXTRACT(MONTH FROM hire_date) as hire_month,
           COUNT(*) as hire_count
    FROM employees
    GROUP BY department_id, EXTRACT(MONTH FROM hire_date)
) monthly_stats
GROUP BY department_id;
```

</details>

<details>
<summary><strong>Advanced Window Functions</strong></summary>

```sql
-- Complex frame specifications
SELECT employee_id, salary, hire_date,
    -- 3-month moving average
    AVG(salary) OVER (
        ORDER BY hire_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3,
    
    -- Percentage of total within department
    salary / SUM(salary) OVER (PARTITION BY department_id) * 100 as pct_of_dept_total,
    
    -- Cumulative percentage
    SUM(salary) OVER (
        PARTITION BY department_id 
        ORDER BY salary DESC 
        ROWS UNBOUNDED PRECEDING
    ) / SUM(salary) OVER (PARTITION BY department_id) * 100 as cumulative_pct
FROM employees;

-- Advanced ranking with gaps
SELECT employee_id, department_id, salary,
    ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) as row_num,
    RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank_with_gaps,
    DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dense_rank,
    PERCENT_RANK() OVER (PARTITION BY department_id ORDER BY salary) as percent_rank,
    CUME_DIST() OVER (PARTITION BY department_id ORDER BY salary) as cumulative_dist
FROM employees;

-- Advanced LAG/LEAD with default values and offsets
SELECT employee_id, salary, hire_date,
    LAG(salary, 1, 0) OVER (ORDER BY hire_date) as prev_hire_salary,
    LEAD(salary, 2, salary) OVER (ORDER BY hire_date) as salary_two_hires_later,
    salary - LAG(salary, 1, salary) OVER (ORDER BY hire_date) as salary_diff_from_prev
FROM employees;

-- Window functions with FILTER clause (PostgreSQL)
SELECT department_id,
    COUNT(*) OVER (PARTITION BY department_id) as total_in_dept,
    COUNT(*) FILTER (WHERE salary > 60000) OVER (PARTITION BY department_id) as high_earners_in_dept,
    AVG(salary) FILTER (WHERE hire_date > '2020-01-01') OVER (PARTITION BY department_id) as recent_hire_avg_salary
FROM employees;
```

</details>

<details>
<summary><strong>Complex Recursive CTEs</strong></summary>

```sql
-- Organizational hierarchy with levels and paths
WITH RECURSIVE org_chart AS (
    -- Base case: CEO/top managers
    SELECT id, first_name, last_name, manager_id, 
           1 as level,
           ARRAY[id] as path,
           first_name || ' ' || last_name as hierarchy_path
    FROM employees 
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive case
    SELECT e.id, e.first_name, e.last_name, e.manager_id,
           oc.level + 1,
           oc.path || e.id,
           oc.hierarchy_path || ' -> ' || e.first_name || ' ' || e.last_name
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
    WHERE NOT e.id = ANY(oc.path)  -- Prevent cycles
)
SELECT * FROM org_chart ORDER BY level, hierarchy_path;

-- Bill of Materials / Parts explosion
WITH RECURSIVE parts_explosion AS (
    -- Base case: final products
    SELECT product_id, component_id, quantity, 1 as level
    FROM bill_of_materials
    WHERE product_id = 'LAPTOP_001'
    
    UNION ALL
    
    -- Recursive case: sub-components
    SELECT bom.product_id, bom.component_id, 
           pe.quantity * bom.quantity as total_quantity,
           pe.level + 1
    FROM bill_of_materials bom
    JOIN parts_explosion pe ON bom.product_id = pe.component_id
    WHERE pe.level < 10  -- Prevent infinite recursion
)
SELECT component_id, SUM(total_quantity) as total_needed
FROM parts_explosion
GROUP BY component_id;

-- Graph traversal - find all connected nodes
WITH RECURSIVE graph_traversal AS (
    SELECT node_id, connected_node_id, 1 as distance,
           ARRAY[node_id] as path
    FROM graph_edges
    WHERE node_id = 'START_NODE'
    
    UNION ALL
    
    SELECT ge.node_id, ge.connected_node_id, 
           gt.distance + 1,
           gt.path || ge.connected_node_id
    FROM graph_edges ge
    JOIN graph_traversal gt ON ge.node_id = gt.connected_node_id
    WHERE NOT ge.connected_node_id = ANY(gt.path)
      AND gt.distance < 20
)
SELECT connected_node_id, MIN(distance) as shortest_distance
FROM graph_traversal
GROUP BY connected_node_id;
```

</details>

<details>
<summary><strong>Advanced Analytics & Statistical Functions</strong></summary>

```sql
-- Statistical aggregates
SELECT department_id,
    COUNT(*) as n,
    AVG(salary) as mean_salary,
    STDDEV(salary) as std_dev,
    VARIANCE(salary) as variance,
    
    -- Percentiles
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY salary) as q1,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) as median,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY salary) as q3,
    PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY salary) as p90,
    
    -- Mode (most frequent value)
    MODE() WITHIN GROUP (ORDER BY salary) as mode_salary
FROM employees
GROUP BY department_id;

-- Linear regression analysis
SELECT department_id,
    COUNT(*) as n,
    CORR(EXTRACT(EPOCH FROM hire_date), salary) as correlation,
    REGR_SLOPE(salary, EXTRACT(EPOCH FROM hire_date)) as salary_trend_per_day,
    REGR_INTERCEPT(salary, EXTRACT(EPOCH FROM hire_date)) as intercept,
    REGR_R2(salary, EXTRACT(EPOCH FROM hire_date)) as r_squared
FROM employees
GROUP BY department_id;

-- Cohort analysis
WITH monthly_cohorts AS (
    SELECT employee_id,
           DATE_TRUNC('month', hire_date) as cohort_month,
           DATE_TRUNC('month', performance_review_date) as review_month
    FROM employees e
    JOIN performance_reviews pr ON e.id = pr.employee_id
),
cohort_sizes AS (
    SELECT cohort_month, COUNT(DISTINCT employee_id) as cohort_size
    FROM monthly_cohorts
    GROUP BY cohort_month
),
cohort_retention AS (
    SELECT mc.cohort_month,
           EXTRACT(YEAR FROM AGE(mc.review_month, mc.cohort_month)) * 12 +
           EXTRACT(MONTH FROM AGE(mc.review_month, mc.cohort_month)) as months_since_hire,
           COUNT(DISTINCT mc.employee_id) as retained_employees
    FROM monthly_cohorts mc
    GROUP BY mc.cohort_month, months_since_hire
)
SELECT cr.cohort_month,
       cr.months_since_hire,
       cr.retained_employees,
       cs.cohort_size,
       cr.retained_employees::float / cs.cohort_size as retention_rate
FROM cohort_retention cr
JOIN cohort_sizes cs ON cr.cohort_month = cs.cohort_month
ORDER BY cr.cohort_month, cr.months_since_hire;
```

</details>

<details>
<summary><strong>Database Design & Normalization</strong></summary>

```sql
-- Example of normalized database design
-- 1NF: Atomic values, no repeating groups
CREATE TABLE employees_1nf (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    skill_1 VARCHAR(50),
    skill_2 VARCHAR(50),
    skill_3 VARCHAR(50)  -- Violates 1NF - repeating groups
);

-- Better 1NF design
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE employee_skills (
    employee_id INTEGER REFERENCES employees(id),
    skill VARCHAR(50),
    PRIMARY KEY (employee_id, skill)
);

-- 2NF: Remove partial dependencies
CREATE TABLE project_assignments_2nf (
    employee_id INTEGER,
    project_id INTEGER,
    hours_worked INTEGER,
    employee_name VARCHAR(100),  -- Violates 2NF - depends only on employee_id
    project_name VARCHAR(100),   -- Violates 2NF - depends only on project_id
    PRIMARY KEY (employee_id, project_id)
);

-- Better 2NF design
CREATE TABLE project_assignments (
    employee_id INTEGER REFERENCES employees(id),
    project_id INTEGER REFERENCES projects(id),
    hours_worked INTEGER,
    PRIMARY KEY (employee_id, project_id)
);

-- 3NF: Remove transitive dependencies
CREATE TABLE employees_3nf (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    department_location VARCHAR(100)  -- Violates 3NF - depends on department
);

-- Better 3NF design
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE,
    location VARCHAR(100)
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INTEGER REFERENCES departments(id)
);

-- Denormalization for performance (when appropriate)
CREATE TABLE employee_summary (
    employee_id INTEGER PRIMARY KEY,
    full_name VARCHAR(101),  -- Denormalized: first_name + last_name
    department_name VARCHAR(50),  -- Denormalized from departments table
    current_salary DECIMAL(10,2),
    total_projects INTEGER,  -- Denormalized count
    last_promotion_date DATE,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

</details>

<details>
<summary><strong>Advanced Transactions & Concurrency</strong></summary>

```sql
-- Transaction isolation levels
-- Read phenomena: Dirty Read, Non-repeatable Read, Phantom Read

-- Serializable isolation (strongest)
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT COUNT(*) FROM inventory WHERE product_id = 'ITEM001';
-- Other operations...
COMMIT;

-- Explicit locking
BEGIN;
SELECT * FROM accounts WHERE id = 123 FOR UPDATE;  -- Row-level lock
UPDATE accounts SET balance = balance - 100 WHERE id = 123;
UPDATE accounts SET balance = balance + 100 WHERE id = 456;
COMMIT;

-- Advisory locks for application-level coordination
SELECT pg_advisory_lock(12345);  -- Acquire application lock
-- Critical section...
SELECT pg_advisory_unlock(12345);  -- Release lock

-- Deadlock detection and handling
BEGIN;
-- Transaction 1
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
-- Potential deadlock point
UPDATE accounts SET balance = balance + 50 WHERE id = 2;
COMMIT;

-- Savepoints for partial rollbacks
BEGIN;
INSERT INTO orders (customer_id, total) VALUES (123, 100.00);
SAVEPOINT before_items;

INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 'PROD1', 2);
-- Something goes wrong with this item
ROLLBACK TO before_items;

INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 'PROD2', 1);
COMMIT;

-- Connection pooling considerations
-- Use prepared statements for performance
PREPARE get_employee_by_dept AS 
SELECT * FROM employees WHERE department_id = $1;

EXECUTE get_employee_by_dept(1);
```

</details>

<details>
<summary><strong>ETL & Data Warehousing Patterns</strong></summary>

```sql
-- Slowly Changing Dimension (SCD) Type 2
CREATE TABLE dim_employee (
    surrogate_key SERIAL PRIMARY KEY,
    employee_id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    effective_date DATE,
    expiration_date DATE,
    is_current BOOLEAN DEFAULT TRUE
);

-- SCD Type 2 update process
WITH updated_employees AS (
    SELECT employee_id, first_name, last_name, department, salary,
           CURRENT_DATE as effective_date
    FROM staging_employees
),
current_records AS (
    SELECT * FROM dim_employee WHERE is_current = TRUE
)
-- Expire changed records
UPDATE dim_employee 
SET expiration_date = CURRENT_DATE - INTERVAL '1 day',
    is_current = FALSE
WHERE employee_id IN (
    SELECT ue.employee_id 
    FROM updated_employees ue
    JOIN current_records cr ON ue.employee_id = cr.employee_id
    WHERE (ue.first_name, ue.last_name, ue.department, ue.salary) != 
          (cr.first_name, cr.last_name, cr.department, cr.salary)
);

-- Insert new versions
INSERT INTO dim_employee (employee_id, first_name, last_name, department, salary, effective_date)
SELECT ue.employee_id, ue.first_name, ue.last_name, ue.department, ue.salary, ue.effective_date
FROM updated_employees ue
LEFT JOIN current_records cr ON ue.employee_id = cr.employee_id
WHERE cr.employee_id IS NULL  -- New employees
   OR (ue.first_name, ue.last_name, ue.department, ue.salary) != 
      (cr.first_name, cr.last_name, cr.department, cr.salary);  -- Changed employees

-- Fact table with time-based partitioning
CREATE TABLE fact_sales (
    sale_id BIGINT,
    customer_key INTEGER,
    product_key INTEGER,
    time_key INTEGER,
    sales_amount DECIMAL(12,2),
    quantity INTEGER,
    sale_date DATE
) PARTITION BY RANGE (sale_date);

-- Create monthly partitions
CREATE TABLE fact_sales_2024_01 PARTITION OF fact_sales
FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE fact_sales_2024_02 PARTITION OF fact_sales
FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');

-- Data quality checks
SELECT 
    'Null check' as check_type,
    COUNT(*) as violations
FROM staging_employees 
WHERE first_name IS NULL OR last_name IS NULL

UNION ALL

SELECT 
    'Duplicate check' as check_type,
    COUNT(*) - COUNT(DISTINCT employee_id) as violations
FROM staging_employees

UNION ALL

SELECT 
    'Range check' as check_type,
    COUNT(*) as violations
FROM staging_employees 
WHERE salary < 0 OR salary > 1000000;
```

</details> 