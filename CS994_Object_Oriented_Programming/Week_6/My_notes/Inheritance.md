# Inheritance

In this video, we explore **inheritance** in object-oriented design, using a hierarchical example to explain key concepts.

---

## Hierarchical Structure in OOP

Object-oriented programming structures software components hierarchically, forming a **tree structure**:

1. **Mammals** (Superclass)
   - **Dogs** (Subclass of Mammals)
     - **German Shepherds** (Subclass of Dogs)

This hierarchical relationship demonstrates inheritance:
- **German Shepherds** inherit characteristics from **Dogs** and **Mammals**.
- Each level in the hierarchy adds its own unique traits.

---

## Inheritance in Programming Terms

- A **subclass** (or child class) is derived from a **superclass** (or parent class).
- Subclasses automatically inherit:
  - **Data** (fields/variables)
  - **Behaviours** (methods)
- Subclasses can:
  - **Augment behaviours** by adding new methods or fields.
  - **Specialise behaviours** by overriding methods from the parent class.

### Example:
- **Superclass (Dog):**
  - Generic methods like `bark()`.
- **Subclass (German Shepherd):**
  - Inherits `bark()` but also adds `bite()` and `detectCriminals()`.

---

## Formal Definition of Inheritance

1. **Mechanism for Modular and Hierarchical Organisation**
   - Subclasses **extend** superclasses.

2. **Characteristics of Inheritance**
   - **Inherits Members**: Subclasses inherit fields and methods.
   - **Does Not Inherit Constructors**: Superclass constructors must be explicitly called.

3. **Specialisation with Polymorphism**
   - Subclasses **override** methods from superclasses to specialise behaviour.

4. **Java-Specific Details**
   - Every object in Java inherits from the root class `Object`.
   - Java supports **single inheritance** (one parent class).
   - Subclasses can also inherit from **interfaces**, enabling multiple inheritance-like behaviour.

---

## Constructors in Inheritance

- Constructors are **not inherited** in Java.
- A subclass must explicitly call the superclass constructor using the `super` keyword.
- The superclass constructor is the first operation when creating a subclass.

---

## Example: Java's Class Hierarchy

The Java language itself uses a hierarchical structure:

- **Collection Interface** (Root)
  - **Set Interface**
    - Subclasses: `TreeSet`, `HashSet`, `LinkedHashSet`
  - **List Interface**
    - Subclasses: `ArrayList`, `LinkedList`

This demonstrates how Java employs inheritance to organise its built-in classes.

---

## Summary

- **Inheritance** is a key feature of object-oriented design, enabling modularity, hierarchy, and code reuse.
- Subclasses inherit traits from superclasses but can add or specialise behaviours.
- Java's class hierarchy, including `Object`, `Set`, and `List`, showcases the practical use of inheritance in the language itself.
