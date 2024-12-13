# Static types and dynamic types

In this video, we explore the concepts of static and dynamic types using the **Network version 2** project in Blue Jay.

---

## Inheritance Structure

### Post Class (Static Type)

- **`Post`** is the superclass.
- It contains all the shared information and methods among all posts:
  - Username
  - Timestamp
  - Number of likes
  - Comments

### Subclasses (Dynamic Types)

- **`MessagePost`**: Encapsulates data specific to messages, like the `message` field.
- **`PhotoPost`**: Encapsulates data specific to photos, like `filename` and `caption`.

---

## Static and Dynamic Types

### Static Type

- The **static type** refers to the declared type of a variable at compile time.
- In this example, `Post` is the static type.
- It holds shared information and methods that won't change.

### Dynamic Type

- The **dynamic type** refers to the actual object that a variable points to at runtime.
- In this example, `MessagePost` and `PhotoPost` are dynamic types.
- Subclasses are considered dynamic because they can change and extend the base functionality of the superclass.

---

## Example in the NewsFeed Class

### Iterating Over Posts

- The **`NewsFeed`** class has a collection of `Post` objects.
- When calling the `show` method:

```java
for (Post post : posts) {
    post.display();
}
```

The `display` method from `Post` is called for each object in the collection.

---

## Limitation of the Static Type

### Post's `display` Method

- The **`Post`** class only knows about its own fields:
  - Username
  - Timestamp
  - Number of likes
  - Comments
- It cannot display information specific to `MessagePost` (e.g., `message`) or `PhotoPost` (e.g., `filename` and `caption`).

### Why?

- The **static type** (`Post`) does not know at compile time which subclass (dynamic type) will instantiate it.
- As a result, it can only access its own fields and methods.

---

## Conclusion

This distinction between static and dynamic types illustrates a trade-off in inheritance:
- The static type provides shared functionality and structure.
- The dynamic type enables flexibility and specific behavior, but it requires additional handling when accessing subclass-specific fields or methods.
