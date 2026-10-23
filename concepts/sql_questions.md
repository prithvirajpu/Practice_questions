# Database Interview Notes

## 1. 🗄️ RDBMS vs NoSQL

**📖 Definition:**

- **RDBMS:** Stores data in tables with rows and columns. Examples: PostgreSQL, MySQL.
- **NoSQL:** Stores data using document, key-value, graph, or wide-column models. Examples: MongoDB, Redis.

**🎯 Why it's used:**
- RDBMS is suitable for structured data, relationships, and transactions.
- NoSQL is useful for flexible data structures and certain distributed workloads.

**🌍 Real-world use case:**

- Banking application → PostgreSQL.
- Product catalog with varying attributes → MongoDB.

**💻 Code Example:**

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary NUMERIC(10, 2)
);
```

```javascript
{
    "name": "Ravi",
    "salary": 35000,
    "skills": ["Python", "Django"]
}
```

---

## 2. ⚠️ Cons of RDBMS

**📖 Definition:**

An RDBMS organizes data into related tables and enforces schemas, constraints, and relationships.

**🎯 Disadvantages:**
- Schema changes may require migrations.
- Horizontal scaling can be complex.
- Complex joins can become expensive without proper optimization.
- Highly variable data can be less convenient to model.
- Distributed deployment may require additional configuration.

**🌍 Real-world use case:**

An application storing millions of flexible event records may find a document database more convenient for certain workloads.

**💡 Interview point:** RDBMS is not inherently slower than NoSQL. The right choice depends on data structure, consistency, query patterns, and scale.

---

## 3. ⚙️ Responsibilities of DBMS

**📖 Definition:**

A Database Management System (DBMS) is software used to create, store, retrieve, and manage data.

**🎯 Main responsibilities:**
- Data storage and retrieval.
- Security and access control.
- Data integrity and constraint enforcement.
- Concurrency control.
- Transaction management.
- Backup and recovery.
- Metadata management.

**🌍 Real-world use case:**

In banking, a DBMS helps ensure account updates are performed reliably when multiple transactions occur simultaneously.

**💻 Code Example:**

```sql
CREATE TABLE accounts (
    id INT PRIMARY KEY,
    balance NUMERIC(12, 2)
);

ALTER TABLE accounts
ADD CONSTRAINT balance_nonnegative
CHECK (balance >= 0);
```

---

## 4. 🧩 Entities

**📖 Definition:**

An entity is a real-world object or concept about which data is stored. A table commonly represents an entity type, and each row represents an instance.

**🎯 Why it's used:**
- Identifies what information must be stored.
- Helps design database tables.
- Defines relationships between data.

**🌍 Real-world use case:**

In a task management application, `User`, `Task`, and `Project` can be entities.

**💻 Code Example:**

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE tasks (
    id INT PRIMARY KEY,
    title VARCHAR(200),
    user_id INT REFERENCES users(id)
);
```

---

## 5. 🔤 CHAR vs VARCHAR

**📖 Definition:**

- **CHAR(n):** Fixed-length character type; shorter values are padded with spaces.
- **VARCHAR(n):** Variable-length character type with a maximum length of `n`.

**🎯 Why it's used:**
- `CHAR` can suit fixed-length values.
- `VARCHAR` suits text whose length varies.

**🌍 Real-world use case:**

- Country code → `CHAR(2)`.
- Employee name → `VARCHAR(100)`.

**💻 Code Example:**

```sql
CREATE TABLE employees (
    country_code CHAR(2),
    name VARCHAR(100)
);

INSERT INTO employees
VALUES ('IN', 'Ravi');
```

**💡 Interview point:** PostgreSQL `VARCHAR(n)` and `TEXT` have similar performance characteristics for many common uses. `CHAR(n)` is not automatically faster.

---

## 6. 🧮 Scalar Functions

**📖 Definition:**

Scalar functions operate on individual values and return a single value for each input row.

**🎯 Why it's used:**
- Transform text.
- Perform calculations.
- Process dates.
- Handle NULL values.

