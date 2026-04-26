# Week 7 — SQL

> 📅 Source: [CS50 Lecture 7](https://cs50.harvard.edu/x/2026/notes/7/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Read/write CSV files with Python's `csv` module
- Understand relational databases vs flat files
- Master SQL CRUD operations: CREATE, READ (SELECT), UPDATE, DELETE
- Use JOINs to combine tables
- Create indexes for query optimization
- Connect Python to SQL databases
- Understand race conditions and SQL injection attacks

---

## 📖 Key Concepts

### Flat File Databases

CSV files are **flat**: all data in a single table.

```python
import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["language"])
```

**Counting with dictionaries:**
```python
counts = {}
for row in reader:
    favorite = row["language"]
    if favorite in counts:
        counts[favorite] += 1
    else:
        counts[favorite] = 1

for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
```

### Relational Databases

- Data stored in **tables** (rows and columns)
- CRUD operations: **Create, Read, Update, Delete**
- SQLite: lightweight SQL database

```bash
sqlite3 favorites.db
.mode csv
.import favorites.csv favorites
.schema
```

### SQL Keywords

**Core commands:**

| Category | Commands |
|----------|----------|
| Read | `SELECT` |
| Create | `INSERT INTO` |
| Update | `UPDATE` |
| Delete | `DELETE` |

**Aggregate functions:** `AVG`, `COUNT`, `DISTINCT`, `LOWER`, `MAX`, `MIN`, `UPPER`

**Filtering/clauses:** `WHERE`, `LIKE`, `ORDER BY`, `LIMIT`, `GROUP BY`

### SELECT Examples

```sql
-- All rows
SELECT * FROM favorites;

-- Count specific
SELECT COUNT(*) FROM favorites WHERE language = 'C';

-- Group and count
SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC LIMIT 1;

-- Pattern matching
SELECT COUNT(*) FROM favorites WHERE problem LIKE 'Hello, %';

-- OR conditions (note single quotes escaping)
SELECT COUNT(*) FROM favorites
WHERE language = 'C' AND (problem = 'Hello, World' OR problem = 'Hello, It''s Me');
```

### INSERT / DELETE / UPDATE

```sql
INSERT INTO favorites (language, problem) VALUES ('SQL', 'Fiftyville');

DELETE FROM favorites WHERE Timestamp IS NULL;

UPDATE favorites SET language = 'SQL', problem = 'Fiftyville';
```

> ⚠️ UPDATE without WHERE modifies ALL rows!

### IMDb — Primary & Foreign Keys

- **Primary key**: Unique identifier for a row (e.g., `id`)
- **Foreign key**: References a primary key in another table (e.g., `show_id`)

**SQLite data types:** `BLOB`, `INTEGER`, `NUMERIC`, `REAL`, `TEXT`

**Constraints:** `NOT NULL`, `UNIQUE`

### JOINs

```sql
-- Explicit JOIN
SELECT title FROM shows
JOIN ratings ON shows.id = ratings.show_id
WHERE rating >= 6.0 LIMIT 10;

-- Multi-table JOIN
SELECT title FROM shows
JOIN stars ON shows.id = stars.show_id
JOIN people ON stars.person_id = people.id
WHERE name = 'Steve Carell';
```

### Indexes

```sql
.timer on
-- Check query time before index

CREATE INDEX title_index ON shows (title);
CREATE INDEX name_index ON people (name);

-- Check query time after index — should be much faster!
```

Trade-off: Speed vs storage space.

### Python + SQL

```python
from cs50 import SQL

db = SQL("sqlite:///favorites.db")
favorite = input("Favorite: ")

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)
print(rows[0]["n"])
```

> ⚠️ Use `?` placeholders to prevent SQL injection!

### Race Conditions

When multiple users modify the same database simultaneously:
- `BEGIN TRANSACTION`
- `COMMIT`
- `ROLLBACK`

### SQL Injection

```python
# ❌ VULNERABLE — string concatenation
db.execute(f"SELECT * FROM users WHERE username = '{username}'")

# ✅ SAFE — parameterized query
db.execute("SELECT * FROM users WHERE username = ?", username)
```

> Never trust user input!

---

## 📝 Summary

| Topic | Key Takeaway |
|-------|-------------|
| **CSV** | `csv.DictReader` for named column access |
| **SQL CRUD** | SELECT, INSERT, UPDATE, DELETE |
| **JOINs** | Combine tables on shared keys |
| **Indexes** | B-tree optimization — faster reads, more storage |
| **Python + SQL** | `cs50.SQL` with `?` placeholders |
| **SQL Injection** | Always use parameterized queries |
| **Race Conditions** | Use transactions (BEGIN/COMMIT/ROLLBACK) |

---

> 📌 **Prev**: [Week 6 — Python](../week6-python/notes.md)  
> 📌 **Next**: [Week 8 — HTML, CSS, JavaScript](../week8-html-css-js/notes.md)
