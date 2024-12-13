# Subtyping (part 2)

In this video, we discuss how the relationship between subtypes and supertypes is preserved when creating new variables, and why this is important in understanding inheritance.

---

## Inheritance Hierarchy Example

Consider a simple inheritance hierarchy:

- **`Vehicle`** is the root superclass.
- **`Car`** and **`Bicycle`** are subtypes of `Vehicle`.

This relationship is central to understanding how variables of supertypes can reference objects of subtypes.

---

## Assigning Subtypes to Supertype Variables

### Standard Object Creation

```java
Vehicle v1 = new Vehicle();
```

- A variable `v1` of type `Vehicle` is assigned a new instance of the `Vehicle` class.
- This is a standard object creation pattern.

### Assigning Subtypes
1. **Bicycle as a Vehicle**:
```java
Vehicle v2 = new Bicycle();
```

- Here, `v2` is a variable of type `Vehicle`, but it references an instance of `Bicycle`.
- This is acceptable because `Bicycle` is a subtype of `Vehicle`.

2. **Car as a Vehicle**:
```java
Vehicle v3 = new Car();
```

- Similarly, `v3` is a `Vehicle` variable referencing a `Car` object.
- This works because `Car` is also a subtype of `Vehicle`.

### Key Concept
- **Subtypes can replace supertypes** because they "do everything the supertype does, and potentially more."
- This relationship is described as **"is-a"**:
  - A **Bicycle is a Vehicle**.
  - A **Car is a Vehicle**.

---

## Common Error: Supertype to Subtype Assignment

### Invalid Assignment Example
```java
Car c1 = new Vehicle(); // Error
```

- This does not work because:
  - A `Vehicle` is not necessarily a `Car`.
  - A `Car` might have additional attributes (e.g., `engineSize`) that do not exist in `Vehicle`.
- Attempting this causes problems because the `Vehicle` object lacks the specific attributes and behaviors of a `Car`.

---

## Key Rule

- **Subtypes can replace supertypes**, but **supertypes cannot replace subtypes**.

---

## Practical Importance: Collections

This relationship is particularly significant when working with **collections**. For example:

- **Collection of a Supertype**:
```java
List<Vehicle> vehicles = new ArrayList<>();
```

- A single collection of type `Vehicle` can hold instances of `Car`, `Bicycle`, or any other `Vehicle` subtype.

- **Why This Matters**:
  - Collections can be designed to work with abstract supertypes.
  - The specific subtype of each object in the collection does not matter, allowing for greater flexibility and scalability.

---

## Conclusion

Understanding the relationship between subtypes and supertypes is crucial for leveraging the power of inheritance. Subtypes can replace supertypes in variable assignments and collections, making code more flexible and reusable. However, remember that the reverse is not true: supertypes cannot replace subtypes, as this leads to compatibility issues.
