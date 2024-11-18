# More Functions

This lecture explores additional concepts in Python functions, with a focus on function behavior, ```return``` versus ```print```, variable scope, and recursion.

## Functions and ```Return``` vs ```Print```
In Python, functions may either return values to be used in other parts of the program or simply print results to the screen. Understanding the difference between return and print is essential for effective function design.

### Example: return vs print
```python
def return_number():
    return 10

def print_number():
    print(10)
```
* ```return_number()``` returns the value 10 to the calling context, so this value can be stored or manipulated further.
* ```print_number()``` outputs 10 to the console but does not return it. If assigned to a variable, it would return ```None```.

### Key Points
* ```return``` sends data back to the caller and allows further manipulation.
* ```print``` only outputs data to the console without storing it.

Using the Python interactive interpreter can sometimes cause confusion, as it displays values without requiring print when no assignment is made. This behavior is unique to the interpreter and does not reflect how return and print work in scripts.

## Functions with Simple Return Values
Returning values is common in functions that perform calculations. Here, we calculate areas using functions that take parameters and return the result.

### Example: Area Calculations

```python
import math

def area_circle(radius):
    """Calculates the area of a circle given the radius."""
    return math.pi * radius ** 2

def area_square(side_length):
    """Calculates the area of a square given the side length."""
    return side_length ** 2
```

* **Purpose:** Breaking down calculations into functions simplifies code reuse and improves readability.
* **Return Values:** These functions return calculated areas without modifying global state.

## Functions with Mutable Arguments
Passing mutable arguments, like lists or dictionaries, allows the function to modify the original data structure, enabling flexible data management but requiring caution to avoid unintentional changes.

### Example: Counting Elements in a List
```python
def count_names(input_list, counts):
    """Counts occurrences of unique words in input_list and stores in counts dictionary."""
    counts.clear()  # Clear existing data for consistent results
    for word in input_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
```
* **Explanation:** count_names receives a list and an empty dictionary. The dictionary counts is filled with word frequencies, and changes persist outside the function since dictionaries are mutable.
* **Design Choice:** Clearing counts at the start ensures the function's output is consistent for each call, regardless of prior state.

### Example: Cumulative Total with Mutable List
```python
def cumulative_total(input_list, output_list):
    """Calculates cumulative totals and stores results in output_list."""
    output_list.clear()  # Clear for consistent results
    cumulative_sum = 0
    for num in input_list:
        cumulative_sum += num
        output_list.append(cumulative_sum)
```

* **Explanation:** This function calculates cumulative totals, appending each total to output_list. The mutable output_list allows results to be stored without returning a value.
* **Practical Use:** Useful in scenarios where the cumulative result needs to be progressively calculated and stored.

## Functions with Optional Parameters
Python functions can use optional parameters, allowing flexibility in input requirements. This feature is useful in functions that compute missing values.

### Example: Calculating Triangle Side Using Pythagoras
```python
import math

def triangle_side(a=None, b=None, h=None):
    """Calculates the missing side of a right triangle."""
    if a is not None and b is not None and h is None:
        return math.sqrt(a**2 + b**2)
    elif a is not None and h is not None and b is None:
        return math.sqrt(h**2 - a**2)
    elif b is not None and h is not None and a is None:
        return math.sqrt(h**2 - b**2)
    else:
        return None  # Invalid input combination
```

* **Explanation:** This function uses optional parameters to identify which side of a right triangle to calculate.
* **Error Handling:** It returns ```None`` if invalid input combinations are provided, preventing calculation errors.

## Recursion
Recursion is a technique where a function calls itself to solve smaller instances of the same problem. It is particularly useful for hierarchical data but can lead to infinite loops if not carefully managed.

### Example: Simple Recursion with a Counter
```python
def decrement_counter(counter):
    """Recursively decrements the counter until it reaches zero."""
    if counter <= 0:
        return
    print(counter)
    decrement_counter(counter - 1)
```

* **Explanation:** decrement_counter recursively calls itself, decrementing counter each time until it reaches zero.
* **Base Case:** The function stops when counter is zero, preventing infinite recursion.

### Example: Recursion with Nested Lists

```python
def print_nested_list(nested_list):
    """Recursively prints elements in a nested list structure."""
    for item in nested_list:
        if isinstance(item, list):
            print_nested_list(item)
        else:
            print(item)
```

* **Explanation:** print_nested_list traverses a nested list, printing each element. If an element is a list, it calls itself, enabling deep traversal.
* **Use Case:** This approach is helpful for data structures with multiple levels, like trees or directories.

### Key Considerations
1. **Recursion Limit:** Excessive recursion depth can lead to memory issues. Many languages, including Python, limit recursion depth to prevent such errors.
1. **Base Case:** Always include a stopping condition to prevent infinite recursion.