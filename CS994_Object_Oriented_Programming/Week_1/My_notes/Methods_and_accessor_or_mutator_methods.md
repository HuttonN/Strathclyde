# Methods and accessor/mutator methods

In this video, we examine the **methods** of the `TicketMachine` class, focusing on **accessors** and **mutators**.

---

## Overview of Methods

- Methods are defined **after the fields and constructor** in the class.
- Often, methods are preceded by comments to describe their purpose. These comments are for human readers and provide clarity about the method’s functionality.

---

## Accessor Methods (Getters)

- **Definition**:
  - Accessor methods, or getters, retrieve the values of private fields.
  - These methods do not modify the state of the object.

- **Examples**:
  - `getPrice`:
    - Retrieves the value of the `price` field.
    - Example:
      ```java
      public int getPrice() {
          return price;
      }
      ```
  - `getBalance`:
    - Retrieves the value of the `balance` field.
    - Example:
      ```java
      public int getBalance() {
          return balance;
      }
      ```

- **Key Characteristics**:
  - The **return type** matches the field’s type (e.g., `int` for `price` and `balance`).
  - These methods take **no parameters**.
  - They provide controlled access to private fields (e.g., `price` and `balance`).

---

## Mutator Methods (Setters)

- **Definition**:
  - Mutator methods, or setters, modify the state of the object by updating fields.

- **Examples**:
  - `insertMoney`:
    - Takes a parameter `amount` (an integer) and adds it to the `balance`.
    - Example:
      ```java
      public void insertMoney(int amount) {
          balance = balance + amount;  // Updates the balance field
      }
      ```

  - `printTicket`:
    - Updates multiple fields (`total` and `balance`) while printing ticket information.
    - Example:
      ```java
      public void printTicket() {
          total = total + balance  // Updates total
          balance = 0;           // Resets balance
      }
      ```

- **Key Characteristics**:
  - The **return type** is often `void`, as these methods do not return a value.
  - They change the state of the object by updating one or more fields.

---

## Anatomy of a Method

1. **Visibility**:
   - The first word specifies the **visibility** of the method.
   - Example: `public` makes the method accessible to any code with access to the object.

2. **Return Type**:
   - Indicates what the method returns.
   - Example:
     - `int` for accessor methods like `getPrice`.
     - `void` for mutator methods like `insertMoney`.

3. **Parameters**:
   - Some methods take parameters to perform their tasks (e.g., `insertMoney(int amount)`).

4. **Method Body**:
   - Enclosed within `{}` curly braces.
   - Contains the instructions for what the method does.

---

## Summary

- **Accessor Methods**:
  - Provide read-only access to private fields.
  - Return the value of the field.
  - Example: `getPrice` and `getBalance`.

- **Mutator Methods**:
  - Change the state of the object by modifying fields.
  - Example: `insertMoney` and `printTicket`.

- **General Method Structure**:
  - The first word indicates visibility (e.g., `public`).
  - The return type specifies what the method will return (e.g., `int` or `void`).
  - The method body contains the logic and operations performed by the method.
