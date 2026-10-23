# Python Interview Questions and Answers

## 1. 🏷️ Data Descriptors

**📖 Definition:**

A data descriptor is an object that defines methods such as `__get__()` and `__set__()` or `__delete__()`, with at least one of `__set__()` or `__delete__()` implemented.

Descriptors allow us to control how an object's attributes are accessed, assigned, or deleted.

**🎯 Why it's used:**

- To validate attribute values before assignment.
- To control access to object attributes.
- To reuse attribute-management logic across multiple classes.
- To implement advanced Python features such as properties and framework internals.

**🌍 Real-world use case:**

In an e-commerce application, a product's price should never be negative. A descriptor can validate the price whenever someone assigns a new value.

**💻 Code Example:**

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")

        instance.__dict__[self.name] = value


class Product:
    price = PositiveNumber()


product = Product()

product.price = 100
print(product.price)  # 100

# product.price = -50
# Raises ValueError
```

**💡 Interview Tip:**

A data descriptor takes precedence over an instance attribute of the same name during normal attribute lookup. A non-data descriptor defines `__get__()` without implementing `__set__()` or `__delete__()`. Regular instance methods are common examples of non-data descriptors.

---

## 2. 🔍 Stack Trace (Traceback)

**📖 Definition:**

A stack trace, also called a traceback, shows the sequence of function calls that led to an exception.

It typically contains the file name, line number, function name, and error message.

**🎯 Why it's used:**

- To identify where an error occurred.
- To understand how program execution reached the error.
- To debug complex applications.
- To investigate errors in production systems.

**🌍 Real-world use case:**

Suppose a Django API returns a 500 Internal Server Error when creating a ticket. The traceback helps identify whether the problem occurred in the view, service function, database operation, or another part of the application.

**💻 Code Example:**

```python
import traceback


def divide(a, b):
    return a / b


def calculate():
    return divide(10, 0)


try:
    calculate()
except ZeroDivisionError:
    traceback.print_exc()
```

**💡 Interview Tip:**

Use `logging.exception()` inside an exception handler to record an error message along with traceback information.

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")
```

In production, avoid exposing detailed tracebacks to end users because they may reveal internal implementation details.

---

## 3. ⚙️ Subprocess Module

**📖 Definition:**

The `subprocess` module allows Python programs to execute external programs or operating-system commands.

It can run commands, capture their output, pass input, and check their exit status.

**🎯 Why it's used:**

- To automate command-line operations.
- To execute external applications from Python.
- To run Git, system utilities, or other command-line tools.
- To automate development and deployment workflows.

**🌍 Real-world use case:**

A deployment automation script may run Git commands, execute tests, or invoke a Django management command as part of a deployment process.

**💻 Code Example:**

```python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True,
    check=True
)

print("Output:", result.stdout)
print("Return code:", result.returncode)
```

**Expected output:**

```text
Output: Python 3.x.x
Return code: 0
```

The exact Python version depends on the environment.

**💡 Interview Tip:**

- `subprocess.run()` executes a command and waits for it to finish.
- `capture_output=True` captures standard output and standard error.
- `text=True` returns decoded text instead of bytes.
- `check=True` raises `CalledProcessError` if the command exits with a non-zero status.

Prefer passing commands as a list of arguments. Avoid `shell=True` with untrusted input because it can introduce command-injection vulnerabilities.

---

## 4. 🚨 Custom Exception Class

**📖 Definition:**

A custom exception is an exception class created by a developer to represent a specific application error.

Custom exceptions usually inherit from Python's built-in `Exception` class or another suitable exception class.

**🎯 Why it's used:**

- To represent application-specific errors.
- To distinguish different failure conditions.
- To improve code readability.
- To handle business errors separately from unexpected technical errors.

**🌍 Real-world use case:**

In a banking application, withdrawing more money than the available balance can raise an `InsufficientBalanceError`.

In a Ticket Raising System, attempting to close an already closed ticket could raise a `TicketAlreadyClosedError`.

**💻 Code Example:**

```python
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient account balance"
        )

    return balance - amount


try:
    remaining_balance = withdraw(500, 700)
    print(remaining_balance)

except InsufficientBalanceError as error:
    print("Transaction failed:", error)
```

**Expected output:**

```text
Transaction failed: Insufficient account balance
```

**💡 Interview Tip:**

Custom exceptions make error handling more specific. In Django REST Framework, an exception handler or API layer can translate a custom exception into an appropriate HTTP response.

---

## 5. 🧵 When to Use Multithreading

**📖 Definition:**

Multithreading allows multiple threads to execute within a single process. Threads share the process's memory but have their own execution state and call stacks.

In standard GIL-enabled CPython, the Global Interpreter Lock (GIL) generally prevents multiple threads from executing Python bytecode simultaneously within the same interpreter.

