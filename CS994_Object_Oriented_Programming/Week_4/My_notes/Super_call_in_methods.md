# Super call in methods

In this video, we explore how to call **super methods** within our classes using the **Network version 2** project in Blue Jay.

---

## Current Problem

- We have **dynamic types** (`MessagePost` and `PhotoPost`) that override the `display` method.
- When calling `show` in `NewsFeed`, only information from the dynamic types is displayed.
- Missing information from the **static type** (`Post`).

---

## Solution: Using `super` to Access Superclass Methods

### Step 1: Modify `MessagePost`

- Use the `super` keyword to call the superclass `display` method:

```java
public void display() {
    super.display();
    System.out.println("Message: " + message);
}
```

### Step 2: Modify `PhotoPost`

- Similarly, use `super` in the `display` method:

```java
public void display() {
    super.display();
    System.out.println("Filename: " + filename);
    System.out.println("Caption: " + caption);
}
```

---

## Testing the Changes

### Steps

1. Create a `NewsFeed`.
2. Add a `MessagePost`:
   - Author: Alice
   - Message: "Hello World"
3. Add a `PhotoPost`:
   - Author: Bob
   - Filename: "photo.jpg"
   - Caption: "A photograph"
4. Call the `show` method.

### Output

- Alice's post displays:
  - Username
  - Timestamp
  - Number of likes
  - Comments
  - Message
- Bob's post displays:
  - Username
  - Timestamp
  - Number of likes
  - Comments
  - Filename
  - Caption

---

## Polymorphic Methods

### Key Concepts

- **Polymorphism**:
  - Both `Post` and its subclasses (`MessagePost` and `PhotoPost`) implement a `display` method.
  - Subclasses have two versions of the method available:
    - The superclass (`Post`) version.
    - The subclass (`MessagePost` or `PhotoPost`) version.
- Using `super` allows access to the **static type's** method.

---

## Conclusion

We can now display all the information from both the **static type** (`Post`) and the **dynamic types** (`MessagePost`, `PhotoPost`). While the formatting and order of the output need improvement, this is a solid start to utilizing polymorphic methods effectively.
