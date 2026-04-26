# Week 1 — C

> 📅 Source: [CS50 Lecture 1](https://cs50.harvard.edu/x/2026/notes/1/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Transition from Scratch to text-based programming (C)
- Understand source code, compilation, and machine code
- Learn C syntax: variables, conditionals, loops, functions
- Master command-line interface (CLI) basics
- Evaluate code on three axes: correctness, design, style

---

## 📖 Key Concepts

### Source Code & Compilation

```
Source Code → [Compiler] → Machine Code
```

- **Source code**: Human-readable instructions
- **Machine code**: 0s and 1s the computer understands
- **Compiler**: Translates source code to machine code

### Three Commands to Write/Run

```bash
code hello.c    # Create/open file in VS Code
make hello      # Compile
./hello         # Run
```

### Hello World

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

### From Scratch to C

| Scratch | C |
|---------|---|
| `say` block | `printf("hello, world\n");` |
| `ask` block | `get_string("What's your name? ")` |
| `join` block | `%s` format code |

### Escape Characters

| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\r` | Carriage return |
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |

### Header Files & Libraries

- `#include <stdio.h>` → Standard I/O (enables `printf`)
- `#include <cs50.h>` → CS50 library (enables `get_string`, `get_int`, etc.)

**CS50 helper functions**: `get_char`, `get_double`, `get_float`, `get_int`, `get_long`, `get_string`

### Hello, You

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

- `%s` = format code (placeholder) for strings

### Linux CLI Commands

| Command | Purpose |
|---------|---------|
| `cd` | Change directory |
| `cp` | Copy files |
| `ls` | List files |
| `mkdir` | Create directory |
| `mv` | Move/rename files |
| `rm` | Delete files |
| `rmdir` | Delete directory |

### Conditionals

```c
if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else
{
    printf("x is equal to y\n");
}
```

### Data Types & Format Codes

| Type | Format Code |
|------|-------------|
| `bool` | — |
| `char` | `%c` |
| `float` | `%f` |
| `int` | `%i` |
| `long` | `%li` |
| `string` | `%s` |

### Variables

```c
int counter = 0;
counter = counter + 1;  // or counter += 1; or counter++;
counter--;              // decrement
```

### Loops

**While loop:**
```c
int i = 0;
while (i < 3)
{
    printf("meow\n");
    i++;
}
```

**For loop (preferred):**
```c
for (int i = 0; i < 3; i++)
{
    printf("meow\n");
}
```

**Do-while loop (at least once):**
```c
int n;
do
{
    n = get_int("What's n? ");
}
while (n < 0);
```

### Functions

```c
#include <stdio.h>

void meow(int n);  // Function prototype

int main(void)
{
    meow(3);
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- **Scope**: Variables in `main` only exist within `main`; copies are passed to functions

### Code Quality — Three Axes

| Axis | Tool | Question |
|------|------|----------|
| **Correctness** | `check50` | Does it work? |
| **Design** | `design50` | Is it well-designed? |
| **Style** | `style50` | Is it readable? |

### Mario — Nested Loops

```c
#include <stdio.h>

int main(void)
{
    const int n = 3;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
```

### Operators & Overflow

| Operator | Meaning |
|----------|---------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo (remainder) |

- **Integer overflow**: `int` max is typically 2,147,483,647
- **Integer division truncates**: `7 / 2` = `3` (use `(float) x` for true division)
- **Floating-point imprecision**: Not all decimals can be exactly represented

---

## 📝 Summary

- Transitioned from Scratch blocks to C syntax
- Learned the edit → compile → run workflow
- Mastered variables, conditionals, loops, and functions
- Evaluated code on correctness, design, and style
- Understood type system, operators, and their limitations

---

> 📌 **Prev**: [Week 0 — Scratch](../week0-scratch/notes.md)  
> 📌 **Next**: [Week 2 — Arrays](../week2-arrays/notes.md)
