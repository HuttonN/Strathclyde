# Inheritance in Java

In this video, we explore how inheritance has been implemented in the **Network Version 2** project using Blue Jay. This approach improves code organization and reduces duplication by encapsulating shared behavior and data in a superclass.

---

## Key Concepts of Inheritance

1. **Hierarchical Structure**:
   - `MessagePost` and `PhotoPost` extend `Post`.
   - This implies that both `MessagePost` and `PhotoPost` **inherit** the behavior and attributes of the `Post` superclass.
   - Think of it as an "is-a" relationship:
     - `MessagePost` **is a** `Post`.
     - `PhotoPost` **is a** `Post`.

2. **Simplified NewsFeed**:
   - NewsFeed now uses a **single list** of `Post` objects.
   - Methods such as `addPost(Post post)` and `show()` operate on the shared `Post` type, simplifying the design.
   - Adding posts and displaying them does not require separate handling for different post types.

---

## Code Structure and Inheritance

### The `Post` Superclass
The `Post` superclass encapsulates all shared data and functionality:

#### Shared Fields:
- `username` (Author of the post)
- `timestamp` (Time of creation)
- `likes` (Number of likes)
- `comments` (List of comments)

#### Shared Methods:
- `like()` and `unlike()`: To increment or decrement the number of likes.
- `addComment(String comment)`: To add a comment to the list.
- `getTimestamp()`: To retrieve the timestamp.
- `display()`: To print common post details (likes, comments, etc.).

### Subclasses: `MessagePost` and `PhotoPost`
Each subclass handles unique data and behavior:

#### `MessagePost`:
- Field: `message` (The text content of the post).
- Method: `getMessage()` (Returns the message).

#### `PhotoPost`:
- Fields:
  - `fileName` (The name of the photo file).
  - `caption` (Caption for the photo).
- Methods:
  - `getFileName()`
  - `getCaption()`

### Constructor Inheritance with `super`
When constructing a subclass object, the superclass constructor is called using the `super` keyword:

#### `MessagePost` Constructor:
```java
public MessagePost(String author, String text) {
    super(author); // Calls the Post constructor to set username, timestamp, likes, and comments.
    this.message = text;
}
```

#### `PhotoPost` Constructor:

```java
public PhotoPost(String author, String fileName, String caption) { 
    super(author); // Calls the Post constructor to set username, timestamp, likes, and comments. 
    this.fileName = fileName; 
    this.caption = caption; 
}
```

---

## Advantages of Inheritance in Network Version 2

1. **Code Reusability**:
   - Shared functionality and data are implemented in one place (`Post`), avoiding duplication.

2. **Simpler NewsFeed**:
   - A single list of `Post` objects simplifies operations like adding posts and displaying them.

3. **Extensibility**:
   - Adding new post types (e.g., `VideoPost`) is straightforward. The `NewsFeed` class does not need any changes as long as the new type extends `Post`.

4. **Cleaner Subclasses**:
   - `MessagePost` and `PhotoPost` focus only on their unique aspects, making them easier to understand and maintain.

---

## Example Usage

1. **Creating a NewsFeed**:
```java
NewsFeed newsFeed = new NewsFeed();
```

2. **Adding Posts**:

```java
MessagePost messagePost = new MessagePost("Alice", "Hello world!"); PhotoPost photoPost = new PhotoPost("Bob", "photo.jpg", "A beautiful sunset");

newsFeed.addPost(messagePost); 
newsFeed.addPost(photoPost);
```

3. **Displaying Posts**:
```java
newsFeed.show();
```

Output:

```
Alice 45 seconds ago Comments: None Hello world!

Bob 23 seconds ago Comments: None File: photo.jpg Caption: A beautiful sunset
```

---

## Conclusion

Inheritance in Network Version 2 organizes shared functionality into the `Post` superclass while allowing specific behavior for `MessagePost` and `PhotoPost` through subclassing. This simplifies code maintenance and makes it easy to extend the system with new post types.
