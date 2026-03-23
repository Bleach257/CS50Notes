# Week 5 — Data Structures

> 📅 Date: _Not started yet_  
> 🎓 Source: [CS50 Lecture 5](https://cs50.harvard.edu/x/2024/weeks/5/)  
> ⏱ Duration: ~2 hours

---

## 🎯 Learning Objectives

- [ ] Implement linked lists in C
- [ ] Understand trees, binary search trees
- [ ] Understand hash tables and hash functions
- [ ] Understand tries
- [ ] Analyze trade-offs between data structures

---

## 📖 Key Concepts

> 📝 *Notes coming soon — work in progress*

### Data Structures Overview

| Structure | Insert | Search | Delete | Notes |
|-----------|--------|--------|--------|-------|
| Array | O(n) | O(n) / O(log n) | O(n) | Fixed size, fast access by index |
| Linked List | O(1) | O(n) | O(n) | Dynamic size, no random access |
| Hash Table | O(1)* | O(1)* | O(1)* | Fast but depends on hash function |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | Sorted, but can become unbalanced |
| Trie | O(k) | O(k) | O(k) | k = key length; great for strings |

### Linked List Node Structure

```c
typedef struct node
{
    int number;
    struct node *next;
}
node;
```

---

## 💻 Code Examples

> *To be filled in during/after lecture*

---

## 🧩 Problem Set Notes

> *To be filled in — typically involves implementing a spell checker with a hash table*

---

## ❓ Questions & Confusions

- [ ] When should I use a hash table vs a trie?
- [ ] How do you handle hash collisions?

---

## 🔗 Further Reading

- [CS50 Week 5 Notes](https://cs50.harvard.edu/x/2024/notes/5/)
- [Visualgo — Data Structures](https://visualgo.net/en)

---

*[← Week 4: Memory](../week4-memory/) · [Back to Index](../README.md) · [Next Week → Week 6: Python](../week6-python/)*
