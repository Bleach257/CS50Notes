# Linked Lists

> 📅 Last Updated: 2026-03-23

---

## 📖 Overview

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Each element (node) contains data and a pointer to the next node.

> Arrays vs Linked Lists:
> - Arrays: Fast access by index (O(1)), slow insert/delete (O(n))
> - Linked Lists: Slow access by index (O(n)), fast insert/delete at head (O(1))

---

## 🏗️ Types of Linked Lists

| Type | Description |
|------|-------------|
| Singly Linked | Nodes point to next only |
| Doubly Linked | Nodes point to next and previous |
| Circular Linked | Last node points to head |

---

## 💻 Implementations

### Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Doubly Linked
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
```

---

### Singly Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add to end — O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add to beginning — O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Delete first occurrence — O(n)"""
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next:
            current.next = current.next.next

    def display(self):
        """Print all nodes"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Reverse in-place — O(n)"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
```

---

### Detect Cycle (Floyd's Tortoise and Hare)

```python
def has_cycle(head: Node) -> bool:
    """Detect if linked list has a cycle — O(n), O(1) space"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next        # Move 1 step
        fast = fast.next.next   # Move 2 steps

        if slow == fast:
            return True

    return False
```

---

### Find Middle Node

```python
def find_middle(head: Node) -> Node:
    """Find middle node using slow/fast pointers — O(n)"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

---

## 🧮 Complexity Analysis

| Operation | Singly Linked | Doubly Linked |
|-----------|---------------|---------------|
| Access at index | O(n) | O(n) |
| Insert at head | O(1) | O(1) |
| Insert at tail | O(n) | O(1) if tail pointer |
| Delete at head | O(1) | O(1) |
| Search | O(n) | O(n) |

---

## 🎯 Use Cases

- **Dynamic memory allocation** — size unknown upfront
- **Frequent insertions/deletions** — at beginning
- **Undo/Redo operations** — stack-like behavior
- **LRU Cache** — doubly linked list with hash map

---

## ❓ Questions & Confusions

- [ ] When to prefer linked list over array?
- [ ] How to efficiently merge two sorted linked lists?

---

## 🔗 Further Reading

- [GeeksforGeeks — Linked List](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [LeetCode — Linked List Tag](https://leetcode.com/tag/linked-list/)
- [Visualgo — Linked List](https://visualgo.net/en/list)

---

*[← Data Structures](../data-structures/) · [Back to Index](../../README.md)]*
