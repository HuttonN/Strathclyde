# Printing from methods

# The `printTicket` Method

In this video, we take a closer look at the **`printTicket`** method of the `NaiveTicketMachine` to understand what happens when it is called.

---

## Overview

- The `printTicket` method:
  - Uses the **`System.out.println`** method from the Java library to output information to the terminal.
  - Simulates the printing of a ticket by displaying formatted output.

---

## Exploring the Code

### Example of the `printTicket` Method

```java
public void printTicket() { 
System.out.println("##################"); 
System.out.println("# The BlueJ Line")
System.out.println("# Ticket")
System.out.println("# " + price + "cents.")
System.out.println("##################");
System.out.println();
```

---

## Breaking Down the Method

1. **Printing Lines**:
   - **First Line**:
     - `System.out.println("##################");`
     - Prints a row of hash symbols.
   - **Second Line**:
     - `System.out.println("# Ticket Price: " + price + " cents");`
     - Concatenates:
       - A string `"# Ticket Price: "`
       - The `price` field.
       - A string `" cents"`.
     - Outputs the formatted ticket price.
   - **Blank Line**:
     - `System.out.println();`
     - Prints a blank line to separate ticket details.

2. **Updating Fields**:
   - Updates the `total` field:
     - `total = total + balance;`
   - Resets the `balance` field:
     - `balance = 0;`

---

## Demonstration in BlueJ

1. **Setting Up**:
   - Open the `NaiveTicketMachine` project in BlueJ.
   - Open the editor and examine the `printTicket` method.

2. **Testing the Method**:
   - Create an instance of `TicketMachine` with a ticket price of `99`.
     ```
     TicketMachine ticketMachine = new TicketMachine(99);
     ```
   - Call the `printTicket` method:
     ```
     ticketMachine.printTicket();
     ```
   - Observe the output in the terminal:
     ```
     ##################
     # Ticket Price: 99 cents
     ```

---

## Key Concepts

- **`System.out.println`**:
  - A standard Java library method used to print output to the terminal.
  - Can print strings, concatenated values, or blank lines.

- **Concatenation**:
  - The `+` operator is used to combine strings with other data types (e.g., integers).

- **Field Updates**:
  - The method updates the `total` by adding the ticket price.
  - The `balance` is reset to `0`.

---

## Summary

- The `printTicket` method performs the following tasks:
  1. Prints formatted ticket details using `System.out.println`.
  2. Updates the `total` to reflect the new sale.
  3. Resets the `balance` to `0`.
- **Key takeaway**:
  - The method provides a clear example of how to format output, concatenate values, and update fields in a Java class.
