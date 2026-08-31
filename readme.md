# 🐍 Python Core Concepts — Cheat Sheet

A quick-reference guide to important-but-often-confusing Python concepts.
Each topic follows the same structure:

> **📖 Definition → 🎯 Why It's Used → 🌍 Real-World Use Case → 💻 Code Example**

---

## 📑 Table of Contents

| # | Concept |
|---|---------|
| 1 | [Monkey Patching](#1-🐒-monkey-patching) |
| 2 | [Decorators](#2-🎁-decorators) |
| 3 | [Generators](#3-⚙️-generators) |
| 4 | [Shallow Copy](#4-📄-shallow-copy) |
| 5 | [Deep Copy](#5-📚-deep-copy) |
| 6 | [Closures](#6-🔒-closures) |
| 7 | [Currying](#7-🍛-currying) |
| 8 | [Assert](#8-✅-assert) |
| 9 | [`*args` and `**kwargs`](#9-📦-args-and-kwargs) |
| 10 | [Context Managers](#10-🚪-context-managers) |
| 11 | [Iterators vs Iterables](#11-🔁-iterators-vs-iterables) |
| 12 | [Lambda Functions](#12-λ-lambda-functions) |
| 13 | [`@property` Decorator](#13-🏷️-property-decorator) |
| 14 | [Memoization / `lru_cache`](#14-🧠-memoization--lru_cache) |
| 15 | [Duck Typing](#15-🦆-duck-typing) |
| 16 | [Metaclasses](#16-🏗️-metaclasses) |

---

## 1. 🐒 Monkey Patching

**📖 Definition:**
Monkey patching means dynamically modifying or extending a class or module **at runtime**, without touching its original source code.

**🎯 Why it's used:**
- Fix a bug in a third-party library without waiting for a patch
- Add missing functionality quickly
- Mock objects/functions during testing

**🌍 Real-world use case:**
In unit testing, you might monkey patch a `requests.get()` call so your tests don't actually hit a live API — this is exactly what libraries like `unittest.mock` do internally.

**💻 Code Example:**
```python
class Dog:
    def bark(self):
        return "Woof!"

def new_bark(self):
    return "Woof Woof!! (patched)"

# Monkey patch the method at runtime
Dog.bark = new_bark

d = Dog()
print(d.bark())  # Output: Woof Woof!! (patched)
```

> ⚠️ **Caution:** Overuse makes code unpredictable and hard to debug — use sparingly, mainly in tests.

---

## 2. 🎁 Decorators

**📖 Definition:**
A decorator is a function that **wraps another function/class** to extend or modify its behavior without changing its actual code.

**🎯 Why it's used:**
- Add reusable logic (logging, timing, auth checks) cleanly
- Follows the **DRY** (Don't Repeat Yourself) principle
- Keeps core business logic separate from cross-cutting concerns

**🌍 Real-world use case:**
Web frameworks like **Flask/Django** use decorators for routing (`@app.route('/home')`) and access control (`@login_required`).

**💻 Code Example:**
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
# Output: slow_function took 1.0001s
```

---

## 3. ⚙️ Generators

**📖 Definition:**
A generator is a special function that **yields** values one at a time using `yield`, pausing its state between calls instead of returning everything at once.

**🎯 Why it's used:**
- Memory-efficient — doesn't load entire data into memory
- Enables lazy evaluation (compute values only when needed)
- Great for streaming or infinite sequences

**🌍 Real-world use case:**
Reading huge log files or datasets (e.g., a 10 GB CSV) line-by-line without loading the whole file into RAM.

**💻 Code Example:**
```python
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Only one line is in memory at a time
for line in read_large_file("huge_log.txt"):
    print(line)
```

---

## 4. 📄 Shallow Copy

**📖 Definition:**
A shallow copy creates a **new outer object**, but nested objects inside it are still **references** to the same objects as the original.

**🎯 Why it's used:**
- Faster and cheaper than a deep copy
- Useful when nested objects are immutable or shared intentionally

**🌍 Real-world use case:**
Duplicating a configuration dictionary where top-level keys need independent copies, but shared sub-objects (like a logger instance) should remain the same reference.

**💻 Code Example:**
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)

shallow[0][0] = 99  # modifies nested list

print(original)  # [[99, 2, 3], [4, 5, 6]]  <- original affected too!
print(shallow)   # [[99, 2, 3], [4, 5, 6]]
```

---

## 5. 📚 Deep Copy

**📖 Definition:**
A deep copy creates a **completely independent clone** of an object, including all nested objects — no shared references at any level.

**🎯 Why it's used:**
- Prevents accidental mutation of the original object
- Essential when working with complex nested structures (JSON, trees, graphs)

**🌍 Real-world use case:**
In game development, cloning a complex game-state object (player stats, inventory, map data) to create a "save point" that won't be affected by future in-game changes.

**💻 Code Example:**
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print(original)  # [[1, 2, 3], [4, 5, 6]]   <- unaffected
print(deep)      # [[99, 2, 3], [4, 5, 6]]
```

### 🔍 Shallow vs Deep Copy — Quick Comparison

| Aspect | Shallow Copy | Deep Copy |
|--------|-------------|-----------|
| Nested objects | Shared references | Fully independent |
| Speed | Faster | Slower |
| Memory usage | Lower | Higher |
| Function | `copy.copy()` | `copy.deepcopy()` |
| Risk | Original may get mutated | Fully safe/isolated |

---

## 6. 🔒 Closures

**📖 Definition:**
A closure is a function that **remembers variables from its enclosing scope**, even after that outer function has finished executing.

**🎯 Why it's used:**
- Data hiding / encapsulation without classes
- Maintain state between function calls
- Basis for decorators and factory functions

**🌍 Real-world use case:**
Creating configurable multiplier/discount functions in an e-commerce pricing engine (e.g., `apply_10_percent_discount`, `apply_20_percent_discount`) generated dynamically.

**💻 Code Example:**
```python
def make_multiplier(factor):
    def multiplier(number):
        return number * factor  # 'factor' remembered via closure
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

---

## 7. 🍛 Currying

**📖 Definition:**
Currying transforms a function that takes **multiple arguments** into a sequence of functions that each take **a single argument**.

**🎯 Why it's used:**
- Enables partial application of functions
- Improves reusability and function composition
- Common in functional programming pipelines

**🌍 Real-world use case:**
Building reusable validation functions, e.g., `is_valid_length(min_len)(max_len)(string)` for form validation pipelines.

**💻 Code Example:**
```python
def curried_add(a):
    def inner1(b):
        def inner2(c):
            return a + b + c
        return inner2
    return inner1

print(curried_add(1)(2)(3))  # 6

# Using functools.partial for a similar effect
from functools import partial

def add(a, b, c):
    return a + b + c

add_5 = partial(add, 5)
print(add_5(2, 3))  # 10
```

---

## 8. ✅ Assert

**📖 Definition:**
`assert` is a debugging aid that tests if a condition is `True`. If it's `False`, it raises an `AssertionError`, optionally with a message.

**🎯 Why it's used:**
- Sanity-checks / catches bugs early during development
- Documents assumptions directly in code
- ⚠️ Not meant for production input validation (can be disabled with `python -O`)

**🌍 Real-world use case:**
Used heavily in **unit tests** (`assert result == expected`) and to verify internal invariants, like ensuring a list isn't empty before processing.

**💻 Code Example:**
```python
def divide(a, b):
    assert b != 0, "Denominator cannot be zero!"
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # AssertionError: Denominator cannot be zero!
```

---

## 9. 📦 `*args` and `**kwargs`

**📖 Definition:**
`*args` collects extra **positional** arguments into a tuple; `**kwargs` collects extra **keyword** arguments into a dictionary.

**🎯 Why it's used:**
- Write flexible functions that accept a variable number of arguments
- Useful for wrapper/decorator functions that forward arguments
- Common in APIs and framework design

**🌍 Real-world use case:**
Django/Flask view functions and decorators use `*args, **kwargs` to forward arbitrary parameters through middleware layers.

**💻 Code Example:**
```python
def describe_pet(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Extra info: {args}")
    print(f"Attributes: {kwargs}")

describe_pet("Rex", "loyal", "playful", breed="Labrador", age=3)
# Name: Rex
# Extra info: ('loyal', 'playful')
# Attributes: {'breed': 'Labrador', 'age': 3}
```

---

## 10. 🚪 Context Managers

**📖 Definition:**
A context manager handles **setup and cleanup** of resources automatically using the `with` statement, via `__enter__` and `__exit__` methods.

**🎯 Why it's used:**
- Guarantees resources (files, DB connections, locks) are released properly
- Cleaner than manual try/finally blocks
- Prevents resource leaks

**🌍 Real-world use case:**
Managing database connections/transactions — automatically committing or rolling back even if an exception occurs mid-transaction.

**💻 Code Example:**
```python
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

with open_file("data.txt", "w") as file:
    file.write("Hello, World!")
# File is automatically closed here
```

---

## 11. 🔁 Iterators vs Iterables

**📖 Definition:**
An **iterable** is any object you can loop over (`__iter__`); an **iterator** is the object that actually produces values one at a time (`__next__`).

**🎯 Why it's used:**
- Powers Python's `for` loops under the hood
- Enables custom, memory-efficient looping behavior
- Foundation for generators

**🌍 Real-world use case:**
Building a custom pagination iterator that fetches the next "page" of API results only when requested.

**💻 Code Example:**
```python
class CountUpTo:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        raise StopIteration

for num in CountUpTo(5):
    print(num)  # 1 2 3 4 5
```

---

## 12. λ Lambda Functions

**📖 Definition:**
A lambda is a small, anonymous, single-expression function defined using the `lambda` keyword — no `def` or name required.

**🎯 Why it's used:**
- Quick, throwaway functions for short operations
- Commonly passed as arguments to `map()`, `filter()`, `sorted()`

**🌍 Real-world use case:**
Sorting a list of dictionaries (e.g., employee records) by a specific key without writing a full function.

**💻 Code Example:**
```python
employees = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]

sorted_by_age = sorted(employees, key=lambda emp: emp["age"])
print(sorted_by_age)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
```

---

## 13. 🏷️ `@property` Decorator

**📖 Definition:**
`@property` lets you define a method that can be **accessed like an attribute**, allowing controlled getting/setting of internal state.

**🎯 Why it's used:**
- Add validation logic without changing the public interface
- Keep attribute access syntax clean (`obj.value` instead of `obj.get_value()`)
- Supports encapsulation

**🌍 Real-world use case:**
A `BankAccount` class exposing a `balance` property that prevents direct assignment of negative values.

**💻 Code Example:**
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

account = BankAccount(100)
account.balance = 50   # works fine
# account.balance = -10  # raises ValueError
```

---

## 14. 🧠 Memoization / `lru_cache`

**📖 Definition:**
Memoization caches the results of expensive function calls, returning the cached result when the same inputs occur again.

**🎯 Why it's used:**
- Massive performance boost for repeated/recursive computations
- Avoids redundant expensive operations (API calls, heavy math)

**🌍 Real-world use case:**
Caching results of expensive recursive algorithms like Fibonacci, or caching API responses that don't change often.

**💻 Code Example:**
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Instant, thanks to caching
```

---

## 15. 🦆 Duck Typing

**📖 Definition:**
"If it walks like a duck and quacks like a duck, it's a duck." Python cares about an object's **behavior/methods**, not its explicit type.

**🎯 Why it's used:**
- Enables flexible, polymorphic code without inheritance hierarchies
- Core to Python's dynamic typing philosophy

**🌍 Real-world use case:**
Any object with a `.read()` method can be used where a "file-like object" is expected (e.g., `io.StringIO`, network sockets, actual files).

**💻 Code Example:**
```python
class Duck:
    def sound(self):
        return "Quack!"

class Person:
    def sound(self):
        return "I'm imitating a duck!"

def make_it_quack(thing):
    print(thing.sound())  # doesn't check type, just calls the method

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I'm imitating a duck!
```

---

## 16. 🏗️ Metaclasses

**📖 Definition:**
A metaclass is the **"class of a class"** — it defines how classes themselves behave and are constructed. `type` is Python's default metaclass.

**🎯 Why it's used:**
- Control/customize class creation (enforce naming rules, auto-register classes)
- Powers ORMs and frameworks (e.g., Django models, ABCs)

**🌍 Real-world use case:**
Django's ORM uses metaclasses to automatically convert model class attributes into database table fields.

**💻 Code Example:**
```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True -- same instance, always
```

---

## 📌 Quick Reference Summary

| Icon | Concept | One-Line Purpose |
|------|---------|-------------------|
| 🐒 | Monkey Patching | Modify code at runtime without editing source |
| 🎁 | Decorator | Wrap functions to add extra behavior |
| ⚙️ | Generator | Lazily yield values, saving memory |
| 📄 | Shallow Copy | Copy top-level only, share nested refs |
| 📚 | Deep Copy | Fully independent clone of nested data |
| 🔒 | Closure | Function that remembers outer scope |
| 🍛 | Currying | Break multi-arg function into single-arg chain |
| ✅ | Assert | Debug-time sanity check |
| 📦 | `*args`/`**kwargs` | Accept variable-length arguments |
| 🚪 | Context Manager | Auto resource setup/cleanup via `with` |
| 🔁 | Iterator/Iterable | Custom, memory-safe looping |
| λ | Lambda | Anonymous one-line function |
| 🏷️ | `@property` | Attribute-style access with logic |
| 🧠 | Memoization | Cache results for speed |
| 🦆 | Duck Typing | Behavior over explicit type |
| 🏗️ | Metaclass | Customize how classes are built |

---

### 🤝 Contributing
Feel free to fork this README, add more concepts (e.g., `async/await`, descriptors, GIL, `__slots__`, MRO), and submit a PR!

### 📄 License
Free to use and modify for learning purposes.