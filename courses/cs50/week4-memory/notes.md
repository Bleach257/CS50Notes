# Week 4 — Memory

> 📅 Source: [CS50 Lecture 4](https://cs50.harvard.edu/x/2026/notes/4/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Understand hexadecimal (base-16) number system
- Learn about memory addresses and pointers
- Master pointer arithmetic and string operations
- Use `malloc` for dynamic memory allocation
- Understand `scanf`, file I/O, and buffer overflow

---

## 📖 Key Concepts

### Hexadecimal

Base-16 counting system: `0 1 2 3 4 5 6 7 8 9 A B C D E F`

| Decimal | Hexadecimal |
|---------|-------------|
| 0       | 0x00        |
| 10      | 0x0A        |
| 15      | 0x0F        |
| 255     | 0xFF        |

- Prefixed with `0x` to distinguish from decimal
- More compact than binary for representing data

### Pointers

Two key operators:
- **`&`** — Get the **address** of a variable
- **`*`** — Go **to** a memory address (dereference)

```c
int n = 50;
int *p = &n;        // p is a pointer to n
printf("%p\n", p);  // Print address (hex)
printf("%i\n", *p); // Print value at address: 50
```

**Pointers are typically stored as 8-byte values.**

### Strings Are Pointers

```c
// These are equivalent:
string s = "HI!";
char *s = "HI!";
```

CS50's `string` definition: `typedef char *string;`

**Memory verification:**
```c
char *s = "HI!";
printf("%p\n", s);      // First char address
printf("%p\n", &s[0]);  // Same
printf("%p\n", &s[1]);  // Next byte
printf("%p\n", &s[2]);  // Next
printf("%p\n", &s[3]);  // '\0' terminator
```

### Pointer Arithmetic

```c
char *s = "HI!";
printf("%c\n", s[0]);       // H
printf("%c\n", *(s + 1));   // I  (same as s[1])
printf("%c\n", *(s + 2));   // !  (same as s[2])

printf("%s\n", s);          // HI!
printf("%s\n", s + 1);      // I!
printf("%s\n", s + 2);      // !
```

### String Comparison — Critical!

```c
// ❌ WRONG — compares addresses, not content
if (s == t) { ... }

// ✅ CORRECT — compares actual string content
if (strcmp(s, t) == 0) { ... }
```

### Copying & `malloc`

**Shallow copy (wrong):**
```c
string t = s;  // Only copies the address!
t[0] = toupper(t[0]);  // Modifies BOTH s and t!
```

**Deep copy with `malloc`:**
```c
#include <stdlib.h>
#include <string.h>

char *s = get_string("s: ");
char *t = malloc(strlen(s) + 1);  // +1 for '\0'
if (t == NULL) return 1;

strcpy(t, s);  // or manual loop
t[0] = toupper(t[0]);

free(t);  // Always free malloc'd memory
```

### Valgrind

```bash
valgrind ./memory
```

Detects:
- Memory leaks (unfreed `malloc`)
- Out-of-bounds access

### Garbage Values

Newly allocated memory may contain **residual data**. Always initialize!

```c
int scores[1024];  // May contain garbage values
```

### Swapping Values

**Wrong (pass by value):**
```c
void swap(int a, int b) { int tmp = a; a = b; b = tmp; }
// Only swaps copies — original unchanged!
```

**Correct (pass by reference/pointer):**
```c
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
swap(&x, &y);
```

### Buffer Overflow

- **Heap overflow**: Exceeding allocated heap memory
- **Stack overflow**: Too many nested function calls
- Both are types of **buffer overflow**

### `scanf`

```c
int n;
scanf("%i", &n);  // Needs & for non-arrays

char s[4];
scanf("%s", s);   // Array name IS a pointer — but DANGEROUS!
```

⚠️ Risk: No input length control → buffer overflow possible.

### File I/O

**Write CSV:**
```c
FILE *file = fopen("phonebook.csv", "a");
if (file == NULL) return 1;

fprintf(file, "%s,%s\n", name, number);
fclose(file);
```

**Copy file (binary):**
```c
typedef unsigned char BYTE;

FILE *src = fopen(argv[1], "rb");
FILE *dst = fopen(argv[2], "wb");

BYTE b;
while (fread(&b, sizeof(b), 1, src) != 0)
    fwrite(&b, sizeof(b), 1, dst);

fclose(dst);
fclose(src);
```

---

## 📝 Summary

| Topic | Key Takeaway |
|-------|-------------|
| **Hexadecimal** | Base-16, prefixed with `0x` |
| **Pointers** | `&` gets address, `*` dereferences |
| **Strings** | Actually `char*` pointing to first character |
| **Pointer Arithmetic** | `*(s + 1)` equals `s[1]` |
| **String Comparison** | Use `strcmp()`, never `==` |
| **`malloc`** | Allocate; `strcpy` to copy; `free` when done |
| **Valgrind** | Tool to detect memory issues |
| **Swap** | Pass pointers, not values |
| **File I/O** | `fopen`, `fprintf`, `fclose` |
| **Buffer Overflow** | Heap and stack overflows are dangerous |

---

> 📌 **Prev**: [Week 3 — Algorithms](../week3-algorithms/notes.md)  
> 📌 **Next**: [Week 5 — Data Structures](../week5-data-structures/notes.md)
