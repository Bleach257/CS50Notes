# Week 9 — Flask

> 📅 Source: [CS50 Lecture 9](https://cs50.harvard.edu/x/2026/notes/9/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Build dynamic web applications with Flask
- Handle HTTP GET and POST requests
- Use Jinja2 templates with layout inheritance
- Integrate Flask with SQL databases
- Implement sessions and login/logout
- Build a shopping cart with session storage
- Create APIs returning JSON responses

---

## 📖 Key Concepts

### Flask Setup

**requirements.txt:**
```
Flask
```

**Minimal app:**
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello, world"
```

Run with: `flask run`

### File Structure

```
/templates
    index.html
    layout.html
    greet.html
app.py
requirements.txt
```

### Routing with Parameters

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", name=name)
```

URL: `http://localhost:5000/?name=David`

### Forms (GET → POST)

**index.html:**
```html
{% extends "layout.html" %}
{% block body %}
    <form action="/greet" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Greet</button>
    </form>
{% endblock %}
```

**app.py:**
```python
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    return render_template("greet.html", name=request.form.get("name", "world"))
```

> 💡 POST data lives in `request.form`, not `request.args`

### Templates — Layout Inheritance

**layout.html:**
```html
<!DOCTYPE html>
<html lang="en">
    <head><title>hello</title></head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```

**greet.html:**
```html
{% extends "layout.html" %}
{% block body %}
    hello, {{ name }}
{% endblock %}
```

### Single Route Handling GET & POST

```python
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name", "world"))
    return render_template("index.html")
```

### Flask + SQL (Frosh IMs)

```python
from cs50 import SQL
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
db = SQL("sqlite:///froshims.db")

SPORTS = ["Basketball", "Soccer", "Ultimate Frisbee"]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name"):
        return render_template("error.html", message="Missing name")
    sports = request.form.getlist("sport")
    if not sports:
        return render_template("error.html", message="Missing sport")
    for sport in sports:
        if sport not in SPORTS:
            return render_template("error.html", message="Invalid sport")
    for sport in sports:
        db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
    return redirect("/registrants")

@app.route("/deregister", methods=["POST"])
def deregister():
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")
```

### Sessions & Login

**requirements.txt:**
```
Flask
Flask-Session
```

```python
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
```

### Shopping Cart (Session-Based)

```python
@app.route("/cart", methods=["GET", "POST"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    if request.method == "POST":
        book_id = request.form.get("id")
        if book_id:
            session["cart"].append(book_id)
        return redirect("/cart")
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
```

### APIs — AJAX Search

```javascript
let input = document.querySelector('input');
input.addEventListener('input', async function() {
    let response = await fetch('/search?q=' + input.value);
    let shows = await response.text();
    document.querySelector('ul').innerHTML = shows;
});
```

### JSON API Responses

```python
from flask import jsonify

@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        shows = []
    return jsonify(shows)
```

```javascript
let response = await fetch('/search?q=' + input.value);
let shows = await response.json();
```

### MVC Architecture

| Component | Role | Flask Equivalent |
|-----------|------|-----------------|
| **Model** | Data logic | SQLite database |
| **View** | What user sees | Jinja2 templates |
| **Controller** | Logic & routing | `app.py` |

---

## 📝 Summary

| Topic | Key Takeaway |
|-------|-------------|
| **Flask** | Python micro-framework for web apps |
| **Routes** | `@app.route` decorator maps URLs to functions |
| **GET vs POST** | GET = URL params, POST = form body |
| **Templates** | Jinja2 with `{% block %}` inheritance |
| **Flask + SQL** | `cs50.SQL` with `?` parameterized queries |
| **Sessions** | `Flask-Session` for login, shopping carts |
| **APIs** | `jsonify()` returns JSON; `fetch()` in JS |
| **MVC** | Model (DB) + View (HTML) + Controller (Python) |

---

> 📌 **Prev**: [Week 8 — HTML, CSS, JavaScript](../week8-html-css-js/notes.md)  
> 📌 **Next**: [Week 10 — The End](../week10-ethics/notes.md)
