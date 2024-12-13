# Protected access

## Problem Overview
In the `Network Version 2` program:
- A news feed is created with posts (message posts and photo posts).
- Posts display data, but not in the desired order.
- The `toString` method in subclasses calls the superclass (`super.toString`), but only provides limited options to format the output.
- Desired order:
  - **Username** at the top.
  - **Post-specific information** (e.g., message or photo caption).
  - Followed by **number of likes**, **timestamp**, and **comments**.

---

## Solution: Protected Methods
To fix this, protected access is introduced:
- **Purpose**: Allow subclasses to access private fields while keeping them hidden from external classes.

### Steps Taken

### 1. Add Protected Getter Methods in `Post`
- Allow subclasses (`MessagePost`, `PhotoPost`) to access data without exposing fields externally.

#### Example Protected Methods

```java
protected String getUsername() { return username; }
protected String getMetadata() { return "Likes: " + likes + ", Comments: " + comments.size(); }
protected String timeString() { return "Posted: " + timestamp.toString(); }
```

---

### 2. Refactor `MessagePost` and `PhotoPost`
- Replace `super.toString()` calls with formatted data using protected methods.

#### Updated `toString` in `MessagePost`

```java
@Override public String toString() {
    String result = getUsername() + "\n"; 
    result += timeString() + "\n"; 
    result += "Message: " + message + "\n"; 
    result += getMetadata(); return result; 
}
```

#### Updated `toString` in `PhotoPost`

```java
@Override public String toString() {
    String result = getUsername() + "\n"; 
    result += timeString() + "\n"; 
    result += "File: " + fileName + "\n"; 
    result += "Caption: " + caption + "\n"; 
    result += getMetadata(); return result; 
}
```

---

## Testing the Solution

### Test Setup
1. Create a `NewsFeed` object.
2. Add a `MessagePost` and `PhotoPost` to the news feed:
    ```java
    MessagePost m1 = new MessagePost("Alice", "Hello world"); 
    PhotoPost p1 = new PhotoPost("Bob", "photo.jpg", "A caption");

    newsFeed.addPost(m1); newsFeed.addPost(p1);
    ```
3. Display the news feed:
    ```java
    newsFeed.show();
    ```
    

### Output

```
Alice 36 seconds ago Message: Hello world Likes: 0, Comments: 0

Bob 24 seconds ago File: photo.jpg Caption: A caption Likes: 0, Comments: 0
```

---

## Key Takeaways

### Benefits of `protected` Methods
- **Encapsulation**: Keeps fields private while exposing controlled access to subclasses.
- **Flexibility**: Allows subclasses to format and structure data independently.
- **Reuse**: Common logic is centralized in the superclass.

### Example Use Cases
- Subclass-specific formatting of parent class data.
- Restricting data access to specific packages or class hierarchies.

---

## Summary
- **Problem**: Data displayed in an undesired format.
- **Solution**:
  - Added protected methods (`getUsername`, `getMetadata`, `timeString`).
  - Subclasses used these methods to reorder and display data.
- **Outcome**: Posts display the desired information order with better encapsulation.
