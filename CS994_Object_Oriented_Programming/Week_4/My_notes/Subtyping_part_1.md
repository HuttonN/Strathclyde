# Subtyping (part 1)

In this video, we explore how creating an inheritance hierarchy influences code design and simplifies the way we write and manage our programs. 

---

## Inheritance Hierarchy Overview

- **Structure**:
  - At the top, we have the `Post` superclass.
  - Below it are subtypes such as `CommentedPost`, `EventPost`, and others.
  - Each subtype inherits from its supertype.

- **Type Relationships**:
  - Higher levels in the hierarchy are **supertypes**.
  - Lower levels are **subtypes**.
  - Example:
    - `EventPost` is a **subtype** of `Post`.
    - `Post` is a **supertype** of `EventPost`.
    - `CommentedPost` is a **supertype** of `PhotoPost`, and `PhotoPost` is a **subtype** of both `CommentedPost` and `Post`.

---

## Implications of Subtypes and Supertypes

### Reusability of Subtypes
- **Subtypes can be used wherever supertypes are expected**.
  - For example, a `PhotoPost` can replace a `CommentedPost` since it inherits all its properties and methods.
  - Similarly, a `CommentedPost` can replace a `Post`.

### Simplified Methods
- **Previous Approach**:
  - Separate methods for different types of posts:
    ```java
    public void addMessagePost(MessagePost post) {
        // Add message post to the collection
    }
    
    public void addPhotoPost(PhotoPost post) {
        // Add photo post to the collection
    }
    ```

  - Separate methods had to be defined for each new post type.

- **Improved Approach**:
  - One generic method using the superclass `Post`:
    ```java
    public void addPost(Post post) {
        posts.add(post); // Add to ArrayList of Posts
    }
    ```
  - The `addPost` method accepts any object of type `Post` or its subtypes (e.g., `EventPost`, `PhotoPost`, etc.).

---

## How the `addPost` Method Works

### Key Details:
1. **Parameter of Type `Post`**:
   - The method takes a parameter of type `Post`.
   - This parameter can accept any object from the inheritance hierarchy (`Post` or any subtype).

2. **ArrayList of Posts**:
   - The collection is defined as `ArrayList<Post>`.
   - All objects added to this list are guaranteed to be either `Post` or one of its subtypes.

3. **Flexibility**:
   - Example usage:
     ```java
     addPost(new Post());
     addPost(new EventPost());
     addPost(new PhotoPost());
     ```
   - The method is indifferent to the specific type of post—it just adds it to the collection.

---

## Key Advantages

1. **Reduced Code Duplication**:
   - Only one method (`addPost`) is required instead of separate methods for each post type.

2. **Scalability**:
   - Adding new post types (e.g., `VideoPost`, `EventPost`) requires no changes to `addPost` or the collection.

3. **Flexibility**:
   - Any subtype can replace its supertype in method calls or collections.

---

## Conclusion

Using inheritance hierarchies simplifies code design by enabling reusability, reducing duplication, and providing flexibility. The `addPost` method is a prime example of how this approach leads to cleaner, more maintainable code. By leveraging the subtype-supertype relationship, we can write more generic and scalable methods, making it easier to extend functionality.
