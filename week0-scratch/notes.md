# Week 0 — Scratch & Computational Thinking

> 📅 Date: 2026-03-23  
> 🎓 Source: [CS50 Lecture 0](https://cs50.harvard.edu/x/2024/weeks/0/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [x] Understand what computer science really is
- [x] Think computationally — inputs, outputs, algorithms
- [x] Get familiar with Scratch as a visual programming language
- [x] Understand basic programming constructs: loops, conditions, functions, events

---

## 📖 Key Concepts

### What is Computer Science?

Computer science is fundamentally about **problem solving**. We take an **input**, apply an **algorithm**, and get an **output**.

```
Input  →  [ Algorithm ]  →  Output
```

> 💡 **Key Insight:** An algorithm is a step-by-step set of instructions for solving a problem. The quality of your algorithm matters — a bad algorithm can be *correct* but still terribly slow.

---

### Representing Information — Binary

Computers only understand **0s and 1s** (bits). Everything is encoded in binary.

| Decimal | Binary |
|---------|--------|
| 0       | 0      |
| 1       | 1      |
| 2       | 10     |
| 3       | 11     |
| 4       | 100    |
| 8       | 1000   |

- **1 bit** = 0 or 1
- **1 byte** = 8 bits → can represent 0–255

**ASCII** maps numbers to characters: `A = 65`, `a = 97`, `0 = 48`

**Unicode** extends ASCII to support all languages and emoji.

---

### Algorithms & Efficiency

Consider finding a name in a phone book:

| Approach | Steps (1000 pages) | Big-O |
|----------|-------------------|-------|
| Page by page | 1000 | O(n) |
| Tear in half each time | ~10 | O(log n) |

> 💡 **Key Insight:** O(log n) is dramatically faster than O(n) for large inputs. This is why **binary search** matters.

---

### Scratch — Building Blocks

Scratch teaches the core building constructs used in *every* programming language:

| Concept | Scratch Block | Real-world equivalent |
|---------|--------------|----------------------|
| Sequence | Stack blocks top to bottom | Line-by-line code execution |
| Loop | `repeat` / `forever` | `for`, `while` loops |
| Condition | `if/else` | `if/else` statements |
| Variable | `set [x] to 0` | `int x = 0;` |
| Function | Custom block | function / method definition |
| Event | `when 🚩 clicked` | event listeners |

---

## 💻 Code Examples

### Scratch: Simple Loop

```
when 🚩 clicked
  repeat 3
    say "Hello!" for 1 second
```

**What this does:** Prints "Hello!" 3 times — equivalent to a `for` loop.

### Scratch: Condition

```
when 🚩 clicked
  if <touching [wall]?> then
    turn 180 degrees
  end
```

**What this does:** Checks a condition and changes behavior — equivalent to an `if` statement.

---

## 🧩 Problem Set Notes

### Problem Set 0 — Scratch Project

**Description:** Create any interactive Scratch project using at least:
- ≥ 2 sprites
- ≥ 3 scripts total
- Conditions, loops, custom blocks, and variables

**My project idea:** A simple quiz game with score tracking.

**Key challenge:** Syncing events between sprites using `broadcast`.

---

## ❓ Questions & Confusions

- [x] What exactly is a "bit" vs a "byte"? → *8 bits = 1 byte*
- [ ] How does floating point representation work in binary?

---

## 🔗 Further Reading

- [CS50 Week 0 Notes](https://cs50.harvard.edu/x/2024/notes/0/) — Official notes
- [Scratch](https://scratch.mit.edu/) — Try it yourself
- [ASCII Table](https://www.asciitable.com/) — Character encoding reference

---

*[Back to Index](../README.md) · [Next Week → Week 1: C](../week1-c/)*
