# SQL Interview Preparation

Comprehensive SQL documentation organized by complexity levels for technical interviews.

## Files Overview

### Core SQL Knowledge

#### [01_Beginner_SQL.md](01_Beginner_SQL.md)
Essential SQL concepts for entry-level positions:
- **Basic SELECT & Filtering**: WHERE, LIKE, IN, BETWEEN
- **Sorting, Limiting, and Pagination**: ORDER BY, LIMIT, OFFSET, cursor-based pagination
- **Aggregate Functions**: COUNT, SUM, AVG, MIN, MAX
- **GROUP BY & HAVING**: Grouping data and filtering groups
- **Basic Joins**: INNER, LEFT, RIGHT joins
- **String Functions**: UPPER, LOWER, CONCAT, SUBSTRING
- **Date Functions**: Date arithmetic, extraction, formatting
- **Data Modification**: INSERT, UPDATE, DELETE

#### [02_Intermediate_SQL.md](02_Intermediate_SQL.md)
Advanced concepts for senior positions:
- **Subqueries**: Scalar, correlated, EXISTS, derived tables
- **Window Functions**: ROW_NUMBER, RANK, LAG/LEAD, running totals
- **CTEs**: Common Table Expressions, recursive queries
- **Advanced Joins**: FULL OUTER, self-joins, LATERAL
- **CASE Statements**: Conditional logic, COALESCE, NULLIF
- **Set Operations**: UNION, INTERSECT, EXCEPT
- **Performance**: Indexing, query optimization, EXPLAIN
- **Data Types**: Constraints, JSON, arrays (PostgreSQL)

#### [03_Advanced_SQL.md](03_Advanced_SQL.md)
Expert-level concepts for architect/data engineer roles:
- **Pivot & Unpivot**: Data transformation, CROSSTAB, dynamic pivoting
- **Advanced Analytics**: Statistical functions, regression, cohort analysis
- **Complex Recursive CTEs**: Hierarchies, graph traversal, bill of materials
- **Performance Optimization**: Advanced indexing, materialized CTEs, batch processing
- **Database Design**: Normalization forms, denormalization strategies
- **Advanced Data Types**: JSON operations, arrays, range types
- **Transactions & Concurrency**: Isolation levels, locking, deadlock handling
- **ETL & Data Warehousing**: SCD patterns, partitioning, data quality

## Usage Guidelines

- **Interview Focus**: All examples use realistic employee/department schemas
- **Database Compatibility**: Primarily PostgreSQL syntax with MySQL notes where different
- **Best Practices**: Emphasizes efficient queries and proper indexing
- **Progressive Learning**: Start with beginner concepts before advancing

## Common Interview Topics

<details>
<summary><strong>Most Frequently Asked</strong></summary>

1. **Joins** - Understanding different join types and when to use them
2. **Subqueries vs CTEs** - When to use each approach
3. **Window Functions** - Ranking, running totals, lag/lead operations
4. **GROUP BY vs Window Functions** - Choosing the right approach
5. **Performance Optimization** - Index usage, query plan analysis
6. **Data Manipulation** - INSERT, UPDATE, DELETE operations
7. **Aggregate Functions** - COUNT, SUM, AVG with GROUP BY
8. **String Operations** - Pattern matching, text manipulation

</details>

## Quick Reference

### Essential Functions
```sql
-- Aggregates: COUNT(*), SUM(), AVG(), MIN(), MAX()
-- Window: ROW_NUMBER(), RANK(), LAG(), LEAD()
-- String: UPPER(), LOWER(), CONCAT(), SUBSTRING()
-- Date: CURRENT_DATE, EXTRACT(), DATE_PART()
-- Conditional: CASE WHEN, COALESCE(), NULLIF()
```

### Join Types
```sql
INNER JOIN    -- Only matching records
LEFT JOIN     -- All from left table
RIGHT JOIN    -- All from right table  
FULL OUTER    -- All records from both tables
CROSS JOIN    -- Cartesian product
```

### Performance Tips
- Use indexes on WHERE, JOIN, and ORDER BY columns
- Prefer EXISTS over IN for subqueries
- Use LIMIT when possible
- Avoid functions on columns in WHERE clauses

## To Consider for Addition

*Scalability and design concepts commonly tested in senior-level interviews*

### 🚨 Priority 1: Critical for Scale
- [ ] **Database Sharding & Partitioning Strategies**
  - Horizontal vs vertical partitioning, sharding keys, cross-shard joins
- [ ] **Read Replicas & Master-Slave Architecture** 
  - Read/write splitting, replication lag, failover strategies
- [ ] **Connection Pooling & Resource Management**
  - Pool sizing, connection limits, lifecycle management
- [ ] **Caching Strategies**
  - Query result caching, cache invalidation patterns

### 🔧 Priority 2: Performance & Operations  
- [ ] **Materialized Views for Performance**
  - Usage patterns, refresh strategies, maintenance overhead
- [ ] **Database Monitoring & Observability**
  - Query metrics, slow query identification, health monitoring
- [ ] **Security at Scale**
  - SQL injection prevention, row-level security, encryption
- [ ] **Schema Evolution & Migrations**
  - Zero-downtime migrations, backward compatibility

### 📊 Priority 3: Architecture Patterns
- [ ] **Multi-tenancy Patterns**
  - Single vs multi-tenant databases, tenant isolation
- [ ] **ACID vs BASE Trade-offs**
  - Consistency vs availability, CAP theorem implications  
- [ ] **Event Sourcing & CQRS Patterns**
  - Command/Query separation, event store design
- [ ] **Data Archiving & Lifecycle Management**
  - Hot vs cold data, retention policies

### 🔄 Priority 4: Real-time & Analytics
- [ ] **Real-time vs Batch Processing**
  - Stream processing, Lambda architecture, real-time aggregation
- [ ] **Cross-Database Compatibility**
  - SQL dialect differences, migration strategies
- [ ] **Backup & Disaster Recovery**
  - Point-in-time recovery, cross-region backups, RTO/RPO