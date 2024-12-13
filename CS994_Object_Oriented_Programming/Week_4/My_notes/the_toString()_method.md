# Object Methods: `toString` in Java

## Overview
- All objects in Java implicitly extend the universal superclass `Object`.
- The `Object` class provides several default methods, including:
  - `toString`: Returns a textual representation of an object.
- Overriding `toString` makes objects provide meaningful string representations.

---

## Applying `toString` in the Network Version 2 Project

### Current Implementation
1. **Default `toString`**:
   - The default `toString` method returns:
     - Class name.
     - An `@` symbol.
     - A hexadecimal representation of the object's memory location.
   - Example Output:
     ```
     MessagePost@6d06d69c
     PhotoPost@7852e922
     ```

2. **Desired Implementation**:
   - Override `toString` to return meaningful details about the object.
   - Example Output:
     ```
     Alice: Hello World (22 seconds ago)
     No comments.
     ```

---

## Refactoring the Code

### Steps to Override `toString`

1. **Modify the `Post` Class**:
   - Override the `toString` method to provide a meaningful textual representation of a `Post`.
   - Implementation:
     ```java
     @Override
     public String toString() {
         String result = username + "\n";
         result += timestamp + "\n";
         result += "Comments:\n";
         for (String comment : comments) {
             result += comment + "\n";
         }
         return result;
     }
     ```

2. **Modify Subclasses (`MessagePost` and `PhotoPost`)**:
   - Extend the `toString` method to include additional details specific to subclasses.
   - Implementation:
     - `MessagePost`:
       ```java
       @Override
       public String toString() {
           return super.toString() + message;
       }
       ```
     - `PhotoPost`:
       ```java
       @Override
       public String toString() {
           return super.toString() + "Photo: " + filename + "\nCaption: " + caption;
       }
       ```

---

### Updating the `NewsFeed` Class
- Replace calls to `display` with calls to `toString` for each `Post` object.
- Implementation:
    ```java
    public void show() { for (Post post : posts) { System.out.println(post); } }
    ```

---

## Testing the Changes

### Creating and Displaying Posts
1. **Setup**:
    ```java
    NewsFeed newsFeed = new NewsFeed(); 
    MessagePost m1 = new MessagePost("Alice", "Hello World"); 
    PhotoPost p1 = new PhotoPost("Bob", "photo.jpg", "A beautiful sunset"); 
    newsFeed.addMessagePost(m1); 
    newsFeed.addPhotoPost(p1);
    ```

2. **Display Output**:
- Before overriding `toString`:
  ```
  MessagePost@6d06d69c
  PhotoPost@7852e922
  ```
- After overriding `toString`:
  ```
  Alice: Hello World (22 seconds ago)
  No comments.

  Bob: (11 seconds ago)
  Photo: photo.jpg
  Caption: A beautiful sunset
  No comments.
  ```

---

## Key Notes

### `System.out.println` and Objects
- The `System.out.println` method automatically calls `toString` on non-string objects.
- Explicitly calling `toString` is unnecessary:
    ```java
    System.out.println(post); // Automatically calls post.toString()
    ```

### Refactoring with Confidence
- Refactor code iteratively and test thoroughly.
- Ensure no functionality changes during refactoring.

---

## Summary
- Overriding the `toString` method provides meaningful textual representations of objects.
- Refactoring existing methods to leverage `toString` improves code clarity and maintainability.
- The `System.out.println` method seamlessly integrates with overridden `toString` methods for clean output.

