# Week 9: Modules and Unit Testing in Python

## Modules in Python

### What Are Modules?

- **Definition:** A module is a way to organize Python code into separate files.
- **Purpose:**
  - Makes code reusable and easier to manage.
  - Facilitates collaboration by reducing conflicts in a shared repository.
  - Improves code structure and readability.

---

### Benefits of Modules

1. **Better Organization:**
   - Splitting a program into multiple files makes it manageable.
   - Allows logical grouping of related functions and classes.
2. **Facilitates Collaboration:**
   - Reduces merge conflicts in repositories by splitting code across multiple files.
3. **Reusability:**
   - Functions and classes in one module can be reused in others via imports.

---

### Module Types in Python

1. **Single File Module:** A `.py` file containing Python code.
2. **Directory Module:**
   - A directory containing multiple `.py` files.
   - Must include a special file named `__init__.py` to be recognized as a module.

---

### Example: Single File Module

File: `my_code.py`

```python
def greet(name): 
    return f"Hello, {name}!"
```

Another File: `modules.py`

```python
import my_code

result = my_code.greet("Alice") 
print(result) # Output: Hello, Alice!
```

Key Points:
- Use `snake_case` for module filenames.
- Avoid naming modules the same as variables or types to prevent confusion.

---

### Example: Directory Module

Directory Structure:

`./my_module/functions.py` - see below
`./my_module/more_functions.py` - see below
`./my_module/__init__.py` - required for directory to be a module. Contains code that you want ran when the module is imported (can be completely empty)
`./my_module/__main__.py` - if module is executed `python -m "name of module"` it will run what is in the `__main__.py` file.
`./run.py` - runs some of the content of `my_module`


Contents of `functions.py`:

```python
def fun1():
    """
    A function to print some text.
    """
    print("fun1")
```

Content of `more_functions.py`

```python
def fun2():
    """
    A function to print some text.
    """
    print("fun2")
```

Usage in `main.py`:

```python
from mymodule import functions

print(functions.fun1()) # Output: Function 1
```

Contents of `run.py`:

```python
from my_module import functions
from my_module import more_functions
import my_module #(will run the __init__.py file)


"""
A program to demonstrate using Python code from a 
module that comprises more than one file.
"""
functions.fun1()  # From my_module/functions.py
more_functions.fun2()  # From my_module/more_functions.py
my_module.fun3()  # From my_module/__init__.py
```

---

### Special Syntax: `if __name__ == "__main__"`

- **Purpose:** Prevents code execution when a file is imported as a module.
- **Example:**
    ```python
    if __name__ == "__main__": 
        print("This code runs only when executed directly.")
    ```

- Code outside the `if` block runs on both import (`import main`) and direct execution (`python main.py`).
- Ensures cleaner module design.

---

## Unit Testing in Python

### What Are Unit Tests?

- **Definition:** Tests that verify the behavior of individual units of code (e.g., functions or classes).
- **Purpose:**
- Ensure code works as expected.
- Catch bugs early in development.
- Prevent regressions when making changes.

---

### Benefits of Unit Testing

1. **Maintainability:** Helps identify and fix issues early.
2. **Collaboration:** Multiple developers can work on the same codebase with confidence.
3. **Automation:** Unit tests can run automatically in repositories.

---

### Writing Unit Tests in Python

- Use the `unittest` module.
- **Test Structure:**
- Create a separate file for tests (e.g., `test_example.py`).
- Define a test class that inherits from `unittest.TestCase`.
- Test methods should start with `test_`.

---

### Example: Testing a Simple Function

Module: `example.py`

```python
def double(x): 
    return x * 2
```  

Test File: `test_example.py`

```python
import unittest 
import example

class TestExample(unittest.TestCase): 
    def test_double(self): 
        self.assertEqual(example.double(2), 4) 
        self.assertEqual(example.double(-3), -6)

if __name__ == "__main__":
    unittest.main()
```

Run the tests:

`python -m unittest test_example.py`

---

### Handling Exceptions in Tests

Use `assertRaises` to test for exceptions.

Example

Module: `my_module.py`

```python
def swap(values):
    """
    A function to swap the first and last
    element in a list.
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list.")
    tmp = values[0]
    values[0] = values[-1]
    values[-1] = tmp


"""
A program to demonstrate the swap function.
"""
if __name__ == "__main__":
    numbers = [1, 2]
    swap(numbers)
    print(numbers)
```
Test File: `test_my_module.py`

```python
import my_module
import unittest


class TestMyModule(unittest.TestCase):
    def test_swap(self):
        """
        A function to test the swap function.
        """

        # Normal use.
        numbers = [1, 2]
        my_module.swap(numbers)
        self.assertEqual(numbers, [2, 1])

        # With no elements.
        self.assertRaises(IndexError, my_module.swap, []) # Checks that an IndexError is raised when my_module.swap([]) is evaluated

        # With an int, rather than a list.
        self.assertRaises(TypeError, my_module.swap, 1) # Checks that an TypeError is raised when my_module.swap(1) is evaluated


if __name__ == "__main__":
    unittest.main()

```


Another Example:

```python
def divide(a, b): 
    if b == 0: 
        raise ValueError("Cannot divide by zero.") 
    return a / b

class TestDivide(unittest.TestCase): 
    def test_zero_division(self): 
        with self.assertRaises(ValueError): 
            divide(1, 0)
```

---

### Best Practices for Unit Tests

1. **Keep Tests Simple:**
   - Use small, understandable inputs.
2. **Name Tests Clearly:**
   - Use descriptive names like `test_function_normal` or `test_function_error`.
3. **Separate Tests from Code:**
   - Store tests in a different file or directory.

---

## Summary

- **Modules:** Enable better code organization and reusability.
- **Unit Tests:** Verify code correctness and prevent bugs.
- **Tips:**
  - Use `if __name__ == "__main__"` to manage execution flow in modules.
  - Keep unit tests focused and concise.
  - Test both normal behavior and expected failures.

---

Let me know if any additional formatting is required or if you'd like more examples!```
