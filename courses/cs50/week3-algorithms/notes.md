# Week 3 — Algorithms

> 📅 Source: [CS50 Lecture 3](https://cs50.harvard.edu/x/2026/notes/3/)  
> 🎓 Course: CS50x 2026  
> 👨‍🏫 Instructor: David J. Malan

---

## 🎯 Learning Objectives

- Implement search algorithms: linear search, binary search
- Implement sorting algorithms: selection sort, bubble sort, merge sort
- Understand and apply Big O, Omega, and Theta notation
- Learn recursion and its base/recursive cases
- Use `struct` to create custom data types

---

## 📖 Key Concepts

### Linear Search

**Check each element one by one.**

```pseudocode
For i from 0 to n-1
    If target is at doors[i]
        Return true
Return false
```

**Code (integers):**
```c
int numbers[] = {20, 500, 10, 5, 100, 1, 50};
int n = get_int("Number: ");
for (int i = 0; i < 7; i++)
{
    if (numbers[i] == n)
    {
        printf("Found\n");
        return 0;
    }
}
printf("Not found\n");
return 1;
```

> ⚠️ **Strings**: Never use `==` for comparison — use `strcmp()` from `<string.h>`.

### Binary Search

**Requires a sorted array. Halves the search space each step.**

```pseudocode
If no doors left
    Return false
If target is behind middle door
    Return true
Else if target < middle
    Search left half
Else if target > middle
    Search right half
```

### Big O Notation

| Symbol | Meaning | Description |
|--------|---------|-------------|
| O | Upper bound | Worst case |
| Ω | Lower bound | Best case |
| Θ | Tight bound | Best and worst are the same |

### Running Time Comparison (slowest → fastest)

| Big O | Name | Example |
|-------|------|---------|
| O(n²) | Quadratic | Selection sort (worst & best) |
| O(n log n) | Linearithmic | Merge sort |
| O(n) | Linear | Linear search |
| O(log n) | Logarithmic | Binary search |
| O(1) | Constant | Array index access |

### Structs

```c
typedef struct
{
    string name;
    string number;
} person;

person people[3];
people[0].name = "Kelly";
people[0].number = "+1-617-495-1000";
```

### Selection Sort

```pseudocode
For i from 0 to n–1
    Find smallest number between numbers[i] and numbers[n-1]
    Swap smallest with numbers[i]
```

**Complexity:**
- Worst: O(n²)
- Best: Ω(n²)

### Bubble Sort

```pseudocode
Repeat n-1 times
    For i from 0 to n–2
        If numbers[i] and numbers[i+1] out of order
            Swap them
    If no swaps
        Quit
```

**Complexity:**
- Worst: O(n²)
- Best: Ω(n)

### Recursion

A function that **calls itself**.

| Term | Definition |
|------|------------|
| **Base case** | Condition that stops recursion |
| **Recursive case** | Part that calls itself with modified input |

**Pyramid — Iterative:**
```c
void draw(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i + 1; j++)
            printf("#");
        printf("\n");
    }
}
```

**Pyramid — Recursive:**
```c
void draw(int n)
{
    if (n <= 0) return;     // Base case
    draw(n - 1);            // Recursive case
    for (int i = 0; i < n; i++)
        printf("#");
    printf("\n");
}
```

### Merge Sort

```pseudocode
If only one number
    Quit
Else
    Sort left half
    Sort right half
    Merge sorted halves
```

**Complexity:**
- Worst: O(n log n)
- Best: Ω(n log n)
- **Θ(n log n)** — always the same

---

## 📝 Summary

| Topic | Key Takeaway |
|-------|-------------|
| **Linear Search** | O(n) — check every element |
| **Binary Search** | O(log n) — halve search space (requires sorted data) |
| **Selection Sort** | O(n²) worst and best |
| **Bubble Sort** | O(n²) worst, Ω(n) best |
| **Merge Sort** | Θ(n log n) — always efficient |
| **Recursion** | Base case + recursive case |
| **Structs** | Custom data types with dot notation |
| **Big O** | Focus on the shape of the growth curve |

---

> 📌 **Prev**: [Week 2 — Arrays](../week2-arrays/notes.md)  
> 📌 **Next**: [Week 4 — Memory](../week4-memory/notes.md)
