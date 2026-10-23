## 1. 🧠 Virtual Memory

**📖 Definition:**

Virtual memory is a memory-management technique that gives each process its own virtual address space and maps it to physical memory.

**🎯 Why it's used:**

- To manage memory efficiently.
- To isolate processes from each other.
- To run applications when RAM is under pressure.

**🌍 Real-world use case:**

Running multiple applications when their combined memory requirements exceed available RAM.

**💻 Example:**

```text
Virtual Memory → Memory Management → RAM + Disk Storage
```

---

## 2. 📈 Time Complexity Notations (Big O, Ω, Θ)

**📖 Definition:**

- **Big O (O):** Asymptotic upper bound.
- **Big Omega (Ω):** Asymptotic lower bound.
- **Big Theta (Θ):** Asymptotically tight bound.

**🎯 Why it's used:**

- To analyze algorithm efficiency.
- To compare algorithms as input size increases.
- To understand best-case and worst-case performance.

**🌍 Real-world use case:**

Choosing an efficient search algorithm when processing millions of records.

**💻 Example:**

```python
# Linear search
def search(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False

# Best case: Θ(1)
# Worst case: Θ(n)
# Worst-case upper bound: O(n)
```

---

## 3. ⏱️ Time and Space Complexity Calculations

**📖 Definition:**

Time complexity measures how an algorithm's work grows with input size. Space complexity measures how its memory usage grows.

**🎯 Why it's used:**

- To improve program performance.
- To reduce memory consumption.
- To choose scalable algorithms.

**🌍 Real-world use case:**

Processing a large list of customer records without unnecessary loops or memory usage.

**💻 Example:**

```python
def print_numbers(numbers):
    for number in numbers:
        print(number)

# Time complexity: O(n)
# Auxiliary space complexity: O(1)
```

---

## 4. 🧩 Types of Memory Allocation (Static and Dynamic)

**📖 Definition:**

- **Static allocation:** Storage has a predetermined size or lifetime, depending on the language.
- **Dynamic allocation:** Memory is obtained as needed during program execution.

**🎯 Why it's used:**

- Static allocation provides predictable storage.
- Dynamic allocation supports changing data requirements.

**🌍 Real-world use case:**

A fixed-size embedded-system buffer versus a dynamically growing collection of user records.

**💻 Example:**

```python
# Dynamic collection
numbers = []
numbers.append(10)
numbers.append(20)

# Fixed-size buffer
buffer = bytearray(128)
```

---

## 5. ✅ Advantages of Static Memory Allocation

**📖 Definition:**

Static memory allocation reserves storage with a predetermined size or lifetime.

**🎯 Why it's used:**

- Predictable memory requirements.
- Potentially lower allocation overhead.
- Useful for fixed-size data structures.
- Suitable for memory-constrained systems.

**🌍 Real-world use case:**

An embedded controller reserves a fixed-size buffer for sensor readings to keep memory usage predictable.

**💻 Example:**

```python
# Create a buffer with 128 bytes
buffer = bytearray(128)

print(len(buffer))  # 128
```

---

## 6. 🕳️ Memory Leak

**📖 Definition:**

A memory leak occurs when memory that is no longer needed remains allocated or referenced, preventing it from being reclaimed.

**🎯 Why it's important:**

- To prevent increasing memory consumption.
- To maintain application performance.
- To avoid crashes in long-running applications.

**🌍 Real-world use case:**

A backend server continuously stores completed requests in a global list and never removes them.

**💻 Example:**

```python
completed_requests = []

def process_request(request):
    # Problem: references keep accumulating
    completed_requests.append(request)

# Fix: remove processed entries when no longer needed,
# or use a bounded collection.
```

---

## 7. 🔤 Control Characters and Character Encoding (ASCII, UTF-8)

**📖 Definition:**

Control characters represent actions or formatting, such as newlines. Character encoding maps characters to numeric representations in bytes.

- **ASCII:** Represents 128 code points.
- **UTF-8:** A variable-length Unicode encoding supporting a vast range of characters.

**🎯 Why it's used:**

- To store and transmit text correctly.
- To support multiple languages.
- To avoid encoding and decoding errors.

**🌍 Real-world use case:**

A website uses UTF-8 to display English, Malayalam, and other languages correctly.

**💻 Example:**

```python
text = "Hello\nWorld"
print(text)

print(ord("A"))              # 65
print("Hello".encode("utf-8"))
```

---

## 8. 💾 Kilobyte vs Kibibyte (Memory Units)

**📖 Definition:**

- **Kilobyte (KB):** 1,000 bytes.
- **Kibibyte (KiB):** 1,024 bytes.

**🎯 Why it's used:**

- To understand storage and memory measurements.
- To distinguish decimal and binary units.

**🌍 Real-world use case:**

Comparing storage advertised by manufacturers with memory values reported by system utilities.

**💻 Example:**