**🌍 Real-world use case:**

Convert employee names to uppercase and calculate the length of each name.

**💻 Code Example:**

```sql
SELECT
    UPPER(name) AS uppercase_name,
    LENGTH(name) AS name_length,
    ROUND(salary, 0) AS rounded_salary
FROM employees;
```

**💡 Common functions:** `UPPER()`, `LOWER()`, `LENGTH()`, `ROUND()`, `ABS()`, `COALESCE()`.

---

## 7. 🪟 Window Functions

**📖 Definition:**

A window function calculates a value across related rows while retaining individual rows in the result.

Unlike `GROUP BY`, it does not collapse all rows in a group into one row.

**🎯 Why it's used:**
- Rank employees by salary.
- Calculate running totals.
- Compare current and previous rows.
- Find top salaries within each department.

**🌍 Real-world use case:**

Rank employees within each department without hiding individual salary records.

**💻 Code Example:**

```sql
SELECT
    name,
    department_id,
    salary,
    RANK() OVER (
        PARTITION BY department_id
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;
```

**💡 Common functions:** `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`.

---

## 8. 📦 Common Table Expressions (CTE)

**📖 Definition:**

A Common Table Expression is a named temporary result set defined using `WITH` and used by the SQL statement that follows it.

**🎯 Why it's used:**
- Improves query readability.
- Breaks complex queries into logical steps.
- Supports recursive queries.

**🌍 Real-world use case:**

Find departments whose total employee salary exceeds ₹100,000.

**💻 Code Example:**

```sql
WITH department_salaries AS (
    SELECT
        department_id,
        SUM(salary) AS total_salary
    FROM employees
    GROUP BY department_id
)
SELECT *
FROM department_salaries
WHERE total_salary > 100000;
```

**💡 Interview point:** A CTE improves readability but is not automatically faster than a subquery.

---

## 9. 🗂️ Types of Indexing

**📖 Definition:**

An index is a data structure that helps a database locate matching rows more efficiently.

**🎯 Common PostgreSQL index types:**
- **B-tree:** Equality and range queries; default index type.
- **Hash:** Equality comparisons.
- **GIN:** Useful for arrays, JSONB, and full-text search.
- **GiST:** Specialized searches, including geometric and range data.
- **SP-GiST:** Certain partitioned search structures.
- **BRIN:** Large tables where values correlate with physical row order.

**🌍 Real-world use case:**

A ticket system frequently searches tickets by status and creation date.

**💻 Code Example:**

```sql
CREATE INDEX idx_tickets_status
ON tickets(status);

CREATE INDEX idx_tickets_created_at
ON tickets(created_at);

EXPLAIN
SELECT *
FROM tickets
WHERE status = 'OPEN';
```

**💡 Interview point:** Indexes can speed up reads but consume storage and add overhead to inserts, updates, and deletes.

---

## 10. 🌳 Clustered vs Non-clustered Index

**📖 Definition:**

- **Clustered index:** In systems supporting this concept, table rows are organized around the index's ordering.
- **Non-clustered index:** A separate index structure stores indexed values and references to table rows.

**🎯 Key differences:**

| Feature | Clustered | Non-clustered |
|---|---|---|
| Row organization | Related to index ordering | Separate from table row order |
| Number per table | Commonly one | Often multiple |
| Storage | Depends on implementation | Requires additional index storage |
| Range queries | Can be efficient | Can also be efficient |

**🌍 Real-world use case:**

A table frequently queried by date may benefit from physical organization that improves date-range access.

**💻 PostgreSQL Example:**

```sql
CREATE INDEX idx_employees_salary
ON employees(salary);

CLUSTER employees
USING idx_employees_salary;
```

**💡 Interview point:** PostgreSQL does not automatically maintain this physical ordering after subsequent writes. `CLUSTER` is an operation, not a permanently enforced row-order guarantee.

---

## 11. 🔑 Composite Key

**📖 Definition:**

A composite key consists of two or more columns that together uniquely identify a row.

**🎯 Why it's used:**
- When one column cannot uniquely identify a record.
- To enforce uniqueness across multiple columns.

