# Exploring the Ticket Machine Project

In this Week 2 video, we explore the **Ticket Machine** project from Chapter 2 of the BlueJ textbook.

---

## Setting Up the Project

1. **Opening the Project**:
   - Navigate to **Chapter 2** and open the project **A Naive Ticket Machine**.
2. **Compiling the Code**:
   - Compile the project to remove the striped lines on the classes.

---

## Creating a `TicketMachine` Object

1. **Constructor**:
   - The `TicketMachine` constructor requires an **integer parameter** representing the cost of a ticket.
   - Example:
     ```java
     TicketMachine ticketMachine1 = new TicketMachine(99);
     ```
   - This creates an instance named `ticketMachine1` with a ticket cost of 99.

---

## Methods in the `TicketMachine` Class

### 1. **Getter Methods**
- **Get Balance**:
  - Method: `getBalance()`
  - Description: Returns the current balance as an integer.
  - Example:
    ```java
    int balance = ticketMachine1.getBalance(); // Output: 0
    ```
- **Get Price**:
  - Method: `getPrice()`
  - Description: Returns the ticket price as an integer.
  - Example:
    ```java
    int price = ticketMachine1.getPrice(); // Output: 99
    ```

---

### 2. **Other Methods**
- **Insert Money**:
  - Method: `insertMoney(int amount)`
  - Description: Adds the specified amount to the current balance.
  - Example:
    ```java
    ticketMachine1.insertMoney(50); // Adds 50 to the balance
    ```
- **Print Ticket**:
  - Method: `printTicket()`
  - Description: Prints the ticket and adjusts the machine's balance and totals.

---

## Inspecting Objects

1. **Object Properties**:
   - Use the **Inspect** tool to examine the attributes of a `TicketMachine` instance.
   - Attributes include:
     - `price`: The cost of the ticket.
     - `balance`: The current balance (initially 0).
     - `total`: The total amount collected by the machine (initially 0).

2. **Example**:
   - Inspecting `ticketMachine1`:
     ```
     price: 99
     balance: 0
     total: 0
     ```
   - Inspecting another instance (e.g., `ticketMachine2` with a price of 50):
     ```
     price: 50
     balance: 0
     total: 0
     ```

---

## Summary

- The **Ticket Machine** project demonstrates:
  - **Constructors**: Creating objects with specific parameters.
  - **Getter Methods**: Retrieving information about an object’s state.
  - **Inspecting Objects**: Viewing and confirming attributes using BlueJ’s inspect tool.
- This short video introduces the basic functionality of the `TicketMachine` class. We will revisit this project later for further exploration.