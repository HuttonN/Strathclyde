# Adding other post types to the network project

In this video, we explore how to extend the **Network Version 2** project in Blue Jay by adding a new post type, `EventPost`. This process demonstrates the power of inheritance and how reusable code in the `Post` superclass simplifies adding new functionality.

---

## Current Structure of the Network Project

- The `NewsFeed` class maintains a collection of `Post` objects.
- Two existing implementations of `Post`:
  - `MessagePost`
  - `PhotoPost`

---

## Adding a New Post Type: `EventPost`

We will create a new post type called `EventPost` that inherits from the `Post` superclass.

### Steps to Create `EventPost`

1. **Create the Class**:
   - In Blue Jay, right-click and create a new class named `EventPost`.

2. **Extend `Post`**:
   - Add the `extends Post` declaration to inherit all fields and methods from `Post`.

3. **Add a New Field**:
   - Introduce a field to store the event type.

4. **Constructor**:
   - Define a constructor that initializes the event type and calls the `Post` constructor to set the author.

5. **Accessor Method**:
   - Add a getter method to retrieve the event type.

---

### `EventPost` Code

```java
public class EventPost extends Post {
    private String eventType; // Field for the event type

    // Constructor
    public EventPost(String author, String eventType) {
        super(author); // Call the superclass constructor to set the author
        this.eventType = eventType; // Set the event type
    }

    // Accessor method for event type
    public String getEventType() {
        return eventType;
    }
}
```

---

## Example Usage

1. **Create a NewsFeed**:

```java
NewsFeed newsFeed = new NewsFeed();
```

2. **Create an EventPost**:

```java
EventPost eventPost = new EventPost("Alice", "Party");
```

3. **Add the EventPost to the NewsFeed**:

```java
newsFeed.addPost(eventPost);
```

4. **Show Posts**:

```java
newsFeed.show();
```

**Output**:
```
Alice 13 seconds ago
Comments: None
```

---

## Key Observations

1. **No Changes to Existing Code**:
   - `Post` and `NewsFeed` required no modifications to support `EventPost`.

2. **Reusability**:
   - Most of the functionality (e.g., handling likes, comments, and timestamps) is inherited from `Post`.

3. **Ease of Extension**:
   - Adding new post types, such as `EventPost`, is straightforward. Only unique aspects of the post type (e.g., event type) need to be implemented.

4. **Subclass-Specific Data**:
   - While `EventPost` inherits shared functionality, additional subclass-specific information (e.g., event type) is managed independently.

---

## Conclusion

By leveraging inheritance, we easily extended the functionality of the Network Version 2 project to include a new `EventPost` type. This demonstrates how well-structured code promotes reuse and simplifies adding new features.