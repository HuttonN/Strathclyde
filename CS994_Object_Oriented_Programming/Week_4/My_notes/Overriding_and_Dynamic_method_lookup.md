# Overriding & Dynamic method lookup

# Method Overriding and Dynamic Method Lookup

In this video, we explore method overriding and dynamic method lookup using the **Network version 2** project in Blue Jay.

---

## Overview

- The **`NewsFeed`** class contains a collection of `Post` objects.
- Subclasses `MessagePost` and `PhotoPost` encapsulate specific data for message and photo posts.

---

## Issue with Shared Information

### Scenario

1. Create a `NewsFeed`.
2. Add a `MessagePost`:
   - Author: Alice
   - Message: "Hello World"
3. Add a `PhotoPost`:
   - Author: Bob
   - Filename: "photo.jpg"
   - Caption: "A photograph"
4. Call the `show` method.

### Result

- Only shared information is displayed:
  - Username
  - Timestamp
  - Number of likes
  - Number of comments
- Specific details (e.g., the message or photo caption) are missing.

---

## Solution: Overriding the `display` Method

### Step 1: Modify `MessagePost`

- Add a `display` method to print the message:

```java
public void display() {
    System.out.println("Message: " + message);
}
```

### Step 2: Modify `PhotoPost`

- Add a `display` method to print the filename and caption:

```java
public void display() {
    System.out.println("Filename: " + filename);
    System.out.println("Caption: " + caption);
}
```

### Step 3: Use the `@Override` Annotation

- Helps ensure the method is correctly overriding the superclass method.
- Provides a runtime error if the method signature is incorrect.

---

## Testing the Changes

1. Create a `NewsFeed`.
2. Add a `MessagePost` and a `PhotoPost`.
3. Call the `show` method.

### New Result

- Posts now display details from their respective subclasses:
  - **`MessagePost`** displays the message.
  - **`PhotoPost`** displays the filename and caption.
- However, shared information from `Post` is not displayed.

---

## Explanation: Dynamic Method Lookup

### Key Points

- When calling `post.display()` on a `Post` object:
  - The overridden `display` method in the subclass (`MessagePost` or `PhotoPost`) is executed.
  - The `display` method in the superclass `Post` is ignored.

### Implications

- Static types (`Post`) do not know about dynamic types (`MessagePost`, `PhotoPost`).
- Dynamic types do know about their static type (`MessagePost` extends `Post`).

---

## Conclusion

Overriding methods in dynamic types improves functionality but still leaves gaps in displaying shared information. Future improvements can leverage the dynamic type's awareness of the static type for more comprehensive solutions.
