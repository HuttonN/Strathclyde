# The Student class example

In this video, we explore the **`Student` class** from the **Lab Classes** project in BlueJ. This class represents a student in a university administration system and stores important details such as their name, ID, and credit count.

---

## Overview of the `Student` Class

- **Purpose**:
  - The `Student` class manages data about a university student, including:
    - **Name**: The student's full name.
    - **ID**: The unique student ID.
    - **Credits**: The number of academic credits they have earned.

---

## Fields

The fields of the `Student` class store the student's state:

```java
private String name; // Stores the student's full name 
private String id; // Stores the student's unique ID 
private int credits; // Tracks the student's earned credits
```

---

## Constructor

- **Purpose**:
  - The constructor initializes the fields when creating a new `Student` object.
  - It accepts two parameters: the student's name and ID.

- **Code Example**:

```java
public Student(String fullName, String studentID) { 
    this.name = fullName; // Initializes the name field 
    this.id = studentID; // Initializes the id field 
    this.credits = 0; // Sets the initial credit count to 0 
}
```

---

## Methods

### Accessor (Getter) Methods

1. **Get Name**
   - Returns the student's full name as a `String`.
   - Example:
        ```java
        public String getName() { 
            return name; 
        }
        ```

2. **Get ID**
- Returns the student's unique ID as a `String`.
- Example:  
    ```java
    public String getID() { 
        return id; 
    }
    ```
    
3. **Get Credits**
- Returns the total number of credits the student has earned.
- Example:
    ```java
    public int getCredits() { 
        return credits; 
    }
    ```

4. **Get Login Name**
- Combines the student's name and ID to generate a unique login name.
- Example:
    ```java
    public String getLoginName() { 
        return name.toLowerCase() + id; 
    }
    ```
    
---

### Mutator (Setter) Methods

1. **Change Name**
- Updates the `name` field with a new value.
- **Note**: Strings in Java are immutable, meaning they cannot be modified. Instead, the `name` field is replaced with a new string.
- Example:
    ```java
    public void changeName(String replacementName) { 
        name = replacementName; 
    }
    ```

2. **Add Credits**
- Adds a specified number of credits to the `credits` field.
- Example:
    ```java
    public void addCredits(int amount) { 
        credits += amount; 
    }
    ```

---

### Print Details

- Prints all details about the student, including:
- Name
- ID
- Credits
- Example:
    ```java
    public void printDetails() { 
        System.out.println("Name: " + name); 
        System.out.println("ID: " + id); 
        System.out.println("Credits: " + credits); 
    }
    ```

---

## Key Characteristics

1. **Immutable Fields**:
   - The `id` field is immutable, meaning there is no method to modify it after the object is created.
   - Strings (such as `name` and `id`) in Java are also immutable. To "change" a string, you must replace it with a new one.

2. **Initialization in Constructor**:
   - The constructor sets the `name` and `id` fields based on the parameters passed in, while the `credits` field is initialized to `0`.

---

## Summary

The `Student` class:
- Represents a student in the university system.
- Stores key details such as their name, ID, and credit count.
- Includes **getter methods** for retrieving data and **setter methods** for updating specific fields.
- Demonstrates the immutability of certain fields and Java strings.
