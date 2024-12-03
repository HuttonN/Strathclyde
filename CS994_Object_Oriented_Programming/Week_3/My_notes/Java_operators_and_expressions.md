# Java Operators and Expressions

In this video, we explore **Java expressions**, which involve combining variables with operators to compute values or perform actions.

---

## Overview of Expressions
- **Java expressions** combine:
  - **Variables**
  - **Operators**
  - **Keywords**
- An **assignment operator (`=`)** assigns the result of an expression to a variable.

### Example 1: Arithmetic Expression
```java
int x = a + b; // Adds integers a and b, assigns the result to x
```

### Example 2: String Concatenation
```java
String s = "Java" + "Programming"; // Combines two string literals
```

---

## Arithmetic Operators

| **Operator** | **Operation**       | **Example**              |
|--------------|---------------------|--------------------------|
| `+`          | Addition            | `x = a + b;`              |
| `-`          | Subtraction         | `x = a - b;`              |
| `*`          | Multiplication      | `x = a * b;`              |
| `/`          | Division            | `x = a / b;`              |
| `%`          | Modulo (remainder)  | `x = a % b;`              |

### Key Rules:
1. **Integer Arithmetic**:
   - Integer division truncates results (e.g., `5 / 2 = 2`).
2. **Mixed Type Arithmetic**:
   - If one operand is a `double`, the result is `double`.

---

## Increment and Decrement Operators

### Syntax
- **Increment (`++`)**: Adds 1 to a variable.
- **Decrement (`--`)**: Subtracts 1 from a variable.

### Examples
```java
int i = 8;
int j = i++; // Postfix: Assign i, then increment (j = 8, i = 9)
int k = ++i; // Prefix: Increment, then assign (i = 10, k = 10)
```

---

## Logical Operators

| **Operator** | **Operation**       | **Example**            |
|--------------|---------------------|------------------------|
| `&&`         | Logical AND         | ``a && b``                |
| `||`         | Logical OR          | ``a || b``                |
| `!`          | Logical NOT         | `!a`                    |
| `==`         | Equals              | `a == b`                |
| `!=`         | Not Equals          | `a != b`                |

### Important Distinction
- **`=`**: Assignment operator (e.g., `x = 10;`)
- **`==`**: Equality operator (e.g., `x == 10`)

---

## Conditional (Ternary) Operator

### Syntax
```java
condition ? value_if_true : value_if_false
```

### Example
```java
int max = (a > b) ? a : b; // Returns the larger of a and b
```

---

## Casting

### What is Casting?
- Converts a value from one type to another.

### Types of Casting
1. **Explicit Casting**:
   - Manually converting between types.
   - Example:
    ```java
     double d = 15.8;
     int i = (int) d; // Truncates to 15
    ```

2. **Implicit Casting**:
   - Automatic conversion from a smaller to a larger type (**widening**).
   - Example:
    ```java
     int i = 10;
     double d = i; // Converts int to double
    ```

### Limitations:
- **Narrowing Casts** (e.g., `double` to `int`) require explicit casting.
- Implicit casting only works for **widening** conversions.

---

## Summary

- **Expressions**: Combine variables, operators, and keywords to compute results.
- **Arithmetic Operators**: Perform basic calculations.
- **Increment/Decrement Operators**: Increase or decrease values by 1.
- **Logical Operators**: Return boolean values based on conditions.
- **Conditional Operator**: Short-hand for simple if-else logic.
- **Casting**:
  - Explicit casting is required for **narrowing** conversions.
  - Implicit casting works automatically for **widening** conversions.
