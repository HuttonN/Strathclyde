# Inheritance hierarchies

In this video, we explore **inheritance hierarchies** in object-oriented programming.

---

## Superclasses and Subclasses

- In Java, a **subclass** may only inherit from a single **superclass**.
- However, a **superclass** can have **multiple subclasses**.

---

## Example Hierarchy: Progression

Here's an example of a simple hierarchy:

1. **Superclass**: `Progression`
   - Represents numeric progressions.
2. **Subclasses**:
   - **Arithmetic Progression**: Determines the next number by adding a fixed constant.
   - **Geometric Progression**: Determines the next number by multiplying the previous value.
   - **Fibonacci Progression**: Determines the next number using the Fibonacci formula.

Each subclass inherits from the superclass and modifies the progression logic in a unique way.

---

## Code Example: `Progression` Class

The `Progression` class serves as the **base class**:

- **Instance Variable**:
  - `protected long current`: Represents the current value of the progression.

- **Method**:
  - `nextValue()`: Determines the next value in the progression.

---

## Code Example: `ArithmeticProgression` Subclass

The `ArithmeticProgression` class demonstrates inheritance and augmentation:

- **Constructor**:
  - Accepts two `long` parameters: `stepwise` and `start`.
  - Calls the superclass constructor using `super(start)` to inherit the `start` variable.

---

### Summary

- Inheritance hierarchies allow us to create specific subclasses that inherit general behaviour from a superclass.
- Each subclass can override or augment inherited methods to provide specific functionality.
- The example of `Progression` illustrates how subclasses like `ArithmeticProgression`, `GeometricProgression`, and `FibonacciProgression` share a common base while implementing distinct behaviours.
