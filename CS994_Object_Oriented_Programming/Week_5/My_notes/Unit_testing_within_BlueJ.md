# Unit Testing within BlueJ

In this video, we explore unit testing using BlueJ and the online shop project. We'll perform interactive testing using the BlueJ inspector and identify logical errors in the program.

---

## Interactive Testing with BlueJ

1. **Creating a Sales Item**
   - Use the BlueJ interface to create a sales item with a name and price.

   Example:

    ```
    Name: "Item1" 
    Price: 100
    ```
    
2. **Adding a Comment**
- Use the `addComment` method, which takes:
  - **Author**: A string representing the name of the person leaving the comment.
  - **Text**: A string for the comment text.
  - **Rating**: An integer between 1 and 5 (inclusive).

Example:

    ```
    Author: "Alice" 
    Text: "Liked it" 
    Rating: 4
    ```
    
- Result:
  - The method returns `true`, indicating the comment was successfully added.
  - Inspect the item to confirm that the comment is recorded.

**Inspector Output:**

```
Item1 Price: 100 
Comments: [Author: Alice, Text: Liked it, Rating: 4]
```

---

## Boundary Condition Testing

### Testing Invalid Ratings
- **Scenario**: Adding a comment with an invalid rating (e.g., 0, which is outside the range of 1 to 5).
- **Test Case**:

```
Author: "Bob" 
Text: "Hated it" 
Rating: 0
```

- **Observed Result**:
- The method returns `true`, indicating the comment was added successfully.
- Inspection reveals the comment was recorded, despite the rating being invalid.

**Inspector Output:**

```
Comments: - [Author: Alice, Text: Liked it, Rating: 4] - [Author: Bob, Text: Hated it, Rating: 0]
```

---

## Identifying the Logical Error

### Problem:
- The program does not validate the rating value in the `addComment` method or in the `Comment` class.
- There is no logic to ensure the rating is within the range of 1 to 5.

### Solution:
- Add validation logic in the `addComment` method to reject comments with ratings outside the valid range.

---

## Summary

- **Key Takeaways**:
- Unit testing revealed a logical error in the program.
- Interactive testing with the BlueJ inspector allowed us to identify the issue.
- Proper validation should be implemented in the program to prevent invalid data from being added.

This highlights the importance of boundary testing and thorough validation in software development.
