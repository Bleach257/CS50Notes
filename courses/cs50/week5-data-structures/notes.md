# Week 5 — Data Structures

> 📅 Source: [CS50 Lecture 5](https://cs50.harvard.edu/x/2026/notes/5/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Understand abstract data types: queues, stacks
- Implement dynamic arrays with `malloc` and `realloc`
- Build and traverse linked lists in C
- Understand binary search trees and their search complexity
- Learn hashing, hash tables, and tries

---

## 📖 Key Concepts

### Queues — FIFO (First In, First Out)

Like a line at an amusement park.

```c
typedef struct
{
    person people[CAPACITY];
    int size;
} queue;
```

Operations: `enqueue` (add), `dequeue` (remove)

### Stacks — LIFO (Last In, First Out)

Like a stack of trays in a cafeteria.

```c
typedef struct
{
    person people[CAPACITY];
    int size;
} stack;
```

Operations: `push` (add to top), `pop` (remove from top)

### Dynamic Arrays

```c
int *list = malloc(3 * sizeof(int));
list[0] = 1; list[1] = 2; list[2] = 3;

// Resize with realloc
int *tmp = realloc(list, 4 * sizeof(int));
if (tmp == NULL) { free(list); return 1; }
list = tmp;
list[3] = 4;

free(list);
```

### Linked Lists

**Node structure:**
```c
typedef struct node
{
    int number;
    struct node *next;
} node;
```

**Insert at head:**
```c
node *n = malloc(sizeof(node));
n->number = get_int("Number: ");
n->next = list;
list = n;
```

**Insert at tail:**
```c
if (list == NULL)
    list = n;
else
    for (node *ptr = list; ptr != NULL; ptr = ptr->next)
        if (ptr->next == NULL)
        {
            ptr->next = n;
            break;
        }
```

**Free entire list:**
```c
node *ptr = list;
while (ptr != NULL)
{
    node *next = ptr->next;
    free(ptr);
    ptr = next;
}
```

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Insert at head | O(n) | O(1) |
| Search | O(n) | O(n) |
| Insert at tail | O(1) | O(n) |
| Index access | O(1) | O(n) |

### Binary Search Trees

**Search implementation:**
```c
bool search(node *tree, int number)
{
    if (tree == NULL) return false;
    else if (number < tree->number) return search(tree->left, number);
    else if (number > tree->number) return search(tree->right, number);
    else return true;
}
```

| Case | Complexity |
|------|------------|
| Balanced | O(log n) |
| Unbalanced | O(n) |

### Hash Tables

**The Holy Grail: O(1) access!**

- **Hash function**: Converts a value to an array index
- **Collision**: Two values hash to same index → use linked list

```c
unsigned int hash(const char *word)
{
    return toupper(word[0]) - 'A';
}
```

| Search | Memory |
|--------|--------|
| O(n) worst case | More memory = fewer collisions |

### Tries (Prefix Trees)

**Trees of arrays — always O(1) search!**

- Each node has an array of children (26 for letters)
- Following pointers from root spells out the word
- Memory-intensive but fastest lookup

---

## 📝 Summary

| Data Structure | Search | Insert | Memory |
|---------------|--------|--------|--------|
| Array | O(n) | O(n) | Low |
| Linked List | O(n) | O(1) head | Low |
| Binary Search Tree | O(log n) balanced | O(log n) balanced | Medium |
| Hash Table | O(n) worst, ~O(1) avg | O(1) avg | Medium |
| Trie | O(1) | O(1) | High |

---

> 📌 **Prev**: [Week 4 — Memory](../week4-memory/notes.md)  
> 📌 **Next**: [Week 6 — Python](../week6-python/notes.md)
