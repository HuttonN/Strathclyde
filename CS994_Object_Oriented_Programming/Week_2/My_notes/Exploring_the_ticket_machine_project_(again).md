# Exploring the Ticket Machine project

In this Week 2 video, we explore the **`NaiveTicketMachine`** project from Chapter 2 in BlueJ.

---

## Setting Up

1. **Open the Project**:
   - Open the `NaiveTicketMachine` project in BlueJ.
   - Compile the project to remove any striped lines in the class diagram.

2. **Create an Instance**:
   - Use the constructor to create a new instance of the `TicketMachine` class.
   - Example:
     ```java
     TicketMachine ticketMachine1 = new TicketMachine(99);
     ```
   - This creates a ticket machine with a ticket price of 99.

---

## Available Methods

1. **Getter Methods**:
   - **`getBalance`**:
     - Returns the current balance as an integer.
   - **`getPrice`**:
     - Returns the ticket price as an integer.

2. **Mutator Methods**:
   - **`insertMoney`**:
     - Accepts an integer amount and adds it to the current balance.
   - **`printTicket`**:
     - Prints the ticket details and resets the balance.

---

## Demonstration

1. **Inspecting the First Instance**:
   - Create an instance of `TicketMachine` with a ticket price of 99:
     ```
     TicketMachine ticketMachine1 = new TicketMachine(99);
     ```
   - Inspect the object:
     - **Fields**:
       - `price`: 99
       - `balance`: 0
       - `total`: 0

2. **Creating a Second Instance**:
   - Create another instance with a ticket price of 50:
     ```
     TicketMachine ticketMachine2 = new TicketMachine(50);
     ```
   - Inspect the object:
     - **Fields**:
       - `price`: 50
       - `balance`: 0
       - `total`: 0

3. **Using Getter Methods**:
   - **Example**:
     ```
     int balance = ticketMachine1.getBalance(); // Returns 0
     int price = ticketMachine1.getPrice();     // Returns 99
     ```

---

## Key Points

- The **constructor** initializes the ticket machine with a specified ticket price.
- The **getter methods** provide read-only access to the ticket machine's fields.
- The **mutator methods** allow users to interact with the machine by inserting money or printing a ticket.
- Each ticket machine instance maintains its own state (e.g., `price`, `balance`, `total`).

---

## Summary

- We explored the basic functionality of the `NaiveTicketMachine`.
- Key methods include:
  - **Getters**: `getBalance` and `getPrice`.
  - **Mutators**: `insertMoney` and `printTicket`.
- Each instance of the `TicketMachine` class can have a unique ticket price and maintains its own state.
- We'll revisit the `TicketMachine` in future sessions to enhance its functionality.
