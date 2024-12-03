# Calling methods and String manipulation

In this video, we explore how to work with **String** objects in Java, including calling methods on these objects to manipulate and retrieve string data.

---

## Strings in the `Student` Class

- In the **Lab Classes** project, the `Student` class includes two fields of type **String**:
  - **`name`**: Represents the student's full name.
  - **`id`**: Represents the student's unique ID.

---

## Creating and Inspecting Strings

1. **Creating a String**:
   - Example:
     ```
     String s = "Phil";
     ```

2. **Inspecting a String**:
   - Using the **Code Pad** in BlueJ (accessible via the **View** menu), we can create and inspect a `String` object.
   - Dragging the string object into the **Inspector** shows the numerous methods available for manipulating strings.

---

## Common String Methods

### `length()`
- **Purpose**: Returns the number of characters in the string.
- **Example**:
    ```java
    s.length(); // Returns 4 for the string "Phil"
    ```

---

### `substring(int startIndex, int endIndex)`
- **Purpose**: Extracts a portion of a string based on the specified indices.
- **Details**:
- `startIndex`: The starting index (inclusive).
- `endIndex`: The ending index (exclusive).
- **Example**:
    ```java
    String name = "Philip"; 
    name.substring(0, 4); // Returns "Phil"
    ```

---

## Using String Methods in the `Student` Class

### `getLoginName` Method
- **Purpose**: Generates a login name by combining parts of the `name` and `id` fields.
- **Code**:
    ```java
    public String getLoginName() { 
        return name.substring(0, 4) + id.substring(0, 3); 
    }
    ```
- **How It Works**:
- Extracts the first 4 characters of the `name` field using `substring(0, 4)`.
- Extracts the first 3 characters of the `id` field using `substring(0, 3)`.
- Combines (concatenates) these two substrings using the `+` operator.

---

## Example Usage

1. **Creating a `Student` Object**:
 - Example:
   ```java
   Student student = new Student("Philip", "12345");
   ```

2. **Calling `getLoginName`**:
 - Example:
   ```java
   student.getLoginName(); // Returns "Phil123"
   ```

 - The result is:
   - The first 4 characters of "Philip" → `"Phil"`
   - The first 3 characters of "12345" → `"123"`
   - Combined result: `"Phil123"`

---

## Summary

- Strings are an essential data type in Java and include many built-in methods for manipulation and retrieval.
- Common methods include:
- `length()` to get the length of a string.
- `substring()` to extract portions of a string.
- String methods can be used in classes like `Student` to generate dynamic values, such as a login name.
- Java's string manipulation capabilities make it a versatile and powerful tool for handling text-based data.
 