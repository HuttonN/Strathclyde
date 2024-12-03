# Object Interaction

In this video, we're exploring how objects in Java interact with each other using the BlueJ environment. We will examine Java source code and its relationship with object interactions.

---

## Setting Up BlueJ

1. Open the **Figures** package in BlueJ.
2. Enable the **Terminal Window**:
   - Navigate to the `View` menu and select `Show Terminal`.
   - Enable the **Record Method Calls** option.

---

## Creating and Interacting with Objects

### Example: Creating a `Person` Object
1. **Create an Instance of `Person`**:
   - Right-click on the `Person` class and select `New Person`.
   - Name the object `Person1`.

2. **Observe the Terminal Output**:
   - The terminal window displays the corresponding Java code:
     ```java
     Person Person1 = new Person();
     ```
   - This is the Java code for creating an instance of the `Person` class.

3. **Calling Methods**:
   - Call methods on `Person1`, such as `moveLeft()` and `moveUp()`.
   - The terminal window shows:
     ```java
     Person1.moveLeft();
     ```
     - This indicates that the `moveLeft` method is called on the `Person` object.
     - The parentheses `()` show that the method does not take parameters.

---

## Switching to a New Project

1. **Open the `House` Project**:
   - Close the `Figures` project and open the `House` project.
   - Ensure the **Terminal Window** is open and **Record Method Calls** is enabled.

2. **Compile Classes**:
   - Classes initially appear with striped lines, indicating they are not compiled.
   - Compile the classes before creating instances.

3. **Create a `Picture` Object**:
   - Create an instance of the `Picture` class and name it `Picture1`.
   - The terminal shows the corresponding Java code:
     ```java
     Picture Picture1 = new Picture();
     ```

---

## Calling Methods on the `Picture` Object

### Example: Drawing the Picture
1. Call the `draw` method on `Picture1`:
   - This draws a house, similar to the exercise in section 1.19 of the textbook.

2. **Class Dependencies**:
   - The `Picture` class relies on other classes, such as:
     - `Circle`
     - `Square`
     - `Triangle`

---

## Exploring the Java Code for the `Picture` Class

1. **Open the Editor**:
   - Right-click on the `Picture` class and select `Open Editor`.

2. **Class Structure**:
   - The class begins with:
     ```java
     public class Picture {
     ```
   - An opening curly brace `{` indicates the start of the class.

3. **Attributes of the `Picture` Class**:
   - The class contains:
     - A `Square` for the wall.
     - A `Square` for the window.
     - A `Triangle` for the roof.
     - A `Circle` for the sun.
     - A boolean attribute to indicate if the picture is drawn.

4. **Constructor**:
   - The constructor initializes the shapes:
     ```java
     public Picture() {
         wall = new Square();
         window = new Square();
         roof = new Triangle();
         sun = new Circle();
     }
     ```

5. **Draw Method**:
   - The `draw` method calls methods on these objects to:
     - Move them to the correct position.
     - Set their size and colour.
     - Make them visible.
   - Example:
     ```java
     wall.moveHorizontal(-50);
     wall.changeSize(120);
     wall.makeVisible();
     ```

---

## Summary

- The **Terminal Window** in BlueJ records method calls, showing the corresponding Java code.
- Objects interact by calling methods on each other.
- The `Picture` class demonstrates object composition, where multiple shapes (circle, square, triangle) form a complete object.
- Methods such as `draw` manipulate these objects to create a complete picture.

---

This concludes the video on object interaction.