**🎯 Why it's used:**

- To handle multiple I/O-bound tasks concurrently.
- To reduce waiting time during network requests.
- To perform file operations concurrently.
- To keep applications responsive while waiting for external operations.

**🌍 Real-world use case:**

Suppose an application needs to retrieve data from five external APIs. Instead of waiting for each API request to finish sequentially, multiple threads can overlap the waiting time.

**💻 Code Example:**

```python
from concurrent.futures import ThreadPoolExecutor
import time


def fetch_data(item):
    print(f"Fetching item {item}")

    time.sleep(1)  # Simulates network waiting

    return f"Data for item {item}"


items = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(fetch_data, items))

print(results)
```

**💡 Interview Tip:**

- **Multithreading:** Generally useful for I/O-bound tasks such as network requests and file operations.
- **Multiprocessing:** Often useful for CPU-bound tasks because separate processes can execute Python code in parallel.
- **Asyncio:** Useful for managing many concurrent I/O operations when the libraries and application support asynchronous execution.

The GIL's impact depends on the Python implementation and configuration. Free-threaded CPython builds and native extensions that release the GIL can behave differently.

---

## 6. 🌐 Python Variable Scopes

**📖 Definition:**

Scope determines where a variable or name can be accessed in a Python program.

Python generally follows the **LEGB rule** when resolving names:

- **L — Local:** Names defined inside the current function.
- **E — Enclosing:** Names defined in an outer function.
- **G — Global:** Names defined at the module level.
- **B — Built-in:** Names provided by Python, such as `len()` and `print()`.

**🎯 Why it's used:**

- To understand how Python finds variable values.
- To avoid unexpected variable modifications.
- To organize code into functions and modules.
- To understand nested functions and closures.
- To debug errors such as `UnboundLocalError`.

**🌍 Real-world use case:**

A Django service function can use local variables to process an individual request while reading configuration values from module-level settings. Understanding scope helps prevent accidental sharing of request-specific data.

**💻 Code Example:**

```python
company = "ABC Technologies"  # Global


def outer():
    department = "Engineering"  # Enclosing

    def inner():
        employee = "Prithviraj"  # Local

        print(employee)
        print(department)
        print(company)
        print(len("Python"))  # Built-in

    inner()


outer()
```

**Expected output:**

```text
Prithviraj
Engineering
ABC Technologies
6
```

**💡 Interview Tip:**

Use `global` when you need to reassign a module-level variable from inside a function. Use `nonlocal` when a nested function needs to reassign a variable from its enclosing function.

Example:

```python
count = 0


def increment():
    global count
    count += 1


increment()
print(count)  # 1
```

Without `global`, assigning to `count` inside `increment()` would make it a local name, causing an `UnboundLocalError` when Python tries to read it before assignment.

---

## 7. 🖼️ SVG vs PNG

**📖 Definition:**

**SVG (Scalable Vector Graphics):** An XML-based image format that represents graphics using paths, shapes, lines, and other vector instructions.

**PNG (Portable Network Graphics):** A raster image format that stores images as pixels and supports lossless compression and transparency.

**🎯 Why it's used:**

- SVG is useful for graphics that need to scale without pixelation.
- PNG is useful for screenshots and pixel-based images.
- Choosing the correct format can improve image quality and performance.
- Both formats support transparency.

**🌍 Real-world use case:**

In a React portfolio:

- Use SVG for logos, icons, and simple diagrams.
- Use PNG for screenshots of your project dashboard or other pixel-based visuals.

**💻 Code Example:**

```html
<!-- SVG logo -->
<img src="/images/logo.svg" alt="Company logo">

<!-- PNG screenshot -->
<img src="/images/dashboard.png" alt="Dashboard screenshot">
```

**💡 Interview Tip:**

| Feature | SVG | PNG |
|---|---|---|
| Image type | Vector | Raster |
| Scaling | Usually remains sharp | Can become pixelated |
| Best suited for | Logos, icons, diagrams | Screenshots, pixel images |
| Transparency | Supported | Supported |
| Editing | Vector editing | Pixel editing |
| File size | Depends on graphic complexity | Depends on image dimensions and content |

SVG is not always smaller than PNG. Its size depends on the complexity of the graphic.

---

## 8. 🔢 Maximum Integer Value in Python

**📖 Definition:**

Python's built-in `int` type supports arbitrary-precision integers. This means integers are not restricted to a fixed 32-bit or 64-bit maximum.

The practical limit depends on available memory and implementation constraints.

**🎯 Why it's used:**

- To perform calculations with very large numbers.
- To understand Python's integer behavior.
- To avoid incorrect assumptions about integer overflow.
- To distinguish Python integers from fixed-width integer types.

