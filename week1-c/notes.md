# Week 1 — C

> 📅 Date: 2026-03-23  
> 🎓 Source: [CS50 Lecture 1](https://cs50.harvard.edu/x/2024/weeks/1/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [x] Write and compile a C program
- [x] Understand data types, variables, and operators
- [x] Use conditionals (`if`, `else if`, `else`, `switch`)
- [x] Use loops (`for`, `while`, `do-while`)
- [x] Call functions from the CS50 library

---

## 📖 Key Concepts

### Program Structure in C

Every C program has this basic skeleton:

```c
#include <stdio.h>    // Include standard I/O library

int main(void)        // Entry point — program starts here
{
    // your code
    return 0;         // 0 = success
}
```

> 💡 **Key Insight:** Unlike Python, C must be **compiled** before running. Source code (`.c`) → compiler → machine code (binary executable).

---

### Data Types

| Type | Size | Range / Use |
|------|------|-------------|
| `int` | 4 bytes | Integers: −2,147,483,648 to 2,147,483,647 |
| `long` | 8 bytes | Larger integers |
| `float` | 4 bytes | Decimal numbers (less precise) |
| `double` | 8 bytes | Decimal numbers (more precise) |
| `char` | 1 byte | Single character: `'A'`, `'z'` |
| `bool` | 1 byte | `true` or `false` (needs `<stdbool.h>`) |
| `string` | varies | CS50 library type (array of chars) |

---

### Operators

```c
// Arithmetic
+  -  *  /  %     // modulo (remainder)

// Comparison
==  !=  <  >  <=  >=

// Logical
&&   // AND
||   // OR
!    // NOT

// Assignment shortcuts
x += 1;   // same as x = x + 1
x++;      // increment by 1
x--;      // decrement by 1
```

---

### Conditionals

```c
if (x > 0)
{
    printf("Positive\n");
}
else if (x < 0)
{
    printf("Negative\n");
}
else
{
    printf("Zero\n");
}
```

---

### Loops

```c
// for loop — when you know how many times
for (int i = 0; i < 10; i++)
{
    printf("%i\n", i);   // prints 0–9
}

// while loop — when condition-based
int i = 0;
while (i < 10)
{
    printf("%i\n", i);
    i++;
}

// do-while — always runs at least once (good for user input)
int n;
do
{
    n = get_int("Enter a positive number: ");
}
while (n < 1);
```

---

## 💻 Code Examples

### Hello, World

```c
#include <stdio.h>

int main(void)
{
    printf("Hello, world!\n");
    return 0;
}
```

**Compile & run:**
```bash
make hello      # or: clang -o hello hello.c
./hello
```

### Using CS50 Library

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");
    printf("Hello, %s!\n", name);
    return 0;
}
```

### Format Specifiers for `printf`

| Specifier | Type |
|-----------|------|
| `%i` or `%d` | int |
| `%f` | float / double |
| `%c` | char |
| `%s` | string |
| `%li` | long |

---

## 🧩 Problem Set Notes

### Problem: Hello

**Description:** Ask user for their name and print "hello, [name]"

**Solution:** Use `get_string()` and `printf()` with `%s` format specifier.

### Problem: Mario (Less / More)

**Description:** Print a pyramid of `#` characters using loops.

**Approach:**
1. Get height from user (1–8), re-prompt if invalid → `do-while`
2. Outer loop: each row
3. Inner loops: spaces, then hashes

```c
for (int i = 0; i < height; i++)
{
    // Print spaces: (height - 1 - i) spaces
    for (int j = 0; j < height - 1 - i; j++)
        printf(" ");
    // Print hashes: (i + 1) hashes
    for (int j = 0; j <= i; j++)
        printf("#");
    printf("\n");
}
```

---

## ❓ Questions & Confusions

- [ ] Why does integer division in C truncate instead of round?
- [ ] What's the difference between `float` precision loss vs `double`?

---

## 🔗 Further Reading

- [CS50 Week 1 Notes](https://cs50.harvard.edu/x/2024/notes/1/) — Official notes
- [C Reference](https://en.cppreference.com/w/c) — Language reference
- [CS50 Manual Pages](https://manual.cs50.io/) — CS50 library functions

---

*[← Week 0: Scratch](../week0-scratch/) · [Back to Index](../README.md) · [Next Week → Week 2: Arrays](../week2-arrays/)*
