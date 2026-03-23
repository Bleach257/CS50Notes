# Week 2 — Arrays

> 📅 Date: 2026-03-23  
> 🎓 Source: [CS50 Lecture 2](https://cs50.harvard.edu/x/2024/weeks/2/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [ ] Understand how arrays store data in contiguous memory
- [ ] Declare, initialize, and access arrays in C
- [ ] Work with strings as arrays of characters
- [ ] Understand command-line arguments (`argc`, `argv`)
- [ ] Get introduced to cryptography concepts

---

## 📖 Key Concepts

### Arrays

An array stores **multiple values of the same type** in contiguous memory locations.

```c
// Declaration & initialization
int scores[3] = {72, 85, 91};

// Access by index (0-based!)
printf("%i\n", scores[0]);   // 72
printf("%i\n", scores[1]);   // 85
printf("%i\n", scores[2]);   // 91
```

> 💡 **Key Insight:** Arrays in C don't store their own length. You must track the size yourself. Accessing out-of-bounds is **undefined behavior** — it won't crash reliably, which makes it dangerous.

---

### Strings are Arrays of Characters

```c
string s = "Hi!";
// In memory: ['H']['i']['!']['\0']
//              s[0] s[1] s[2] s[3]
```

The **null terminator** `'\0'` marks the end of a string — always takes 1 extra byte.

```c
#include <string.h>

int len = strlen("Hello");   // 5 (doesn't count '\0')
```

---

### Command-Line Arguments

```c
int main(int argc, char *argv[])
{
    // argc = number of arguments (including program name)
    // argv = array of argument strings
    // argv[0] = program name
    // argv[1] = first argument, etc.

    if (argc == 2)
        printf("Hello, %s!\n", argv[1]);
    else
        printf("Usage: ./hello [name]\n");
}
```

---

### Useful `<string.h>` Functions

| Function | Description |
|----------|-------------|
| `strlen(s)` | Length of string |
| `strcmp(s1, s2)` | Compare strings (0 = equal) |
| `strcpy(dst, src)` | Copy string |
| `strcat(dst, src)` | Concatenate strings |
| `toupper(c)` / `tolower(c)` | Change case (from `<ctype.h>`) |

---

## 💻 Code Examples

### Iterating over a String

```c
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
```

### Caesar Cipher (Shift each letter by key)

```c
// Rotate a letter by key positions
char rotate(char c, int key)
{
    if (isupper(c))
        return (c - 'A' + key) % 26 + 'A';
    else if (islower(c))
        return (c - 'a' + key) % 26 + 'a';
    else
        return c;
}
```

---

## 🧩 Problem Set Notes

### Problem: Readability (Coleman-Liau Index)

**Formula:** `index = 0.0588 * L - 0.296 * S - 15.8`  
Where L = avg letters per 100 words, S = avg sentences per 100 words.

**Approach:**
1. Count letters, words, sentences
2. Calculate L and S
3. Apply formula, round to nearest int

### Problem: Caesar / Substitution

**Description:** Encrypt text by shifting (Caesar) or substituting (Substitution) letters.

**Key insight for Caesar:** Use modulo 26 to wrap around the alphabet.

---

## ❓ Questions & Confusions

- [ ] Why does C use `strcmp` instead of `==` for string comparison?
- [ ] What exactly is `char *argv[]` — a pointer to an array?

---

## 🔗 Further Reading

- [CS50 Week 2 Notes](https://cs50.harvard.edu/x/2024/notes/2/)
- [C String Functions Reference](https://cplusplus.com/reference/cstring/)

---

*[← Week 1: C](../week1-c/) · [Back to Index](../README.md) · [Next Week → Week 3: Algorithms](../week3-algorithms/)*
