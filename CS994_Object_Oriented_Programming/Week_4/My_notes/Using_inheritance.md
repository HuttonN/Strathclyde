# Using inheritance

In this video, we explore how inheritance can improve the code structure in the Blue Jay Network Version 1 project. The current implementation contains duplicate code, which makes maintenance difficult. By using inheritance, we can centralize shared functionality and simplify the design.

---

## Observations in Current Code

### Common Fields
Both `MessagePost` and `PhotoPost` share these fields:
- `username`
- `timestamp`
- `number of likes`
- `collection of comments`

### Common Methods
Identical methods in both classes include:
- `like()`
- `unlike()`
- `addComment(String comment)`
- `getTimestamp()`

### Duplicate Logic in Display
The `display()` methods in both classes:
- Share logic for printing likes and comments.
- Differ only in how they handle post-specific details like the message or photo.

---

## Problems with Duplicate Code

1. **Maintenance Complexity**:
   - Changes to shared logic (e.g., `display()`) require updates in multiple places.
   
2. **Scalability Issues**:
   - Adding new post types (e.g., `VideoPost`, `EventPost`) involves creating new collections and methods in `NewsFeed`.

---

## Solution: Using Inheritance

### Introducing a `Post` Superclass
We create a `Post` superclass to encapsulate shared fields and methods.

#### Shared Data:
- Fields like `username`, `timestamp`, `likes`, and `comments` are moved to `Post`.

#### Shared Methods:
- Methods such as `like()`, `unlike()`, `addComment()`, and `getTimestamp()` are implemented in `Post`.

### Benefits
1. **Code Reuse**:
   - Common functionality resides in one place, reducing duplication.

2. **Simplified Maintenance**:
   - Changes to shared functionality only need to be made in the `Post` superclass.

3. **Scalability**:
   - Adding new post types (e.g., `VideoPost`) becomes easier. `NewsFeed` doesn't require changes to accommodate new types.

---

## Refactoring NewsFeed

### Current Implementation
- Two separate collections: one for `MessagePost` and one for `PhotoPost`.
- Separate methods for adding each post type.

### Refactored Implementation
1. **Single Collection**:
   - Use one collection to store all posts (`List<Post>`).

2. **Unified Methods**:
   - A single `addPost(Post post)` method, regardless of post type.

3. **Simplified Display**:
   - Iterate over the single collection in `show()` to display all posts.

---

## Future Improvements

By introducing inheritance:
- **Adding New Post Types**: For example, `VideoPost` or `EventPost` can extend `Post`. The `NewsFeed` class remains unchanged.
- **Centralized Logic**: Shared logic like displaying likes or comments is written once in the `Post` superclass.

---

## Conclusion

Inheritance is a powerful tool for eliminating duplicate code and improving scalability. In this project, it simplifies the `NewsFeed` design and reduces redundancy across `MessagePost` and `PhotoPost`. This makes the code easier to maintain and extend in the future.
