# Anatomy of a Java Class and Class Headers

In this video, we explore the structure of a Java class by examining the source code of the `TicketMachine` class in BlueJ.

---

## Opening the Source Code

1. **Accessing the Code**:
   - Open the **Ticket Machine** project in BlueJ.
   - Right-click on the `TicketMachine` class and select `Open Editor` to view the source code.

2. **Class Overview**:
   - The file begins with an optional **block of comments**, typically used to:
     - Describe the purpose of the class.
     - Provide metadata (e.g., author, creation date).
     - Include licensing terms.

---

## Class Declaration

1. **Class Header**:
   - The first line of code:
     ```java
     public class TicketMachine {
     ```
     - **`public`**: Indicates that the class is accessible by other code.
     - **`class`**: Declares that this is a class.
     - **`TicketMachine`**: The name of the class.

2. **Curly Braces**:
   - The **opening curly brace** `{` marks the start of the class body.
   - The **closing curly brace** `}` is located at the bottom of the class.
   - In BlueJ:
     - The **class body** is highlighted in pale green.
     - Methods are highlighted in yellow.

---

## Structure of a Java Class

A typical Java class has three main components:

### 1. **Fields**
   - Fields define the **state** of the object.
   - In `TicketMachine`, the fields are:
     ```java
     private int price;
     private int balance;
     private int total;
     ```
   - These fields store:
     - `price`: The cost of a ticket.
     - `balance`: The current balance.
     - `total`: The total amount collected.

---

### 2. **Constructors**
   - **Purpose**: Used to create and initialize objects.
   - Example:
     ```java
     public TicketMachine(int cost) {
         price = cost;
         balance = 0;
         total = 0;
     }
     ```
   - **Key Points**:
     - The constructor name matches the class name (`TicketMachine`).
     - It takes a parameter (`int cost`) to set the `price` field.
     - The other fields (`balance` and `total`) are initialized to `0`.
     - Although Java sets integer fields to `0` by default, explicitly initializing them is considered good practice.

---

### 3. **Methods**
   - Methods define the **behavior** of the class and allow interaction with objects.
   - Example methods in `TicketMachine`:
     1. **Getter Methods**:
        - **Get Price**:
          ```java
          public int getPrice() {
              return price;
          }
          ```
        - **Get Balance**:
          ```java
          public int getBalance() {
              return balance;
          }
          ```
     2. **Insert Money**:
        - Adds money to the current balance:
          ```java
          public void insertMoney(int amount) {
              balance = balance + amount;
          }
          ```
     3. **Print Ticket**:
        - Simulates printing a ticket:
          ```java
          public void printTicket() {
              // Ticket printing logic
          }
          ```

---

## Summary

- The anatomy of a Java class includes:
  1. **Fields**: Represent the object's state.
  2. **Constructors**: Initialize the object's fields and ensure proper setup.
  3. **Methods**: Define the behavior and allow interaction with the object.
- Key features in the `TicketMachine` class:
  - The **class header** specifies accessibility (`public`) and the class name.
  - The **constructor** initializes fields, demonstrating good programming practice.
  - The **methods** provide functionality such as retrieving values, modifying fields, and performing actions.