**🌍 Real-world use case:**

A student can enroll in many courses, and each course can have many students. Together, `student_id` and `course_id` identify an enrollment.

**💻 Code Example:**

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    PRIMARY KEY (student_id, course_id)
);
```

Here, a student cannot enroll in the same course twice, but can enroll in different courses.

---

## 12. 🔗 Partial and Transitive Dependency (Normalization)

**📖 Definition:**

- **Partial dependency:** A non-key attribute depends on only part of a composite candidate key. This violates Second Normal Form (2NF).
- **Transitive dependency:** A non-key attribute depends on another non-key attribute instead of depending directly on a candidate key. This is a common 3NF violation.

**🎯 Why it's used:**
- Reduces data duplication.
- Prevents insertion, update, and deletion anomalies.
- Improves data consistency.

**🌍 Real-world use case:**

A student-course table stores student names and course names along with a composite key.

**💻 Code Example:**

```sql
CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    student_name VARCHAR(100),
    course_name VARCHAR(100),
    PRIMARY KEY (student_id, course_id)
);
```

Here:
- `student_name` depends only on `student_id`.
- `course_name` depends only on `course_id`.

Both are partial dependencies on the composite key.

**Improved design:**

```sql
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE student_courses (
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    PRIMARY KEY (student_id, course_id)
);
```

**💡 Transitive dependency example:**

If `employee_id → department_id` and `department_id → department_name`, then `employee_id → department_name` is a transitive dependency.

To remove it, store department details in a separate `departments` table and reference it from `employees`.

---

## 13. 🏛️ Three-Schema Architecture

**📖 Definition:**

The three-schema architecture separates a database into three levels to provide abstraction and data independence.

**🎯 The three levels:**

1. **External level:** What an individual user or application sees.
2. **Conceptual level:** The overall logical structure of the database.
3. **Internal level:** How data is physically stored.

**🌍 Real-world use case:**

In a college database:
- Students see their marks.
- Administrators see student and course information.
- The database manages the underlying physical storage.

**💻 Code Example:**

```sql
-- External-level representation
CREATE VIEW student_public_info AS
SELECT student_id, student_name
FROM students;

-- Conceptual-level example
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    marks NUMERIC(5, 2)
);

