# Week 6 — Python

> 📅 Source: [CS50 Lecture 6](https://cs50.harvard.edu/x/2026/notes/6/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Transition from C (compiled) to Python (interpreted)
- Learn Python syntax: variables, types, loops, conditionals
- Understand OOP basics (string methods)
- Work with lists, dictionaries, and exception handling
- Read/write CSV files and use command-line arguments

---

## 📖 Key Concepts

### Hello Python

**C vs Python:**
```c
#include <stdio.h>
int main(void) { printf("hello, world\n"); }
```
```python
print("hello, world")
```

- Python is **interpreted** (no separate compilation step)
- No semicolons, no curly braces, uses **indentation**

### Speller in Python

```python
words = set()

def check(word):
    return word.lower() in words

def load(dictionary):
    with open(dictionary) as file:
        words.update(file.read().splitlines())
    return True

def size():
    return len(words)

def unload():
    return True
```

> 💡 No manual memory management — Python handles it automatically!

### Variables & Types

```python
counter = 0        # No type declaration needed
counter += 1       # No counter++
```

| Type | Description |
|------|-------------|
| `bool` | Boolean |
| `float` | Floating point |
| `int` | Integer |
| `str` | String |
| `list` | Mutable sequence |
| `dict` | Key-value pairs |
| `set` | Unique values |
| `tuple` | Immutable sequence |
| `range` | Number sequence |

### Strings

```python
# Concatenation
print("hello, " + answer)

# Auto space
print("hello,", answer)

# f-strings (preferred)
print(f"hello, {answer}")
```

### Conditionals

```python
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# List membership check
if s in ["y", "yes"]:
    print("Agreed.")
```

### Loops

```python
# For loop
for i in range(3):
    print("meow")

# While loop
i = 0
while i < 3:
    print("meow")
    i += 1

# Iterate over characters
for c in before:
    print(c.upper(), end="")
```

### Functions & Abstraction

```python
def main():
    meow(3)

def meow(n):
    for i in range(n):
        print("meow")

main()
```

### Exceptions

```python
try:
    n = int(input("Input: "))
    print("Integer.")
except ValueError:
    print("Not integer.")
```

### Lists

```python
scores = [72, 73, 33]
scores.append(get_int("Score: "))

average = sum(scores) / len(scores)
print(f"Average: {average}")
```

### Dictionaries

```python
people = {
    "Kelly": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

name = get_string("Name: ")
if name in people:
    print(f"Number: {people[name]}")
```

### OOP — String Methods

```python
s = input("s: ")
t = s.capitalize()  # Returns new string, s unchanged
```

### Command-Line Arguments

```python
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
```

### CSV Files

```python
import csv

# Using csv.DictReader
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["language"])
```

```python
# Writing CSV
with open("phonebook.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, number])
```

### Third-Party Libraries

```bash
pip install cs50
pip install cowsay
pip install qrcode
```

---

## 📝 Summary

| C Feature | Python Equivalent |
|-----------|-------------------|
| `printf` | `print()` |
| `get_string` | `input()` |
| `strcmp` | `==` |
| `malloc`/`free` | Automatic |
| `{ }` blocks | Indentation |
| `counter++` | `counter += 1` |
| `switch` | `if/elif/else` |

> Your skills aren't limited to one language. This course teaches you how to learn *any* language!

---

> 📌 **Prev**: [Week 5 — Data Structures](../week5-data-structures/notes.md)  
> 📌 **Next**: [Week 7 — SQL](../week7-sql/notes.md)
