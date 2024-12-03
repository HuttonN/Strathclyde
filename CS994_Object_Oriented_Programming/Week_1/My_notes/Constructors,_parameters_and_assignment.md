# Constructors, parameters and assignment

In this video, we explore **constructors** by examining the `TicketMachine` class from Chapter 2 of the BlueJ textbook.

---

## What is a Constructor?

- A **constructor** is a special method in a Java class used to create new instances of the class.
- Whenever a new instance of a class is needed, the constructor must be called.

---

## Examining the Constructor

1. **Constructor in the `TicketMachine` Class**:
   - The constructor takes a single parameter, `cost`, which represents the ticket price.
   - The `cost` parameter is assigned to the field `price`.
   - Example of the constructor:
     ```java
     public TicketMachine(int cost) {
         price = cost;   // Assigns the parameter `cost` to the field `price`
         balance = 0;    // Initializes balance
         total = 0;      // Initializes total
     }
     ```

2. **Initialization**:
   - The constructor initializes the fields `balance` and `total` to `0`.
   - This ensures that these fields have default values when the object is created.

---

## How the Constructor Works

1. **Parameter Handling**:
   - The parameter `cost` is passed to the constructor:
     - `cost` is used to set the value of the `price` field.
     - Once the constructor finishes executing, the `cost` parameter is discarded, and only the fields (`price`, `balance`, `total`) remain.

2. **Scope of the Constructor**:
   - The body of the constructor is defined by the curly braces `{}`.
   - Example:
     ```java
     public TicketMachine(int cost) {
         // Constructor body starts
         price = cost;
         balance = 0;
         total = 0;
         // Constructor body ends
     }
     ```
   - When the closing curly brace `}` is reached, the constructor completes, and any local variables (e.g., `cost`) are no longer available.

---

## Key Points

- The constructor's primary purpose is to **initialize** the fields of the class when an object is created.
- **Parameters** are used to pass values to the constructor, which are then used to set the fields.
- Once the constructor completes, only the fields remain; any local variables (e.g., `cost`) are discarded.

---

## Summary

- **Constructors** are special methods used to create new instances of a class.
- They:
  - Accept **parameters** to initialize fields.
  - Assign values to the fields of the class.
- In the `TicketMachine` class:
  - The constructor assigns `cost` to the `price` field.
  - It initializes `balance` and `total` to `0`.
- After execution, the constructor discards any local parameters, leaving only the class fields.

