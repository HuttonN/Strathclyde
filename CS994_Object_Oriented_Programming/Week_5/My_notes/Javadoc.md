# Javadoc

In this video, we explore **Java documentation (Javadoc)** and **code completion** features in BlueJ. These tools are essential for creating well-documented, maintainable, and easy-to-understand code.

---

## Introduction to Javadoc

- **Purpose**: Javadoc helps you document your classes and methods inline with the code, making it easier to understand for others and your future self.
- **Why it’s important**:
  - Enables others to understand how to use your classes and methods.
  - Reduces the need to revisit the implementation details when you return to your code after some time.

---

## Example Project: Zuul Better Program

### Existing Documentation
- The `@author` and `@version` tags are part of Javadoc and contribute to the generated documentation.
- BlueJ automatically includes this information in the documentation.

### Generating Documentation
1. Open the project folder.
2. Delete any existing `doc` folder for demonstration purposes.
3. In BlueJ, click on `Tools > Project Documentation`.
   - BlueJ generates a `doc` folder containing HTML files.
   - Open `index.html` to view the documentation in a browser.
   - The documentation includes:
     - Class name, version, and author.
     - Constructor details.
     - Method summaries and details.

---

## Writing Effective Javadoc Comments

### Class-Level Comments
Include:
- **Class name**.
- **Description** of the class's purpose.
- **Version number**.
- **Author name**.

Example:

```java
/**
 * This class represents a basic game in the Zuul project.
 * @author John Doe
 * @version 1.0
 */
public class Game {
    ...
}
```

### Method-Level Comments
For each method, include:
- **Brief description** of its functionality.
- **Parameters** using `@param`.
- **Return type** using `@return`.

Example:

```java
/**
 * Starts the game and processes user commands.
 * @param command The initial command from the user.
 * @return A string indicating the game state.
 */
public String play(String command) {
    ...
}
```

---

## Best Practices for Documentation

- Use the `@` symbols correctly (e.g., `@param`, `@return`).
- Write concise, clear, and accurate descriptions.
- Avoid leaving undocumented classes or methods.

---

## Encapsulation and Information Hiding

### Principles
- **Encapsulation**: Keep data private within a class and provide controlled access through public methods.
- **Information Hiding**:
  - Make fields private whenever possible.
  - Expose only necessary methods via the public interface.

### Benefits
- Promotes **loose coupling** between classes.
- Reduces interdependencies, improving maintainability.

---

## Code Completion in BlueJ

### Features
- **Code completion** (also called autocomplete):
  - Suggests available methods and fields.
  - Works for both Java's built-in classes and your project classes.

### How to Use
1. Start typing a variable or method name.
2. Press **Ctrl + Space** to bring up suggestions.
   - Methods from the variable's class appear.
   - Methods from the current project also appear if relevant.
3. Select the desired method or field to insert it into your code.

### Example

```java
String s = "example";
s. // Press Ctrl + Space to see available methods like substring, length, etc.
```

For your project classes:

```java
Game game = new Game();
game. // Press Ctrl + Space to see methods like play.
```

---

## Summary

- **Javadoc**:
  - Simplifies documentation and creates an API-like view for your classes.
  - Improves collaboration and maintenance.
- **Encapsulation**:
  - Protects data and reduces dependencies between classes.
- **Code Completion**:
  - Increases coding efficiency by suggesting available methods and fields.

### Final Advice
- Document all classes and methods thoroughly.
- Use encapsulation to design robust and maintainable software.
- Leverage code completion to explore available methods and write code faster.

Explore the exercises in Chapter 6 for hands-on practice with Javadoc and code completion features.

---
