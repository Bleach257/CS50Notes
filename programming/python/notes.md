# Python

> 📅 Last Updated: 2026-03-23  
> 🔗 Official: [Python Docs](https://docs.python.org/3/)

---

## 📖 Overview

Python is a high-level, interpreted programming language known for its readability and versatility. Used in web development, data science, automation, and more.

> "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."

---

## 💻 Language Basics

### Variables & Types

```python
# Variables
name = "Alice"
age = 25
height = 5.7
is_student = True

# Type hints (Python 3.5+)
def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You're {age} years old."
```

### Data Structures

| Type | Example | Mutability |
|------|---------|------------|
| List | `[1, 2, 3]` | ✅ |
| Tuple | `(1, 2, 3)` | ❌ |
| Set | `{1, 2, 3}` | ✅ (unique only) |
| Dict | `{"key": "value"}` | ✅ |

```python
# List
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[0] = "avocado"

# Dictionary
person = {"name": "Bob", "age": 30}
person["city"] = "NYC"
del person["age"]
```

---

## 🔄 Control Flow

### Conditionals

```python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Ternary operator
result = "even" if x % 2 == 0 else "odd"
```

### Loops

```python
# for loop
for i in range(10):
    print(i)

# while loop
while condition:
    # do something

# List comprehension
squares = [x**2 for x in range(10)]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
```

---

## 🎯 Functions

```python
def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b

# Default arguments
def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

# Variable arguments
def sum_all(*numbers: int) -> int:
    return sum(numbers)

def print_info(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
add = lambda a, b: a + b
```

---

## 📦 Useful Libraries

| Library | Purpose | Import |
|---------|---------|--------|
| `requests` | HTTP | `import requests` |
| `pandas` | Data analysis | `import pandas as pd` |
| `numpy` | Numerical computing | `import numpy as np` |
| `matplotlib` | Plotting | `import matplotlib.pyplot as plt` |

---

## 🧪 Common Patterns

### Reading a File

```python
with open("file.txt", "r") as f:
    content = f.read()

# Line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
```

### HTTP Request

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```

### Try-Except

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup here")
```

---

## ❓ Questions & Confusions

- [ ] When to use `is` vs `==`? (identity vs equality)
- [ ] How does Python's GIL affect threading?

---

## 🔗 Further Reading

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [PEP 8 — Style Guide](https://pep8.org/)

---

*[← Programming](../programming/) · [Back to Index](../../README.md)]*
