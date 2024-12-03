# Introduction to Java collections

In this video, we explore how Java handles **collections**, which are essential for maintaining groups of related items like students, employees, messages, or game characters.

---

## Collections in Programming

- Collections are used to store and manage groups of items, such as:
  - Students in a record system.
  - Employees in a workforce system.
  - Messages or texts in an email application.
  - Characters in a video game.
- Java provides robust tools for creating and working with collections, allowing for operations like:
  - **Adding items**
  - **Removing items**
  - **Sorting items**
  - **Iterating through items**

---

## ArrayLists: A Common Collection Type

### What is an ArrayList?
- A **resizable array-like structure** that stores objects.
- Part of Java's **generic collections**, meaning you can specify the type of objects the list will hold.

### Creating an ArrayList
- Example: Creating an ArrayList of Strings.
  ```java
  ArrayList<String> names = new ArrayList<>();
  ```
- Example: Creating an ArrayList of `TicketMachine` objects.
    ```java
    ArrayList<TicketMachine> machines = new ArrayList<>();
    ```

### Key Features
- **Indexing**: Items are indexed starting at `0`.
- **Flexibility**: You can add or remove objects dynamically.

---

## Iterating Over Collections

### Using a `for` Loop
- A concise and convenient way to process every element in a collection.
- Syntax:
    ```java
    for (Type element : collection) { 
        // Process each element 
    }
    ```
- Example: Iterating over a list of names.
    ```java    
    for (String name : names) { 
        System.out.println(name); 
    }
    ```
- Example: Iterating over a list of `TicketMachine` objects.
    ```java
    for (TicketMachine machine : machines) { 
        machine.printTicket(); 
    }
    ```
    
### Using a `while` Loop
- A more flexible looping structure for conditional iteration.
- Syntax:
    ```java
    while (condition) { 
        // Execute loop body 
    }
    ```

- Example: Iterating while a condition is true.
    ```java
    int i = 0; 
    while (i < names.size()) { 
        System.out.println(names.get(i)); 
        i++; 
    }
    ```  

---

## Choosing Between `for` and `while`

| **Scenario**                                  | **Recommended Loop** |
|-----------------------------------------------|-----------------------|
| Process every element in a collection         | `for` loop           |
| Locate a specific element or stop mid-iteration | `while` loop         |

---

## Summary

- **Collections** are fundamental for managing groups of related items.
- **ArrayLists** are a flexible and commonly used collection type.
- Two main looping structures for working with collections:
- **`for` loop**: Ideal for processing every item in the collection.
- **`while` loop**: More versatile, suitable for custom iteration conditions.
- Combining collections, loops, and conditionals allows you to write powerful and flexible programs.
