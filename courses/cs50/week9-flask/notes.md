# Week 9 — Flask

> 📅 Date: _Not started yet_  
> 🎓 Source: [CS50 Lecture 9](https://cs50.harvard.edu/x/2024/weeks/9/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [ ] Build web applications with Flask (Python)
- [ ] Handle HTTP GET and POST requests
- [ ] Use Jinja2 templating for dynamic HTML
- [ ] Work with forms and user sessions
- [ ] Connect Flask with a SQLite database

---

## 📖 Key Concepts

> 📝 *Notes coming soon — work in progress*

### Minimal Flask App

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
```

Run with: `flask run`

### Route with Template

```python
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template("index.html", name="Alice")
```

```html
<!-- templates/index.html -->
<h1>Hello, {{ name }}!</h1>
```

---

## 💻 Code Examples

> *To be filled in during/after lecture*

---

## 🧩 Problem Set Notes

> *To be filled in — typically the Finance project (stock portfolio app)*

---

## ❓ Questions & Confusions

- [ ] What is the difference between GET and POST?
- [ ] How do sessions work in Flask?

---

## 🔗 Further Reading

- [CS50 Week 9 Notes](https://cs50.harvard.edu/x/2024/notes/9/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)

---

*[← Week 8: HTML/CSS/JS](../week8-html-css-js/) · [Back to Index](../README.md) · [Next Week → Week 10: Ethics](../week10-ethics/)*
