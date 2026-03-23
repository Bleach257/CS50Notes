# Sorting Algorithms

> 📅 Last Updated: 2026-03-23

---

## 📖 Overview

Sorting rearranges elements into a specific order (typically ascending). The choice of algorithm depends on data size, constraints, and stability requirements.

---

## 📊 Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |

---

## 💻 Algorithm Implementations

### Merge Sort

```python
def merge_sort(arr):
    """Divide and conquer — O(n log n)"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**Key insight:** Always O(n log n), but uses extra space.

---

### Quick Sort

```python
def quick_sort(arr):
    """Divide and conquer — O(n log n) average, O(n²) worst"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

**Key insight:** In-place, efficient in practice, but pivot choice matters.

---

### Binary Search (for sorted data)

```python
def binary_search(arr, target):
    """O(log n) — requires sorted array"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
```

---

## 🧠 When to Use Which

| Scenario | Recommendation |
|----------|----------------|
| Small data (< 1000) | Insertion sort (fast, simple) |
| General purpose, stability needed | Merge sort |
| Average case, in-place | Quick sort |
| Minimal memory usage | Heap sort |
| Built-in | Use language's `sort()` (usually Timsort) |

---

## ❓ Questions & Confusions

- [ ] How does Python's `sort()` implement Timsort?
- [ ] What's the best pivot selection strategy for Quick Sort?

---

## 🔗 Further Reading

- [Sorting Algorithm Visualizer](https://visualgo.net/en/sorting)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Wikipedia — Sorting Algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)

---

*[← Algorithms](../algorithms/) · [Back to Index](../../README.md)]*
