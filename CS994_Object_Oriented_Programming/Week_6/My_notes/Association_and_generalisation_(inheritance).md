# UML Class Diagram: Relationships Between Classes

## Types of Relationships in Class Diagrams

### 1. **Association**
- Represents a relationship between two classes.
- Example: `Student` and `Lecturer` have a relationship where the lecturer acts as a supervisor or tutor for the student.

#### Key Points:
- Association can be **unidirectional** or **bidirectional**.
  - **Unidirectional**: Only one class knows about the other.
    - Example: A `Student` class has a reference to the `Lecturer` class, but the `Lecturer` class does not reference the `Student`.
  - **Bidirectional**: Both classes know about each other.
    - Example: A `Student` class references the `Lecturer` class, and vice versa.
- If the `Student` object is destroyed, the `Lecturer` object remains unaffected.

#### Representation in Diagrams:
- **Unidirectional Association**: A line with an arrow pointing from the dependent class to the related class.
- **Bidirectional Association**: A line with or without arrows at both ends.

---

### 2. **Aggregation**
- Represents a "whole-part" relationship where the part can exist independently of the whole.
- Example: A `Library` aggregates `Books`. If the `Library` is destroyed, the `Books` still exist.

#### Key Points:
- Indicates ownership but not dependency.
- Represented with a line ending in a hollow diamond at the owning class.

---

### 3. **Composition**
- A stronger form of aggregation where the part cannot exist independently of the whole.
- Example: A `House` is composed of `Rooms`. If the `House` is destroyed, the `Rooms` cease to exist.

#### Key Points:
- Represents a "whole-part" relationship with a stronger dependency.
- Represented with a line ending in a filled diamond at the owning class.

---

### 4. **Generalisation (Inheritance)**
- Represents an "is-a" relationship where one class inherits from another.
- Example: A `Dog` is a subclass of `Animal`.

#### Key Points:
- Represented with a solid line ending in a closed arrow (triangle) pointing to the parent class.
- Abstract classes can be identified with the keyword `abstract` before the class name.

---

### 5. **Interface**
- Similar to an abstract class but with no attributes, and all methods are abstract.
- Example: A `Bird` class implements the `Flyable` interface.

#### Key Points:
- Represented with a dashed line ending in a closed arrow (triangle) pointing to the interface.
- In Java, the keyword `implements` is used.

---

## Conceptual Differences Between Relationships

| Relationship Type | Dependency | Directionality | Representation in Diagrams |
|-------------------|------------|----------------|----------------------------|
| **Association**   | None       | Uni/Bi         | Line (with optional arrow) |
| **Aggregation**   | Weak       | Uni            | Hollow diamond             |
| **Composition**   | Strong     | Uni            | Filled diamond             |
| **Generalisation**| Inheritance| Uni            | Solid line with triangle   |
| **Interface**     | None       | Uni            | Dashed line with triangle  |

---

## Code Implementation Examples

### Example 1: Unidirectional Association

Class `Student` references `Lecturer`:
```java
class Student {
    private Lecturer tutor;
}
class Lecturer {
    // No reference to Student
}
```

### Example 2: Bidirectional Association

Class `Student` references `Lecturer` and vice versa:
```java
class Student {
    private Lecturer tutor;
}
class Lecturer {
    private List<Student> students;
}
```

### Example 3: Aggreagation

Class `Library` aggregates `Book`:
```java
class Library {
    private List<Book> books;
}
class Book {
    // Exists independently of Library
}
```

### Example 4: Composition

Class `House` composed of `Room`:
```java
class House {
    private List<Room> rooms;
}
class Room {
    // Exists only as part of House
}
```

### Example 5: Generalisation

Class `Dog` inherits from `Animal`:
```java
abstract class Animal {
    abstract void makeSound();
}
class Dog extends Animal {
    void makeSound() {
        System.out.println("Bark");
    }
}
```

### Example 6: Interface

Class `Bird` implements `Flyable`:
```java
interface Flyable {
    void fly();
}
class Bird implements Flyable {
    public void fly() {
        System.out.println("Flying");
    }
}
```

---

## Summary
* Relationships such as association, aggregation, composition, generalisation, and interfaces help model real-world systems in UML diagrams. 
* Understanding the differences between these relationships is crucial for creating effective designs and writing clean, maintainable code.