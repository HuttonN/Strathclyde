# Overview of conditional (if) statements

In this video, we examine the **flaws** in the `NaiveTicketMachine` and introduce **conditional statements** to address them.

---

## Identifying a Flaw

- The current implementation of the `NaiveTicketMachine` allows printing a ticket without verifying if enough money has been inserted.
- This flaw makes the ticket machine ineffective, as it can issue tickets for free.

---

## Introduction to Conditional Statements

- **Conditional statements** allow the execution of specific blocks of code based on certain conditions.
- **Key Concepts**:
  - Use the keyword `if` to evaluate a condition.
  - Optionally, use the keyword `else` to execute an alternative block of code if the condition is false.
  - Conditions must evaluate to a **boolean value** (`true` or `false`).

---

## Structure of a Conditional Statement

### Basic Structure:

```java
if (some test) { 
// Statements to execute if condition is true // 
} else { 
// Statements to execute if condition is false (optional) 
}
```

---

### Explanation of the Code

1. **Condition**:
   - The `if` statement checks whether `balance` is greater than or equal to `price`.
   - Example:
     - `balance = 99`, `price = 99` → Condition evaluates to `true`.
     - `balance = 50`, `price = 99` → Condition evaluates to `false`.

2. **If True**:
   - Executes the block:
     - Prints the ticket using `printTicket()`.
     - Updates `total` to reflect the sale.
     - Deducts the ticket price from `balance`.

3. **If False**:
   - Displays a message prompting the user to insert more money.

---

### Key Concepts Recap

- **Conditional Statements**:
  - Allow code to make decisions based on variable values.
  - Execute different actions depending on the result of a condition.

- **Boolean Expressions**:
  - Evaluate to `true` or `false`.
  - Example: `balance >= price`.

- **Usage**:
  - Make the ticket machine smarter by ensuring it only prints tickets when sufficient payment has been received.

---

## Summary

- **Flaw in NaiveTicketMachine**:
  - Tickets can be printed without verifying payment.
- **Solution**:
  - Use conditional statements to check payment before allowing ticket printing.
- **Structure**:
  - Use `if` for conditions and `else` for alternative actions.
- **Outcome**:
  - Conditional logic allows the ticket machine to handle scenarios dynamically, improving functionality.
