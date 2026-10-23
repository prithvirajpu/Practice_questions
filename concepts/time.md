# Algorithm Notations and Their Uses

## 1. ⏱️ Big O Notation — O(n)

**📖 Definition:**

Big O describes an asymptotic upper bound on an algorithm's growth rate, commonly used to express worst-case time complexity.

**🎯 Why it's used:**
- Analyze how an algorithm scales as input grows.
- Compare algorithm efficiency.
- Estimate performance for large inputs.

**💻 Code Example:**

```python
def print_numbers(n):
    for i in range(n):
        print(i)
```

**⏱️ Time Complexity:** `O(n)`

**🌍 Use case:** Iterating through a list of `n` elements.

---

## 2. 📉 Big Omega Notation — Ω(n)

**📖 Definition:**

Big Omega describes an asymptotic lower bound on an algorithm's growth rate.

**🎯 Why it's used:**
- Understand lower-bound performance.
- Describe how quickly an algorithm must grow asymptotically.

**💻 Code Example:**

```python
def print_first_item(items):
    print(items[0])
```

**⏱️ Time Complexity:** `Θ(1)` for a nonempty list, so it is also `Ω(1)`.

**🌍 Use case:** Describing lower bounds for algorithms. Omega notation alone does not automatically mean best-case complexity.

---

## 3. 📈 Big Theta Notation — Θ(n)

**📖 Definition:**

Big Theta describes a tight asymptotic bound: the growth rate is bounded both above and below by the same order.

**🎯 Why it's used:**
- Describe an algorithm's asymptotic growth precisely.
- Show when upper and lower bounds match.

**💻 Code Example:**

```python
def print_items(items):
    for item in items:
        print(item)
```

**⏱️ Time Complexity:** `Θ(n)`

**🌍 Use case:** Describing an algorithm that processes every item in a list.

---

## 4. ⚡ Constant Time — O(1)

**📖 Definition:**

An operation takes constant time relative to input size.

**💻 Code Example:**

```python
def get_first(items):
    return items[0]
```

**⏱️ Time Complexity:** `O(1)`, assuming the list is nonempty and standard array indexing.

**🌍 Use case:** Accessing an element by index in a Python list.

---

## 5. 🔍 Logarithmic Time — O(log n)

**📖 Definition:**

The number of operations grows logarithmically as the input size increases.

**💻 Code Example:**

```python
def binary_search(items, target):
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

**⏱️ Time Complexity:** `O(log n)`

**🌍 Use case:** Searching a sorted list using binary search.

---

## 6. 🔁 Linear Time — O(n)

**📖 Definition:**

The number of operations grows proportionally to the input size.

**💻 Code Example:**

```python
def find_item(items, target):
    for item in items:
        if item == target:
            return True
    return False
```

**⏱️ Time Complexity:** Worst case `O(n)`.

**🌍 Use case:** Searching an unsorted list.

---

## 7. 🔀 Linearithmic Time — O(n log n)

**📖 Definition:**

The growth rate is proportional to `n log n`.

**💻 Code Example:**

```python
items = [5, 2, 8, 1, 3]
items.sort()
```

**⏱️ Time Complexity:** Python's Timsort has worst-case `O(n log n)` time complexity.

**🌍 Use case:** Efficient comparison-based sorting algorithms such as merge sort and heap sort.

---

## 8. 🔄 Quadratic Time — O(n²)

**📖 Definition:**

The number of operations can grow proportionally to the square of the input size.

**💻 Code Example:**

```python
def print_pairs(items):
    for first in items:
        for second in items:
            print(first, second)
```

**⏱️ Time Complexity:** `O(n²)`

**🌍 Use case:** Comparing every element with every other element.

---

## 9. 💥 Exponential Time — O(2ⁿ)

**📖 Definition:**

The running time can double for each additional input element.

**💻 Code Example:**

```python
def subsets_count(n):
    return 2 ** n
```

**⏱️ Time Complexity:** `O(2ⁿ)` for generating all subsets of an `n`-element set, because there are \(2^n\) subsets.

**🌍 Use case:** Brute-force subset enumeration and some recursive algorithms.

---

## 10. 🧮 Factorial Time — O(n!)

**📖 Definition:**

The number of operations grows factorially with input size.

**💻 Code Example:**

```python
from itertools import permutations

items = [1, 2, 3]

for arrangement in permutations(items):
    print(arrangement)
```

**⏱️ Time Complexity:** Generating all permutations takes at least `Ω(n!)` outputs and typically `Θ(n · n!)` time when constructing each permutation.

**🌍 Use case:** Brute-force solutions that examine all possible orderings.

---

## 11. 💾 Space Complexity — O(n)

**📖 Definition:**

Space complexity describes how an algorithm's memory usage grows with input size.

**💻 Code Example:**

```python
def duplicate_items(items):
    result = []

    for item in items:
        result.append(item)

    return result
```

**💾 Space Complexity:** `O(n)` auxiliary space for the copied list.

**🌍 Use case:** Understanding the memory needed to store additional data structures.

---

## 12. 🔙 Backtracking Notation — Choose, Explore, Undo

**📖 Definition:**

Backtracking explores possible solutions by making a choice, recursively exploring it, and undoing the choice to try another possibility.

**💻 Code Example:**

```python
def generate_subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current.copy())

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

**🎯 Key pattern:**

`Choose → Explore → Undo`

**🌍 Use case:** Subsets, permutations, Sudoku, and N-Queens.

---

## 13. 🧵 Recursion Notation — T(n)

**📖 Definition:**

`T(n)` represents the running time of an algorithm for an input of size `n`. A recurrence relation expresses the running time in terms of smaller inputs.

**💻 Code Example:**

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

**⏱️ Time Complexity:** `T(n) = T(n - 1) + O(1)`, giving `Θ(n)` time.

**💾 Space Complexity:** `O(n)` due to the recursive call stack.

**🌍 Use case:** Analyzing recursive algorithms such as factorial and tree traversal.

---

## 14. 🌳 Binary Tree Height — O(log n)

**📖 Definition:**

A balanced binary tree has height proportional to `log n`, where `n` is the number of nodes.

**🎯 Why it's used:**
- Analyze search and insertion operations in balanced search trees.
- Understand how tree height affects performance.

**🌍 Use case:** Searching in a balanced binary search tree typically takes `O(log n)` time.

**💡 Important:** An unbalanced binary search tree can have height `O(n)`, making search `O(n)`.

---

## 15. 🧠 Quick Complexity Comparison

| Notation | Name | Typical example |
|---|---|---|
| `O(1)` | Constant | List indexing |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Linear search |
| `O(n log n)` | Linearithmic | Efficient comparison sorting |
| `O(n²)` | Quadratic | Nested loops over the same input |
| `O(2ⁿ)` | Exponential | Subset enumeration |
| `O(n!)` | Factorial | Permutation enumeration |

**💡 Interview tip:** Big O, Big Omega, and Big Theta describe asymptotic bounds. They are not automatically equivalent to worst-case, best-case, and average-case analysis, respectively.