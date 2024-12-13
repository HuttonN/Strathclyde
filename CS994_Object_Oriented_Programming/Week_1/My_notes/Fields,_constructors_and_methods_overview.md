# Fields, Constructors, and Methods

In this video, we explore the structure of Java classes, focusing on the three main components found in all Java classes: **fields**, **constructors**, and **methods**.

---

## Java Class Structure

1. **Class Definition**:
   - The class begins with a header that defines its name:
     ```java
     public class ClassName {
     ```
     - **`public`**: Indicates accessibility.
     - **`ClassName`**: Represents the name of the class.
   - The opening `{` and closing `}` curly braces encapsulate the class body.

2. **Key Components**:
   - Inside the class body, the following components are typically defined in order:
     1. **Fields**: Represent the state of the object.
     2. **Constructors**: Initialize the fields and create object instances.
     3. **Methods**: Define the behavior of the object.

---

## 1. Fields

- **Definition**:
  - Fields are variables that hold data and define the **state** of an object.
- **Example** (from the `TicketMachine` class):
    ```java
    private int price;
    private int balance;
    private int total;
    ```
- **Key Points:**
  - Each field has:
    - A **data type** (e.g., `int`) and a name.
    - **Values** that can change over time:
      - **`price`**: Represents the ticket price.
      - **`balance`**: Tracks the money inserted into the machine.
      - **`total`**: Tracks the total amount collected by the machine.
  - Different objects created from the same class can have different values in their fields.

### Instance Variables
- Fields are often referred to as **instance variables** because they store data specific to each object instance.

---

## 2. Constructors

### Definition
- Constructors are special methods used to initialize objects when they are created.

### Characteristics
- Always have the **same name** as the class.
- Do not have a **return type** (not even `void`).
- Often accept **parameters** to initialize fields.

### Example
```java
public TicketMachine(int cost) {
    price = cost;   // Assigns the parameter `cost` to the field `price`
    balance = 0;    // Initializes balance
    total = 0;      // Initializes total
}
```

## Assignment Statement

- The `=` symbol in `price = cost` assigns the value of the parameter `cost` to the field `price`.
- This is different from an **equality check**, which compares two values for equivalence.

---

## 3. Methods

### Definition
- Methods are used to:
  - Interact with objects.
  - Retrieve information about an object’s state.
  - Update the state of an object.

### Types of Methods

#### 1. **Accessor Methods**
- **Purpose**: Retrieve information about the object's state.
- **Behavior**: Do not modify the object.
- **Example**:
  ```java
  public int getBalance() {
      return balance;
  }
  ```

#### 2. **Mutator Methods**

- **Purpose**: Modify the object's state by updating fields.
- **Example**:
  ```java
  public void insertMoney(int amount) {
      balance = balance + amount;  // Updates the balance field
  }

---

## Order of Components

### Typical Order
1. **Fields**
2. **Constructors**
3. **Methods**

### Benefits of Following This Convention
- **Code readability**: Makes the structure easier to follow.
- **Ease of understanding**: Helps others working with your code.

---

## Summary

- **Fields**:
  - Represent the object's state and can vary across instances.
- **Constructors**:
  - Initialize fields and create object instances.
  - Often use parameters to pass data during object creation.
- **Methods**:
  - **Accessor Methods**: Retrieve data without modifying the object.
  - **Mutator Methods**: Change the object's state by updating fields.
- **Conventions**:
  - Following the tradition of placing fields first, followed by constructors and methods, improves code readability and maintainability.

---

Next: 
* [Fields](Fields.md)