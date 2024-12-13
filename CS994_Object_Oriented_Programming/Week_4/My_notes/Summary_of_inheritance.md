# Summary of inheritance

## Introduction
Inheritance is a fundamental concept in object-oriented programming, allowing hierarchical organization of classes. This mechanism enables child classes (or subclasses) to inherit data (variables) and behaviors (methods) from parent classes (or superclasses). In addition, subclasses can have their own unique traits and behaviors.

---

## Hierarchical Structure
### Mammal-Dog-German Shepherd Example:
- **Mammals**: Top-level superclass.
- **Dogs**: Subset (child class) of mammals.
- **German Shepherds**: Subset (child class) of dogs.
  
### Key Relationships:
- **German Shepherd**:
  - Inherits traits from **Dogs** and **Mammals**.
  - Can have its own traits (e.g., methods like `bite()` or `detect()`).
- Other subclasses of **Dogs** (e.g., Poodles) can have unique traits.

---

## Key Concepts in Programming Terms
1. **Subclass**:
   - A class derived from a superclass.
   - Example: `Dog` is a subclass of `Mammal`.
   
2. **Inheritance**:
   - Subclasses inherit data (variables) and behaviors (methods) from their superclasses.
   - Subclasses can add new methods or override inherited methods.

3. **Overriding**:
   - Subclasses can modify the behavior of inherited methods by overriding them.

---

## Formal Definitions
1. **Inheritance**:
   - Mechanism for modular and hierarchical organization of classes.
   - A subclass extends a superclass, inheriting its members (fields and methods) but **not** its constructor.

2. **Polymorphism**:
   - Allows specialization of inherited behavior by overriding methods in the subclass.

3. **Constructor**:
   - Special method in Java used to initialize objects.
   - **Superclass constructors are not inherited**; they must be explicitly called using the `super` keyword.

---

## Java Inheritance Hierarchy
1. **All Java Classes Inherit From `Object`**:
   - The root class in Java.
   - Each class inherits from exactly one parent class.

2. **Interfaces**:
   - Java supports multiple inheritance through interfaces.
   - A class can implement multiple interfaces.

---

## Example: Mammal-Dog-German Shepherd
```java
// Superclass
class Mammal {
    public void eat() {
        System.out.println("Eating...");
    }
}

// Subclass
class Dog extends Mammal {
    public void bark() {
        System.out.println("Barking...");
    }
}

// Sub-subclass
class GermanShepherd extends Dog {
    public void guard() {
        System.out.println("Guarding...");
    }
}
```

### Usage

```java
GermanShepherd gs = new GermanShepherd();
gs.eat();       // Inherited from Mammal
gs.bark();      // Inherited from Dog
gs.guard();     // Unique to German Shepherd
```

## Java Collections Example

The Java Collections Framework is organized hierarchically:

### Hierarchy Overview
- **Root**: `Collection` interface.
- **Set Interface**:
  - Child classes: `TreeSet`, `HashSet`, `LinkedHashSet`.
- **List Interface**:
  - Child classes: `ArrayList`, `LinkedList`.

---

### Key Points
1. Subclasses inherit data and behaviors from superclasses but can also have unique methods.
2. Constructors are **not inherited**; `super` must be explicitly used.
3. The `Object` class is the universal superclass for all Java classes.
4. Java supports **single inheritance** but allows **multiple inheritance** through interfaces.

---

### Summary
Inheritance enables:
- **Code reuse** and **hierarchical organization**.
- Seamless integration into Java's built-in class structures, such as the **Collections Framework**.

It is a powerful feature in object-oriented programming but requires careful design when:
- Overriding methods.
- Implementing constructors.

