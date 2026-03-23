# Week 4 — Memory

> 📅 Date: _Not started yet_  
> 🎓 Source: [CS50 Lecture 4](https://cs50.harvard.edu/x/2024/weeks/4/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [ ] Understand pointers and memory addresses
- [ ] Use `malloc` and `free` for dynamic memory allocation
- [ ] Understand the stack vs the heap
- [ ] Work with files and file I/O in C
- [ ] Debug memory leaks with Valgrind

---

## 📖 Key Concepts

> 📝 *Notes coming soon — work in progress*

### Pointers Quick Reference

```c
int n = 50;
int *p = &n;      // p stores the address of n

printf("%i\n", n);    // 50  — the value
printf("%p\n", p);    // 0x... — the address
printf("%i\n", *p);   // 50  — dereference: value at address
```

### Dynamic Memory

```c
// Allocate
int *arr = malloc(10 * sizeof(int));

// Always check for NULL!
if (arr == NULL) return 1;

// Use it...

// Free when done
free(arr);
```

> ⚠️ **Common Pitfalls:**
> - Forgetting to `free()` → memory leak
> - Using memory after `free()` → use-after-free bug
> - Writing beyond allocated size → buffer overflow

---

## 💻 Code Examples

> *To be filled in during/after lecture*

---

## 🧩 Problem Set Notes

> *To be filled in — typically involves image filters (blur, grayscale, etc.)*

---

## ❓ Questions & Confusions

- [ ] What's the difference between stack and heap allocation?
- [ ] How does `valgrind` detect memory leaks?

---

## 🔗 Further Reading

- [CS50 Week 4 Notes](https://cs50.harvard.edu/x/2024/notes/4/)
- [Pointer Basics](https://www.tutorialspoint.com/cprogramming/c_pointers.htm)
- [Valgrind Quick Start](https://valgrind.org/docs/manual/quick-start.html)

---

*[← Week 3: Algorithms](../week3-algorithms/) · [Back to Index](../README.md) · [Next Week → Week 5: Data Structures](../week5-data-structures/)*
