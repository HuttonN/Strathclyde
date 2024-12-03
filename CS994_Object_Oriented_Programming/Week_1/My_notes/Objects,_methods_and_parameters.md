# Objects, methods and parameters

In this video, we continue our exploration of BlueJ, focusing on how methods work with objects and instances. We will build on what we learned previously about classes and objects.

## Recap

In the previous session, we explored:
- BlueJ as a tool for visualizing classes and objects.
- The **Figures** project, which includes:
  - `Canvas`
  - `Circle`
  - `Square`
  - `Triangle`
  - `Person`

---

## Creating and Interacting with a `Circle` Object

### Step 1: Create an Instance of `Circle`
- In BlueJ, create a new instance of the `Circle` class. The object will appear on the **Object Bench** at the bottom of the screen.

### Step 2: Exploring Methods
- Methods allow us to interact with the object.
- Example methods in the `Circle` class include:
  - `makeVisible`
  - `makeInvisible`
  - Movement methods (e.g., `moveUp`, `moveRight`).

---

### Example Interactions

1. **Making the Circle Visible or Invisible**:
   - Call `makeVisible`:
     - The circle appears on the screen.
   - Call `makeInvisible`:
     - The circle disappears.

2. **Moving the Circle**:
   - Call `moveUp`:
     - The circle moves up.
   - Call `moveRight`:
     - The circle moves right.
     - Repeated calls continue moving the circle in the same direction.

3. **State Preservation**:
   - If the circle is made invisible and then visible again:
     - It reappears in the same position as when it was last visible.

4. **Calling Methods with Parameters**:
   - Call `moveHorizontal`:
     - A dialog box will prompt you for input (e.g., a distance value in pixels).
     - Input a value, such as `50`, and click OK.
     - The circle will move the specified number of pixels to the right.
   - This method is more flexible than `moveRight` or `moveLeft` because you can specify the exact distance to move.

---

## Key Concepts

### Methods
- Methods represent operations you can perform on an object.
- Using proper terminology, we say that a method is **called** or **invoked**.

### Parameters
- Some methods require **parameters**, which are additional values needed for the method to execute.
- Example:
  ```java
  void moveHorizontal(int distance)
    ```
    - ```int distance``` is the parameter
    - It specifies the distance (in pixels) to move the circle horizontally.

### Method Signature
- The method signature includes:
    - The method name (e.g., ```moveHorizontal```).
    - The parameter types (e.g., ```int distance```).
- Example:
    ```java
    void moveHorizontal(int distance)
    ```
    - **Name:** moveHorizontal
    - **Parameter Type:** int

---

## Summary

- **Methods** in BlueJ allow you to:
  - Change the state of an object (e.g., visibility).
  - Move objects in different directions.
  - Pass parameters to customize behavior (e.g., ```moveHorizontal``` with a specified distance).
- **Parameters** enhance method flexibility by allowing you to provide additional information. 
- **Key takeaway**: Objects retain their state (position, size, visibility) between method calls.

---

Next steps: Continue exploring additional methods and interactions to deepen your understanding of object behavior in BlueJ.
