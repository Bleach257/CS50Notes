# Week 0 — Scratch & Computational Thinking

> 📅 Source: [CS50 Lecture 0](https://cs50.harvard.edu/x/2026/notes/0/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Understand AI's relationship with programming fundamentals
- Learn how computers represent information (binary, ASCII, Unicode, RGB)
- Understand algorithms and their efficiency (Big O notation)
- Get familiar with Scratch as a visual programming language
- Master pseudocode as a fundamental programming skill
- Learn basic programming constructs: loops, conditions, functions, events

---

## 📖 Key Concepts

### Welcome & AI

- AI is bringing new advances to computer science, but **learning fundamentals + being empowered by AI = new opportunities**
- Understanding, creating, and organizing code makes you the driver and navigator

### Visual Studio Code & First Program

```python
from openai import OpenAI

client = OpenAI()

user_prompt = input("Prompt: ")
system_prompt = "Limit your answer to one sentence. Pretend you're a cat."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5"
)

print(response.output_text)
```

> 💡 **Only 10 lines of code to build a powerful program!**

### Representing Information — Binary

Computers only understand **0s and 1s** (bits).

```
Position:  2²   2¹   2⁰
Weights:   4    2    1

Example: 0 1 1 = 3
```

- **1 bit** = 0 or 1 (binary digit)
- **1 byte** = 8 bits → can represent 0–255
- `00000101` = decimal 5
- `11111111` = decimal 255

### ASCII

**ASCII** maps binary patterns to characters:

| Binary   | Decimal | Character |
|----------|---------|-----------|
| 01000001 | 65      | A         |
| 01001000 | 72      | H         |
| 01001001 | 73      | I         |
| 00100001 | 33      | !         |

### Unicode

- Extends ASCII to support all languages, special characters, and **emoji**
- Standardized across devices (though rendering may vary)

### RGB

- **RGB** = Red, Green, Blue
- Three bytes form the color of each pixel
- **Image** = collection of RGB values
- **Video** = sequence of images
- **Music** = various byte combinations

### Algorithms & Efficiency

**Algorithm**: A step-by-step set of instructions for solving a problem.

| Method | Big O | Description |
|--------|-------|-------------|
| Read page by page | O(n) | 100 names → up to 100 steps |
| Two pages at a time | O(n/2) | Twice as fast |
| Split in half (binary) | O(log₂n) | Doubling the problem adds only 1 step |

### Pseudocode

**Pseudocode**: Human-readable instructions describing algorithm steps.

```
1   Pick up phone book
2   Open to middle of phone book
3   Look at page
4   If person is on page
5       Call person
6   Else if person is earlier in book
7       Open to middle of left half
8       Return to line 3
9   Else if person is later in book
10      Open to middle of right half
11      Return to line 3
12  Else
13      Quit
```

### Four Building Blocks of Programming

| Element | Example | Term |
|---------|---------|------|
| Verb-starting lines | "pick up", "open", "look at" | **Functions** |
| Conditional keywords | "if", "else if" | **Conditionals** |
| True/false expressions | "person is earlier" | **Boolean Expressions** |
| Go-to lines | "return to line 3" | **Loops** |

---

## 🧩 Scratch Programming

### Hello World

```scratch
when green flag clicked
say [hello, world]
```

### Interactive — Hello, You

```scratch
when green flag clicked
ask [What's your name?] and wait
say (join [hello,] (answer))
```

### Loops & Abstraction

**Before (repetitive):**
```scratch
when green flag clicked
play sound (Meow v) until done
wait (1) seconds
play sound (Meow v) until done
wait (1) seconds
play sound (Meow v) until done
wait (1) seconds
```

**After (with loop):**
```scratch
when green flag clicked
repeat (3)
play sound (Meow v) until done
wait (1) seconds
```

**With custom function:**
```scratch
define meow n times
repeat (n)
play sound [meow v] until done
wait (1) seconds

when green flag clicked
meow (3) times
```

### Conditionals

```scratch
when green flag clicked
forever
if <touching (mouse-pointer v)?> then
play sound (Meow v) until done
```

### Oscartime Game — Collision Detection

```scratch
when green flag clicked
forever
if <touching [Oscar v] ?> then
go to x: (pick random (0) to (240)) y: (180)
```

### Ivy's Hardest Game — Keyboard Input

```scratch
define listen for keyboard
if <key (up arrow v) pressed?> then
change y by (1)
end
if <key (down arrow v) pressed?> then
change y by (-1)
end
if <key (right arrow v) pressed?> then
change x by (1)
end
if <key (left arrow v) pressed?> then
change x by (-1)
end
```

---

## 📝 Summary

- AI empowers but doesn't replace learning fundamentals
- Computers use **binary** (0s and 1s) to represent everything
- **ASCII** maps numbers to characters; **Unicode** extends to emoji
- **RGB** values create colors; images/videos/music are all bytes
- **Algorithms** vary in efficiency — prefer O(log n) over O(n)
- **Pseudocode** bridges human thinking and code
- Programming's four building blocks: **functions, conditionals, boolean expressions, loops**
- Scratch demonstrates all these concepts visually

---

> 📌 **Next**: [Week 1 — C](../week1-c/notes.md)