-- Index supporting physical data access
CREATE INDEX idx_students_name
ON students(student_name);
```

**💡 Interview point:** Views can represent external-level access. Indexes help with physical data access, but the three-schema architecture is a broader database design concept.

---

## 14. ⚠️ Cons of Database Triggers

**📖 Definition:**

A trigger is a database action that executes automatically when a specified event occurs, such as an `INSERT`, `UPDATE`, or `DELETE`.

**🎯 Disadvantages:**
- Business logic can become hidden.
- Debugging can be more complicated.
- Triggers can slow down write operations.
- Multiple triggers can interact unexpectedly.
- Recursive or cascading behavior can be difficult to manage.
- Testing and maintenance can become more complex.

**🌍 Real-world use case:**

Updating an employee record automatically triggers multiple audit and notification operations. Poorly designed triggers can make the update unexpectedly slow.

**💻 Code Example:**

```sql
CREATE FUNCTION log_salary_change()
RETURNS TRIGGER AS $$
BEGIN
    RAISE NOTICE 'Salary changed';
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER salary_change_trigger
AFTER UPDATE OF salary ON employees
FOR EACH ROW
EXECUTE FUNCTION log_salary_change();
```

**💡 Interview point:** Triggers are useful for auditing and database-level rules, but application service-layer logic is often easier to maintain.

---

## 15. 🧱 BLOB Data Type

**📖 Definition:**

BLOB stands for Binary Large Object. It refers to binary content such as images, audio, documents, and other files stored in a database.

**🎯 Why it's used:**
- Stores binary content alongside related records.
- Supports applications that need database-managed files.
- Can help maintain transactional consistency between records and content.

**🌍 Real-world use case:**

An application stores profile photos or uploaded documents.

**💻 PostgreSQL Example:**

PostgreSQL does not have a column type literally named `BLOB`. It supports `BYTEA` for binary data.

```sql
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255),
    file_data BYTEA
);
```

**💡 Interview point:** Large files are often stored in object storage such as Amazon S3 or Cloudinary, while the database stores their URLs and metadata.

---

## 16. ⚙️ Stored Procedure Use Cases

**📖 Definition:**

A stored procedure is a named routine stored in the database that executes SQL statements and procedural logic.

**🎯 Why it's used:**
- Reuses database operations.
- Groups multiple operations into a routine.
- Implements database-side business rules.
- Can reduce application-to-database round trips.
- Can help control access to sensitive operations.

**🌍 Real-world use case:**

Transferring money between two bank accounts requires deducting money from one account and adding it to another safely.

**💻 PostgreSQL Example:**

```sql
CREATE PROCEDURE transfer_money(
    sender_id INT,
    receiver_id INT,
    amount NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE accounts
    SET balance = balance - amount
    WHERE id = sender_id;

    UPDATE accounts
    SET balance = balance + amount
    WHERE id = receiver_id;
END;
$$;

CALL transfer_money(1, 2, 500);
```

**💡 Important:** This is a simplified example. Production code must validate the amount, verify both accounts, prevent insufficient balances, and handle concurrency safely.

---

## 17. 🔍 How Indexing Works

**📖 Definition:**

Indexing creates an additional data structure that helps the database find matching rows without scanning every row in all cases.

**🎯 How it works:**

Suppose a table has one million employees and you frequently search by email.

- Without an index, the database may scan many or all rows.
- With a B-tree index, it can navigate the index to locate matching entries.
- The database then retrieves the corresponding table rows when needed.

**🌍 Real-world use case:**

A login API searches for a user by email. An appropriate index can speed up this lookup as the number of users increases.

**💻 Code Example:**

```sql
CREATE INDEX idx_users_email
ON users(email);

EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email = 'ravi@example.com';
```

**💡 Important points:**
- Indexes can help with `WHERE`, `JOIN`, `ORDER BY`, and some grouping operations.
- Indexes consume storage.
- Indexes add overhead to inserts, updates, and deletes.
- The database does not always use an available index.
- A sequential scan may be faster when a query returns a large portion of the table.
- Use `EXPLAIN ANALYZE` to inspect actual query execution.

---

# 💻 Practical SQL Interview Questions

## 18. 🥈 Find the Second-Highest Distinct Salary

**📖 Question:** Find the second-highest distinct salary in the company.

**💻 Answer:**

```sql
SELECT DISTINCT salary
FROM employees
WHERE salary IS NOT NULL
ORDER BY salary DESC
OFFSET 1
LIMIT 1;
```

**🎯 Explanation:**
- `DISTINCT` removes duplicate salaries.
- `ORDER BY salary DESC` sorts salaries from highest to lowest.
- `OFFSET 1` skips the highest salary.
- `LIMIT 1` returns the next salary.

---

## 19. 🏆 Find the Top Three Salaries in Each Department

**📖 Question:** Find the top three distinct salary levels in each department, including ties.

**💻 Answer:**

```sql
SELECT *
FROM (
    SELECT
        name,
        department_id,
        salary,
        DENSE_RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary DESC
        ) AS salary_rank
    FROM employees
) ranked
WHERE salary_rank <= 3;
```

**🎯 Explanation:**
- `PARTITION BY` ranks employees separately in each department.
- `DENSE_RANK()` gives equal salaries the same rank.
- Filtering to ranks 1–3 includes all employees in the top three distinct salary levels.

---

## 20. 💰 Find Departments Whose Total Salary Exceeds ₹100,000

**📖 Question:** Return departments with a combined employee salary greater than 100,000.

**💻 Answer:**

```sql
SELECT
    department_id,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department_id
