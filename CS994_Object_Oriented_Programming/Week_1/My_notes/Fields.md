# Fields

In this video, we take a closer look at the **fields** of a class by examining the `TicketMachine` class in BlueJ.

---

## What Are Fields?

- **Fields** are used to store the **state** of an object.
- In the `TicketMachine` class, the fields are:
  - `price`
  - `balance`
  - `total`

---

## Field Definition

Each field in the class has the following structure:
- **Access Modifier**:
  - The first word, `private`, means the field is private to the class.
  - **Implication**: Other classes cannot access or modify the field directly.
  - Example: Use a getter method (e.g., `getPrice()`) to retrieve a field’s value.
- **Data Type**:
  - The second word, `int`, specifies that the field stores an integer (whole number).
- **Field Name**:
  - The name of the field (e.g., `price`, `balance`, `total`).
- **Statement Terminator**:
  - Each field declaration ends with a semicolon (`;`).

---

## Field Behavior Across Instances

- Each object instance has its **own set of fields**.
- This means:
  - Each object can have a unique `price`, `balance`, and `total`.
  - Example:
    - Create two ticket machine objects:
        ```java
          TicketMachine ticketMachine1 = new TicketMachine(99);
          TicketMachine ticketMachine2 = new TicketMachine(50);
        ```
    - Inspecting these objects will show:
      - TicketMachine1’s `price` is 99.
      - TicketMachine2’s `price` is 50.
  - The fields belong to the object, not the class itself.

---

## Using Getters

To access the value of a field, use the corresponding getter method.

### Example of Using a Getter

```java
    int ticketPrice = ticketMachine1.getPrice()
```

---

## Summary

- Fields are used to store an object’s state and are declared using an **access modifier**, **data type**, and **field name**.
- **Private Fields**:
  - Cannot be accessed directly by other classes.
  - Require getter and setter methods for access and modification.
- **Field Values in Instances**:
  - Each object instance has its own unique values for the fields, even if they share the same class.

---

Next: 
* [Constructors, parameters and assignment](Constructors,_parameters_and_assignment.md)
* Relevant reading:
    * [Chapter 2, Section 2.4 Fields, constructors, and methods](Textbooks/Objects_First_with_Java/2.4_Fields_constructors_and_methods.pdf)
    * [Chapter 2, Section 2.5 Parameters: receiving data](Textbooks/Objects_First_with_Java/2.5_Parameters_receiving_data.pdf)
    * Chapter 2, Section 2.6 Assignment (read online)