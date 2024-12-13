# Subtyping (part 3)

In this video, we explore situations where the rules of assigning subtypes to supertypes can be restrictive and how casting can help resolve such cases.

---

## Example Scenario

Consider the familiar inheritance hierarchy:

- **`Vehicle`** is the superclass.
- **`Car`** and **`Bicycle`** are subtypes of `Vehicle`.

---

## Assigning Subtypes to Supertypes

### Assigning a Car to a Vehicle

```java
Vehicle v;
Car c = new Car();
```

- We first declare a variable `v` of type `Vehicle`.
- Then, we declare and instantiate a variable `c` of type `Car`.
- Assigning `c` to `v` works perfectly:

```java
v = c;
```

- This is valid because `Car` is a subtype of `Vehicle`.
- The compiler is happy with this because `v` can refer to any object of type `Vehicle`, including its subtypes.

---

## Attempting to Assign a Supertype to a Subtype

### Problematic Assignment

```java
C = v; // Error
```

- Here, we try to assign the `Vehicle` variable `v` to the `Car` variable `c`.
- This creates an error because the compiler only sees that `v` is a `Vehicle` and doesn't know that `v` refers to a `Car`.

---

## Why This Seems Acceptable

### One Object, Two References

- In this case, `v` actually references the same `Car` object created earlier.
- Logically, assigning `v` to `c` should be fine because both variables refer to the same object.

### Compiler Limitations

- The compiler only knows the declared types (`Vehicle` for `v` and `Car` for `c`).
- It cannot determine that `v` is pointing to a `Car` object.

---

## Solution: Casting

### Explicit Casting

```java
C = (Car) v;
```

- Here, we explicitly cast `v` to type `Car` using `(Car)`.
- This tells the compiler: "Trust me, `v` is a `Car`."

### Risks of Casting

- If `v` does not actually reference a `Car` object, this will throw a runtime exception.
- Casting introduces potential errors, so it must be used carefully.

---

## Practical Applications

### Casting in Collections

- Sometimes, objects retrieved from collections (e.g., `ArrayList`) need to be cast to their specific types.
- For example, a collection of `Vehicle` objects might require casting individual elements to `Car` or `Bicycle` for specific operations.

---

## Best Practices

1. **Avoid Casting When Possible**:
   - Casting is error-prone and can lead to runtime exceptions.
2. **Use Polymorphism**:
   - Design methods and classes to work with supertypes, leveraging polymorphism to avoid explicit casting.
3. **Use Generics**:
   - In collections, generics can help ensure type safety and reduce the need for casting.

---

## Conclusion

Casting can resolve issues when assigning supertypes to subtypes, but it should be used sparingly. Instead, focus on designing flexible, type-safe code that minimizes the need for explicit type conversions.
