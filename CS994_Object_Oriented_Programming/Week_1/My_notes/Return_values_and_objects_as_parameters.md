# Return Values and Objects as Parameters

In this video, we explore return types, method parameters, and how objects can be passed as parameters in Java.

---

## Setting Up BlueJ

1. Open BlueJ and load the **Lab Classes** project.
   - Close the **House** project if it is open.
2. **Compile the Project**:
   - The project needs to be compiled before creating objects.

---

## Creating a `Student` Object

1. **Using the Constructor**:
   - Unlike previous examples (e.g., `Circle`), the `Student` class constructor requires two parameters:
     - A **name** (String)
     - A **student ID** (String)
   - Example of valid input:
     ```java
     Student student1 = new Student("Phil Rogers", "12345");
     ```

2. **Common Errors**:
   - **Missing Quotes for Strings**:
     - Strings must be surrounded by double quotes, e.g., `"Phil Rogers"`.
   - **Incorrect Parameter Types**:
     - If you pass an integer instead of a string, an error occurs:
       - Example: Passing `12345` instead of `"12345"` causes a type mismatch error.

---

## Exploring `Student` Methods

### Methods Overview

The `Student` class includes several methods, categorized as follows:

1. **Setters**:
   - Modify attributes of the `Student` object.
   - Example:
     ```java
     student1.addCredits(100); // Adds 100 credits
     student1.changeName("Philip Rogers");
     ```

2. **Getters**:
   - Retrieve information from the `Student` object.
   - Example:
     ```java
     int credits = student1.getCredits(); // Returns the number of credits
     String name = student1.getName();    // Returns the student's name
     ```

3. **Void Methods**:
   - Perform actions but do not return values.
   - Example:
     ```java
     student1.print(); // Prints the student's details
     ```

---

### Examples of Method Calls

1. **Get Name**:
   - Returns the student's name as a string.
   - Example:
     ```java
     String name = student1.getName(); // Output: "Phil Rogers"
     ```

2. **Get and Add Credits**:
   - Initially, the credits are `0`.
   - Use `addCredits(int value)` to add credits:
     ```java
     student1.addCredits(100);
     int credits = student1.getCredits(); // Output: 100
     ```

3. **Change Name**:
   - Modify the student's name by passing a new string:
     ```java
     student1.changeName("Philip Rogers");
     ```

---

## Creating a `LabClass` Object

1. **Constructor Parameters**:
   - The `LabClass` constructor requires the maximum number of students (integer).
   - Example:
     ```java
     LabClass labClass1 = new LabClass(10);
     ```

2. **Enrolling a Student**:
   - The `enrolStudent` method accepts a `Student` object as a parameter.
   - Example:
     ```java
     labClass1.enrolStudent(student1);
     ```

---

## Observing Interactions Between Objects

1. **Objects as Parameters**:
   - The `enrolStudent` method demonstrates how objects (e.g., `Student`) can be passed as parameters to other objects (e.g., `LabClass`).

2. **Class Details**:
   - After enrolling a student, print the lab class details:
     ```java
     labClass1.printList();
     ```
   - Example output:
     ```
     Class Name: Unknown
     Instructor: Unknown
     Class List:
     - Philip Rogers
     Number of Students: 1
     ```

---

## Summary

- **Method Parameters**:
  - Methods can accept different parameter types, such as `String`, `int`, or objects (e.g., `Student`).
  - Correct parameter types must be provided to avoid errors.
- **Return Values**:
  - Methods can return values of specific types (e.g., `int`, `String`).
  - Example: `getCredits()` returns an integer representing the number of credits.

- **Objects as Parameters**:
  - Objects can be passed as parameters to other objects, enabling complex interactions.
  - Example: A `Student` object is passed to the `enrolStudent` method of the `LabClass` class.

- **BlueJ Tools**:
  - The terminal helps visualize Java code corresponding to method calls and object interactions.

---

Next: 
* [Chapter 1, Sections 1.12 to 1.14](Textbooks/Objects_First_with_Java/Chapter_1_Objects_and_Classes.pdf)
* Chapter 1 summary