HAVING SUM(salary) > 100000;
```

**🎯 Explanation:**
- `GROUP BY` groups employees by department.
- `SUM()` calculates each department's total salary.
- `HAVING` filters groups after aggregation.

---

## 21. 📈 Find Employees Earning More Than Their Department's Average

**💻 Answer:**

```sql
SELECT name, department_id, salary
FROM (
    SELECT
        name,
        department_id,
        salary,
        AVG(salary) OVER (
            PARTITION BY department_id
        ) AS department_average
    FROM employees
) employee_stats
WHERE salary > department_average;
```

**🎯 Explanation:**

The window function calculates the average salary for each department without collapsing individual employee rows. The outer query returns employees earning more than their department average.

---

## 22. 🔎 Find Duplicate Email Addresses

**📖 Question:** Find email addresses that appear more than once in the `users` table.

**💻 Answer:**

```sql
SELECT
    email,
    COUNT(*) AS total
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**🎯 Explanation:**

`GROUP BY` groups identical email addresses, and `HAVING COUNT(*) > 1` returns only duplicates.

---

## 23. 🔄 Calculate a Running Total of Salaries

**📖 Question:** Calculate the cumulative salary total ordered by employee ID.

**💻 Answer:**

```sql
SELECT
    id,
    name,
    salary,
    SUM(salary) OVER (
        ORDER BY id
        ROWS BETWEEN UNBOUNDED PRECEDING
                 AND CURRENT ROW
    ) AS running_total
FROM employees;
```

**🎯 Explanation:**

For each row, `SUM()` adds salaries from the first row through the current row.

---

## 24. 🔗 Find Employees Without a Matching Department

**📖 Question:** Find employees whose department does not match a record in `departments`.

**💻 Answer:**

```sql
SELECT e.*
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.id
WHERE d.id IS NULL;
```

**🎯 Explanation:**

`LEFT JOIN` retains every employee. If no matching department exists, the department columns are `NULL`.

---

## 25. 🧠 Use a CTE to Find Above-Average Salaries

**💻 Answer:**

```sql
WITH company_stats AS (
    SELECT AVG(salary) AS average_salary
    FROM employees
)
SELECT e.name, e.salary
FROM employees e
CROSS JOIN company_stats c
WHERE e.salary > c.average_salary;
```

**🎯 Explanation:**

The CTE calculates the company-wide average salary. The outer query compares each employee's salary with that value.

---

## 26. ⚡ Create a Composite Index

**📖 Question:** An application frequently filters tickets by `status` and `created_at`. Create an index for this query pattern.

**💻 Answer:**

```sql
CREATE INDEX idx_tickets_status_created
ON tickets(status, created_at);
```

Example query:

```sql
SELECT *
FROM tickets
WHERE status = 'OPEN'
  AND created_at >= DATE '2026-01-01';
```

**🎯 Explanation:**

The index is ordered by `status` first and then `created_at`. It can help queries filtering by `status`, or by both columns. The ideal column order depends on the actual workload.

---

## 27. 🔐 Demonstrate a Transaction

**📖 Question:** Transfer ₹500 between two accounts.

**💻 Answer:**

```sql
BEGIN;

UPDATE accounts
SET balance = balance - 500
WHERE id = 1
  AND balance >= 500;

UPDATE accounts
SET balance = balance + 500
WHERE id = 2;

COMMIT;
```

**🎯 Explanation:**

A transaction groups database operations so they can be committed together or rolled back together.

**💡 Important:** This is a simplified example. Production code must verify that the sender has sufficient funds and that both accounts exist. If either operation fails, the transaction should be rolled back.

---

## 🎯 Final Interview Tips

Prioritize these concepts:

- `WHERE` vs `HAVING`
- `GROUP BY` vs window functions
- Primary key vs composite key
- Partial dependency vs transitive dependency
- RDBMS vs NoSQL
- Clustered vs non-clustered index
- CTE vs subquery
- Stored procedures vs triggers
- Index benefits vs index overhead
- `DELETE` vs `TRUNCATE` vs `DROP`
- Transactions and ACID properties

**Practice tip:** For each topic, explain the definition, give one real-world example, and write a small SQL query. This helps prepare for both theory questions and practical coding rounds.