```text
1 KB  = 1,000 bytes
1 KiB = 1,024 bytes
1 MiB = 1,024 KiB
```

---

## 9. 🧱 Jagged, Heterogeneous and Homogeneous Arrays

**📖 Definition:**

- **Jagged array:** A collection of rows or subarrays with different lengths.
- **Heterogeneous collection:** Contains elements of different types.
- **Homogeneous array:** Contains elements of the same data type.

**🎯 Why it's used:**

- Jagged structures represent irregular data.
- Heterogeneous collections store different kinds of information.
- Homogeneous arrays store consistent data efficiently.

**🌍 Real-world use case:**

Student groups may contain different numbers of students, while a numerical array may store only measurement values.

**💻 Example:**

```python
# Jagged structure
groups = [[1, 2], [3, 4, 5], [6]]

# Heterogeneous list
employee = ["Prithviraj", 25, True]

# Homogeneous integer array
from array import array
numbers = array("i", [10, 20, 30])
```

---

## 10. 🚦 Priority Queue

**📖 Definition:**

A priority queue is a data structure in which elements are removed according to priority rather than insertion order.

**🎯 Why it's used:**

- To process urgent tasks first.
- To schedule tasks efficiently.
- To support algorithms that select the next lowest-cost item.

**🌍 Real-world use case:**

Hospital triage systems prioritize patients according to urgency. Scheduling software can similarly prioritize tasks.

**💻 Example:**

```python
import heapq

tasks = []

heapq.heappush(tasks, (2, "Normal task"))
heapq.heappush(tasks, (1, "Urgent task"))

print(heapq.heappop(tasks))
# (1, 'Urgent task')
```

---

## 11. ⚖️ Load Factor in Hashing

**📖 Definition:**

Load factor is the ratio of the number of stored entries to the number of buckets in a hash table.

**🎯 Why it's used:**

- To monitor hash-table occupancy.
- To understand collision behavior.
- To help determine when resizing is needed.

**🌍 Real-world use case:**

A hash table may increase its capacity when too many entries are stored, helping maintain efficient lookups.

**💻 Example:**

```python
entries = 75
buckets = 100

load_factor = entries / buckets

print(load_factor)  # 0.75
```

---

## 12. 🫧 Why Is Bubble Sort Stable?

**📖 Definition:**

Bubble sort is stable when equal elements retain their original relative order. This happens when adjacent elements are swapped only if the left element is strictly greater than the right element.

**🎯 Why it's used:**

- To preserve the order of records with equal sorting keys.
- To maintain previous sorting order when sorting by another field.

**🌍 Real-world use case:**

Sorting employees by salary while preserving their previous order among employees with equal salaries.

**💻 Example:**

```python
if numbers[j] > numbers[j + 1]:
    numbers[j], numbers[j + 1] = (
        numbers[j + 1], numbers[j]
    )

# Using > instead of >= preserves equal elements' order.
```

---

## 13. 🔄 Applications of Circular Queue

**📖 Definition:**

A circular queue is a FIFO (First In, First Out) data structure in which the last position connects back to the first position.

**🎯 Why it's used:**

- To reuse empty positions in a fixed-size buffer.
- To avoid shifting elements after removal.
- To manage continuous streams of data.

**🌍 Real-world use case:**

Circular queues are used in keyboard buffers, streaming systems, and producer-consumer workflows.

**💻 Example:**

```python
capacity = 5
current_index = 4

next_index = (current_index + 1) % capacity

print(next_index)  # 0
```

---

## 14. 🔁 Drawbacks of Recursion

**📖 Definition:**

Recursion occurs when a function calls itself to solve smaller versions of a problem.

**🎯 Why it's important:**

- Recursive calls consume call-stack space.
- Deep recursion can cause `RecursionError`.
- Repeated calculations can make some recursive algorithms inefficient.

**🌍 Real-world use case:**

Recursively processing deeply nested JSON data may exceed Python's recursion limit.

**💻 Example:**

```python
# Iterative factorial avoids recursive calls
def factorial(n):
    result = 1

    for number in range(2, n + 1):
        result *= number

    return result

print(factorial(5))  # 120
```

---

## 15. 📚 When to Use a Stack Over an Array

**📖 Definition:**

A stack is a LIFO (Last In, First Out) data structure. An array provides indexed access to elements.

**🎯 Why it's used:**

- Use a stack when the newest item must be processed first.
- Use an array when indexed access is important.
- A stack provides a clear push/pop interface for LIFO operations.

**🌍 Real-world use case:**

Stacks are used for undo operations, browser navigation history, function calls, and depth-first search.

**💻 Example:**

```python
stack = []

stack.append("First")
stack.append("Second")

print(stack.pop())  # Second
print(stack.pop())  # First
```

**💡 Interview Tip:**

Python lists can implement stacks efficiently using `append()` and `pop()` at the end. A stack is an abstract data structure, not necessarily a separate built-in Python type.