**🌍 Real-world use case:**

Python can handle extremely large integer calculations in mathematical algorithms without overflowing at the usual 32-bit or 64-bit boundaries.

**💻 Code Example:**

```python
number = 10 ** 100

print(number)
print(len(str(number)))
```

**Expected output:**

```text
A very large integer
101
```

The integer contains 101 decimal digits.

**💡 Interview Tip:**

Python's built-in `int` has no fixed maximum value such as `2**31 - 1`.

However, very large integers require more memory and processing time.

For comparison:

```python
# Maximum signed 32-bit integer
print(2**31 - 1)   # 2147483647

# Maximum signed 64-bit integer
print(2**63 - 1)   # 9223372036854775807
```

These are limits of conventional fixed-width integer representations, not limits of Python's built-in `int`.

---

## 9. 📦 Memory Allocation of a Python List

**📖 Definition:**

A Python list is a mutable, ordered collection of object references.

In CPython, a list typically uses a dynamically allocated array of references. It may reserve extra capacity so that appending elements does not require reallocating the array every time.

The actual elements are separate objects when they are ordinary separately allocated Python objects.

**🎯 Why it's used:**

- To understand how lists use memory.
- To understand list resizing and performance.
- To choose appropriate data structures.
- To distinguish a list of references from a packed numerical array.

**🌍 Real-world use case:**

In a Django application, a service might collect ticket objects in a list before processing them. The list stores references to the objects rather than embedding each complete object inside the list's storage array.

**💻 Code Example:**

```python
import sys

numbers = []

print("Empty list:", sys.getsizeof(numbers))

numbers.append(10)
print("After one item:", sys.getsizeof(numbers))

numbers.extend([20, 30, 40])
print("After more items:", sys.getsizeof(numbers))
```

**💡 Interview Tip:**

`sys.getsizeof()` reports the shallow size of the list object, including its allocated reference storage in CPython. It does not include the full memory used by the objects referenced by the list.

List allocation sizes can vary across Python versions and implementations.

Common time complexities:

- Indexing: O(1).
- Appending: amortized O(1).
- Searching: O(n).
- Inserting at the beginning: O(n).
- Removing an item from the middle: generally O(n).

For large numerical datasets, an `array.array` or a NumPy array may use less memory than a list of Python number objects.

---
## 10. 🔙 Backtracking

📖 Definition:

Backtracking is an algorithmic technique that solves problems by building a solution step by step. If a choice leads to an invalid solution, the algorithm goes back, undoes that choice, and tries another option.

It commonly uses recursion to explore possible solutions.

🎯 Why it's used:

Explores different possible solutions systematically.

Rejects invalid paths early.

Solves problems involving combinations, permutations, and constraints.

Avoids continuing down a path that cannot produce a valid solution.

🌍 Real-world use case:

Solving Sudoku puzzles.

Finding paths through a maze.

Generating all possible combinations.

Solving the N-Queens problem.

Checking possible arrangements in puzzles.

## 11. 🪆 Maximum Depth of a Nested List

**📖 Definition:**

A nested list is a list that contains other lists as elements.

Python does not define one universal maximum nesting depth for lists. The practical limit depends on memory, implementation constraints, and the operation being performed.

Recursive functions that process deeply nested lists can encounter Python's recursion limit.

**🎯 Why it's used:**

- To process hierarchical data.
- To understand recursive algorithms.
- To prevent recursion errors.
- To handle deeply nested JSON and tree structures.
- To validate data received from external systems.

**🌍 Real-world use case:**

An API might return categories containing subcategories, which contain further subcategories. A recursive function can calculate the nesting depth to validate or analyze the data structure.

**💻 Code Example:**

```python
nested = [1, [2, [3, [4]]]]


def get_max_depth(value):
    if not isinstance(value, list):
        return 0

    if not value:
        return 1

    return 1 + max(
        get_max_depth(item)
        for item in value
    )


print(get_max_depth(nested))  # 4
```

**💡 Interview Tip:**

In this example:

- A scalar value has depth 0.
- A list containing scalar values has depth 1.
- Every additional nested list adds one level.

You can inspect the interpreter's recursion limit using:

```python
import sys

print(sys.getrecursionlimit())
```

This limit applies to recursive interpreter execution, not to the creation of nested lists themselves.

For very deeply nested data, consider iterative traversal using an explicit stack instead of recursion.

---
```

**💡 Interview Tip:**

The example implements a basic singleton metaclass that returns the same instance for each class.

Because the instance is created only once, the second call does not run `__init__()` again. This example also demonstrates why singleton implementations require careful design: the second initialization argument is ignored.

Metaclasses are powerful but advanced. For ordinary validation and attribute control, functions, decorators, or descriptors are often simpler choices.

---

