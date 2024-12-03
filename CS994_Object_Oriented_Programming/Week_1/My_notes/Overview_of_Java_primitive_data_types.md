# Java Primitive Data Types

In this video, we review the **base data types** in Java, also known as **primitive types**, and how they are used to store and manipulate data.

---

## Overview of Primitive Types

- A **variable** in Java is declared with a specific data type and assigned a value.
- Once a variable's data type is set, it cannot be changed, but the value can be reassigned.
- **Example**:
  ```java
  int VATRate = 20; // Declare a variable of type int with an initial value
  VATRate = 25;     // Reassign a new value
    ```
- The type remains `int` even after reassignment.

---

## List of Primitive Data Types

There are **8 primitive data types** in Java, each designed for specific use cases:

---

### 1. **byte**
- **Description**: An 8-bit signed 2's complement integer.
- **Range**: -128 to 127 (inclusive).
- **Default Value**: `0`.
- **Use Case**: Saves memory in large arrays where an `int` is not required.
- **Example**:
    ```java
    byte smallNumber = 100;
    ```

---

### 2. **short**
- **Description**: A 16-bit signed 2's complement integer.
- **Range**: -32,768 to 32,767 (inclusive).
- **Default Value**: `0`.
- **Use Case**: Saves memory in arrays compared to `int`.
- **Example**:
  ```java
  short mediumNumber = 2000;
    ```

---

### 3. **int**
- **Description**: A 32-bit signed 2's complement integer.
- **Range**: -2<sup>31</sup> to 2<sup>31</sup>-1 (approximately -2 billion to 2 billion).
- **Default Value**: `0`.
- **Use Case**: The most commonly used data type for storing whole numbers in Java programs.
- **Example**:
  ```java
  int largeNumber = 123456;
    ```

---

### 4. **long**
- **Description**: A 64-bit signed 2's complement integer.
- **Range**: -2<sup>63</sup> to 2<sup>63</sup>-1.
- **Default Value**: `0`.
- **Use Case**: Used when you need to store whole numbers that are larger than what an `int` can hold.
- **Example**:
    ```java
    long veryLargeNumber = 123456789L;
    ```

---

### 5. **float**
- **Description**: A 32-bit single-precision floating-point number.
- **Default Value**: `0.0`.
- **Use Case**: Used to store decimal numbers when saving memory is a priority, such as in large arrays of floating-point values, or when precision is less critical.
- **Example**:
  ```java
  float decimalNumber = 3.14f;
    ```

---

### 6. **double**
- **Description**: A 64-bit double-precision floating-point number.
- **Default Value**: `0.0`.
- **Use Case**: The default choice for storing decimal numbers in Java programs, providing higher precision than `float`.
- **Example**:
  ```java
  double preciseDecimal = 3.14159265358979;
    ```

---

### 7. **boolean**
- **Description**: Represents one of two possible values: `true` or `false`.
- **Default Value**: `false`.
- **Use Case**: Used for flags or conditions to track `true`/`false` states in logic.
- **Example**:
  ```java
  boolean isJavaFun = true;
    ```

---

### 8. **char**
- **Description**: A single 16-bit Unicode character.
- **Range**: Any Unicode character (65,536 possible values).
- **Default Value**: The null character `'\u0000'`.
- **Use Case**: Used to store a single character, such as letters, digits, or symbols, from various character sets.
- **Example**:
  ```java
  char letter = 'A';
    ```
---

## Summary

- Java provides **8 primitive data types** for storing various types of data:
  - **Integer types**: `byte`, `short`, `int`, `long`.
  - **Floating-point types**: `float`, `double`.
  - **Boolean type**: `boolean`.
  - **Character type**: `char`.
- Each type has:
  - A **default value**.
  - A **specific range** and **use case**.
- Using the appropriate data type helps manage memory efficiently and ensures precision in calculations.