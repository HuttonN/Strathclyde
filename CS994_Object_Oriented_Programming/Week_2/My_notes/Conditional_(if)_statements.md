# Conditional (if) statements

In this video, we explore improvements made to the **NaiveTicketMachine** by introducing safety checks to handle invalid inputs and ensure correct operation.

---

## Key Improvements

### 1. Safety Check in `insertMoney` Method
- A **conditional statement** checks the validity of the amount inserted.
- Code:
    ```java
    public void insertMoney(int amount) { 
        if (amount > 0) { 
            balance = balance + amount; // Updates the balance 
        } 
        else { 
            System.out.println("Use a positive amount rather than " + amount); 
        } 
    }
    ```

- **How it Works**:
- If the `amount` is greater than 0:
  - Adds the `amount` to `balance`.
- Otherwise:
  - Prints an error message indicating the amount must be positive.

### 2. Validation in `printTicket` Method
- A **conditional statement** ensures the user has inserted enough money to buy the ticket.
- Code:
    ```java
    public void printTicket() {
        if (balance >= price) { 
            System.out.println("##################"); 
            System.out.println("# The BlueJ line");
            System.out.println("# Ticket");
            System.out.println("# " + price + " cents"); 
            System.out.println("##################"); 
            System.out.println()

            // Update the total collected with the price
            total = total + price; 
            // Reduce the balance by the price.
            balance = balance - price; 
        } 
        else { 
            System.out.println("You must insert at least " + (price - balance) + " more cents."); 
        } 
    }
    ```
    
- **How it Works**:
- If `balance >= price`:
  - Executes the first block of code:
    - Prints the ticket.
    - Updates `total` and deducts the ticket price from `balance`.
- Otherwise:
  - Executes the `else` block:
    - Calculates the remaining amount needed: `price - balance`.
    - Prints an error message indicating the additional amount required.

---

## Demonstration

1. **Creating an Instance**:
 - Create a new instance of the improved `TicketMachine`:
   ```java
   TicketMachine ticketMachine = new TicketMachine(99);
   ```
 - Sets the ticket price to 99 cents.

2. **Testing `insertMoney`**:
 - Attempt to insert a negative amount:
   ```java
   ticketMachine.insertMoney(-10);
   ```
 - Output:
   ```
   Use a positive amount rather than -10
   ```
 - Insert a valid amount:
   ```java
   ticketMachine.insertMoney(50);
   ```
 - Balance is updated without errors.

3. **Testing `printTicket`**:
 - Attempt to print a ticket with insufficient balance:
   ```java
   ticketMachine.printTicket();
   ```
 - Output:
   ```
   You must insert at least 49 more cents.
   ```
 - Insert the remaining amount and print the ticket:
   ```java
   ticketMachine.insertMoney(49);
   ticketMachine.printTicket();
   ```
 - Output:
   ```
   ##################
   # Ticket Price: 99 cents
   ```

---

## Conditional Statements in Action

1. **Structure**:
 - Two blocks of code (inside `{}` curly braces).
 - A **boolean expression** determines which block executes.

2. **Example in `printTicket`**:
 - Boolean expression: `balance >= price`
 - If **true**:
   - Executes the block for printing the ticket and updating fields.
 - If **false**:
   - Skips to the `else` block to display an error message.

---

## Key Takeaways

- **Safety Checks**:
- Prevent invalid inputs using conditional statements.
- Ensure the user has sufficient balance before printing a ticket.

- **Conditional Logic**:
- The `if` statement evaluates a **boolean expression** to decide which block of code to execute.

- **Outcome**:
- The improved ticket machine is more robust, handling edge cases and invalid inputs gracefully.
