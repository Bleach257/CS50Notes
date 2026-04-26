# Week 2 — Arrays

> 📅 Source: [CS50 Lecture 2](https://cs50.harvard.edu/x/2026/notes/2/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Learn how compilers work (preprocessing, compiling, assembling, linking)
- Master debugging techniques (rubber duck, printf, debug50)
- Understand arrays as contiguous memory
- Learn that strings are arrays of characters (ending with `\0`)
- Implement string operations manually and with libraries
- Use command-line arguments in C programs

---

## 📖 Key Concepts

### Debugging

**Rubber Duck Debugging**: Talk through your code with an inanimate object (or person) to reason about bugs.

**printf debugging**: Insert print statements to trace variable values.

**debug50**: VS Code's built-in debugger.
1. Set a breakpoint (red dot on line number)
2. Run `debug50 ./program`
3. Step through code, inspecting variables

### Compiling — Four Steps

```
Source Code → [Preprocessing] → [Compiling] → [Assembling] → [Linking] → Machine Code
```

1. **Preprocessing**: `#include` directives are replaced with actual header file contents
2. **Compiling**: Source code → Assembly code
3. **Assembling**: Assembly code → Machine code (0s and 1s)
4. **Linking**: Merges your code with pre-compiled libraries → Final executable

### Data Types & Memory

| Type | Bytes (typical) |
|------|-----------------|
| `bool` | 1 |
| `char` | 1 |
| `int` | 4 |
| `long` | 8 |
| `float` | 4 |
| `double` | 8 |
| `string` | variable |

### Arrays

**Arrays store values in contiguous memory locations.**

```c
int scores[3];
scores[0] = 72;
scores[1] = 73;
scores[2] = 33;
```

**With loop input:**
```c
#include <cs50.h>
#include <stdio.h>

const int N = 3;

float average(int length, int array[]);

int main(void)
{
    int scores[N];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Score: ");
    }
    printf("Average: %f\n", average(N, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
```

### Strings

**Strings are arrays of `char`, terminated by `\0` (NUL).**

```c
// These are equivalent:
string s = "HI!";
char *s = "HI!";
```

**CS50's `string` is actually:** `typedef char *string;`

```c
char *s = "HI!";
printf("%c%c%c\n", s[0], s[1], s[2]);  // H I !
printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);  // 72 73 33 0
```

### String Length

**Manual:**
```c
int string_length(string s)
{
    int n = 0;
    while (s[n] != '\0')
    {
        n++;
    }
    return n;
}
```

**With library:**
```c
#include <string.h>
int length = strlen(name);
```

### String Case Conversion

**Manual (ASCII):**
```c
// 'a' = 97, 'A' = 65, difference = 32
if (s[i] >= 'a' && s[i] <= 'z')
{
    printf("%c", s[i] - 32);
}
```

**Using ctype.h:**
```c
#include <ctype.h>
printf("%c", toupper(s[i]));
```

### Command-Line Arguments

```c
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}
```

- `argc` = argument count
- `argv[0]` = program name, `argv[1]` = first argument

### Exit Status

```c
if (argc != 2)
{
    printf("Missing command-line argument\n");
    return 1;  // Error
}
return 0;  // Success
```

Check with: `echo $?`

---

## 📝 Summary

1. **Compiling** — Four steps: preprocessing → compiling → assembling → linking
2. **Debugging** — Rubber duck, printf, debug50
3. **Arrays** — Contiguous memory locations
4. **Strings** — `char` arrays ending with `\0`
5. **String operations** — Manual ASCII manipulation or library functions
6. **Command-line arguments** — `argc` and `argv[]`
7. **Exit status** — `return 0` (success) or `return 1` (error)

---

> 📌 **Prev**: [Week 1 — C](../week1-c/notes.md)  
> 📌 **Next**: [Week 3 — Algorithms](../week3-algorithms/notes.md)
