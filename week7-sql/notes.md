# Week 7 — SQL

> 📅 Date: _Not started yet_  
> 🎓 Source: [CS50 Lecture 7](https://cs50.harvard.edu/x/2024/weeks/7/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [ ] Understand relational databases and tables
- [ ] Write SQL queries: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- [ ] Use `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`
- [ ] Understand database design and normalization
- [ ] Use SQLite in Python with `cs50` library

---

## 📖 Key Concepts

> 📝 *Notes coming soon — work in progress*

### SQL CRUD Quick Reference

```sql
-- CREATE
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- READ
SELECT * FROM users WHERE name = 'Alice';

-- UPDATE
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- DELETE
DELETE FROM users WHERE id = 1;
```

---

## 💻 Code Examples

> *To be filled in during/after lecture*

---

## 🧩 Problem Set Notes

> *To be filled in*

---

## ❓ Questions & Confusions

- [ ] What is SQL injection and how to prevent it?
- [ ] When to use `JOIN` vs subqueries?

---

## 🔗 Further Reading

- [CS50 Week 7 Notes](https://cs50.harvard.edu/x/2024/notes/7/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQL Tutorial — W3Schools](https://www.w3schools.com/sql/)

---

*[← Week 6: Python](../week6-python/) · [Back to Index](../README.md) · [Next Week → Week 8: HTML/CSS/JS](../week8-html-css-js/)*
