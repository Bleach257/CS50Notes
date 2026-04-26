# Week 8 — HTML, CSS, JavaScript

> 📅 Source: [CS50 Lecture 8](https://cs50.harvard.edu/x/2026/notes/8/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Understand the Internet: TCP/IP, DNS, DHCP, HTTP/HTTPS
- Build web pages with HTML (structure)
- Style pages with CSS (presentation)
- Add interactivity with JavaScript (behavior)
- Use Bootstrap framework for rapid development

---

## 📖 Key Concepts

### The Internet

- **Routers** direct data between two points
- **TCP/IP**: Protocols for transmitting data
- **IP Address**: Identifies computers on the internet (`#.#.#.#`)
- **DNS**: Maps domain names (harvard.edu) to IP addresses
- **DHCP**: Assigns IP addresses to devices
- **Ports**: HTTP=80, HTTPS=443

### HTTP/HTTPS

| Code | Meaning |
|------|---------|
| 200 | OK |
| 301 | Moved Permanently |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

**Methods:** GET (retrieve), POST (send)

```bash
curl -I https://www.harvard.edu/
```

### HTML — Structure

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>hello, title</title>
    </head>
    <body>
        hello, body
    </body>
</html>
```

**Common elements:**

```html
<!-- Headings -->
<h1>One</h1> <h2>Two</h2> <h3>Three</h3>

<!-- Paragraph -->
<p>Lorem ipsum dolor sit amet...</p>

<!-- Lists -->
<ul><li>foo</li><li>bar</li></ul>
<ol><li>first</li><li>second</li></ol>

<!-- Table -->
<table>
    <tr><td>1</td><td>2</td><td>3</td></tr>
</table>

<!-- Image -->
<img alt="bridge" src="bridge.png">

<!-- Video -->
<video controls muted>
    <source src="video.mp4" type="video/mp4">
</video>

<!-- Link -->
<a href="https://harvard.edu">Harvard</a>

<!-- Form -->
<form action="/search" method="get">
    <input name="q" type="search" placeholder="Query">
    <button>Search</button>
</form>
```

### Regular Expressions

```html
<input name="email" type="email" pattern=".+@.+\.edu" placeholder="Email">
```

### CSS — Presentation

**Inline:**
```html
<p style="font-size: large; text-align: center;">Text</p>
```

**Internal (in `<style>`):**
```html
<style>
    .centered { text-align: center; }
    .large { font-size: large; }
</style>
```

**External (`style.css`):**
```html
<link href="style.css" rel="stylesheet">
```

**Semantic tags:**
```html
<header class="large">Title</header>
<main class="medium">Content</main>
<footer class="small">Copyright</footer>
```

### Bootstrap Framework

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
```

```html
<table class="table table-striped table-hover">
    <thead><tr><th>Name</th><th>Number</th></tr></thead>
    <tbody><tr><td>Kelly</td><td>+1-617-495-1000</td></tr></tbody>
</table>
```

### JavaScript — Behavior

**Alert on form submit:**
```html
<script>
    function greet() {
        alert('hello, ' + document.querySelector('#name').value);
    }
</script>
<form onsubmit="greet(); return false;">
    <input id="name" placeholder="Name" type="text">
    <input type="submit">
</form>
```

**Event listener (modern approach):**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    let input = document.querySelector('input');
    input.addEventListener('keyup', function(event) {
        let name = document.querySelector('p');
        if (input.value) {
            name.innerHTML = `hello, ${input.value}`;
        } else {
            name.innerHTML = 'hello, whoever you are';
        }
    });
});
```

**Change style:**
```javascript
let body = document.querySelector('body');
document.querySelector('#red').addEventListener('click', function() {
    body.style.backgroundColor = 'red';
});
```

**Timers:**
```javascript
setInterval(blink, 500);          // Every 500ms
setTimeout(function() { ... }, 3000);  // After 3 seconds
```

**Autocomplete:**
```javascript
let input = document.querySelector('input');
input.addEventListener('keyup', function() {
    let html = '';
    if (input.value) {
        for (word of WORDS) {
            if (word.startsWith(input.value)) {
                html += `<li>${word}</li>`;
            }
        }
    }
    document.querySelector('ul').innerHTML = html;
});
```

---

## 📝 Summary

| Technology | Role | Analogy |
|-----------|------|---------|
| **HTML** | Structure | Skeleton |
| **CSS** | Presentation | Skin/Clothing |
| **JavaScript** | Behavior | Muscles/Brain |
| **Bootstrap** | Pre-built UI | Wardrobe |

---

> 📌 **Prev**: [Week 7 — SQL](../week7-sql/notes.md)  
> 📌 **Next**: [Week 9 — Flask](../week9-flask/notes.md)
