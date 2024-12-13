# Goals, principles & patterns

In this video, we discuss **object-oriented design**, focusing on its **goals**, **principles**, and **patterns**. These concepts are fundamental to creating efficient, maintainable, and flexible software.

---

## Goals of Object-Oriented Design

The three primary goals are:

### Responsibility
- Break the system into distinct **actors**, each with a specific responsibility.
- These **actors** become the classes in the software.

### Independence
- Ensure that each class operates as independently as possible from others.
- Minimise dependencies between classes.

### Behaviour
- Carefully define the behaviour of each class.
- Ensure the consequences of actions performed **on** or **by** a class are clear and predictable for any interacting class.

---

### Additional Goals for Software Design
- **Correctness**: The software must meet its intended purpose.
- **Readability**: It should be understandable and verifiable by others.
- **Robustness**: Handle unexpected inputs gracefully.
- **Efficiency**: Optimise computing time and memory usage.
- **Flexibility**: Generalise the system for multiple scenarios.
- **Reusability**: Write code that can be reused in other projects.

---

## Principles of Object-Oriented Design

There are four key principles:

### 1. Abstraction
- **Definition**: Extract the essence of a system, focusing on its fundamental parts.
- **Purpose**: Generalise the system for use in different scenarios.

### 2. Encapsulation
- Achieve **information hiding**:
  - Only expose necessary details to other parts of the system.
  - Keep internal implementation details private.
- This allows developers to modify the internal workings of a class without affecting its external interface.

### 3. Modularity
- Divide the system into **distinct modules** or components to:
  - Simplify design and maintenance.
  - Make complex systems easier to manage.
- Each module has a well-specified role and communicates through clear interfaces.
- In Java, the **package** is the primary unit for organising modules.

### 4. Hierarchical Organisation
- Arrange classes and objects in a structured hierarchy.
- Define relationships between classes using inheritance.

---

## Design Patterns in Object-Oriented Design

There are two main types of design patterns:

### Algorithmic Patterns
- Generalised methods to solve common problems, e.g., sorting a list.
- Examples discussed in this course:
  - **Recursion**
  - **Brute Force**
  - **Greedy Method**

### Software Design Patterns
- Templates for creating specific types of software.
- These patterns provide proven solutions to recurring design problems.
- Examples to be covered in later videos.

---

## Summary

- **Goals**: Responsibility, independence, and well-defined behaviour for each class.
- **Principles**: Abstraction, encapsulation, modularity, and hierarchical organisation.
- **Patterns**: Algorithmic and software design patterns help standardise and generalise solutions.

Stay tuned for upcoming videos where we dive deeper into these topics, including **modular design**, **interface design**, and **design patterns**.
