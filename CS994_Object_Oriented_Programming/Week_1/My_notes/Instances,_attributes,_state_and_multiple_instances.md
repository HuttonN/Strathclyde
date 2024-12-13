# Instances, Attributes, State, and Multiple Instances

In this video, we're revisiting the BlueJ Figures project and focusing on:
- Method signatures
- How multiple instances of objects behave
- Attributes and the state of objects

---

## Method Signatures

When working with methods in the `Circle` class, the method signature provides details about:
1. **Return Type**:
   - Methods starting with the word `void` do not return any value.
2. **Method Name**:
   - Examples: `makeInvisible`, `moveHorizontal`, `changeColour`
3. **Parameters**:
   - Methods like `makeInvisible` have no parameters, indicated by empty parentheses `()`.
   - Some methods require parameters, which are enclosed in parentheses:
     - `moveHorizontal(int distance)` expects an integer value to indicate how far the object should move.
     - `changeColour(String colour)` expects a string value, such as `"red"` or `"yellow"`.

### Examples of Method Signatures

- **No Parameters**:
  ```java
  void makeInvisible()
    ```
- **With Parameters**:
  ```java
    void moveHorizontal(int distance)
    void changeColour(String colour)
    ```

## Creating Multiple Instances

We can create multiple instances of the same class, such as multiple `Circle` objects, and modify each instance independently.

### Example: Working with Multiple Circles

1. **Create Three Circles**:
   - Initially, the circles may overlap if their positions are identical.

2. **Move Each Circle to a Unique Position**:
   - Example: Move one circle left and another right.

3. **Change Their Attributes**:
   - Modify attributes such as colour.
   - **Valid Colours**:
     - `red`
     - `yellow`
     - `blue`
     - `green`
     - `magenta`
     - `black`

---

## Attributes and State

Each object has attributes that define its state, such as:
- **Position**: `xPosition` and `yPosition`
- **Size**: `diameter` (for circles)
- **Colour**
- **Visibility**: A boolean value (`true` for visible, `false` for invisible`)

### Using the Object Inspector in BlueJ

#### Inspecting an Object:
- Right-click an object and select `Inspect` to view its state.

**Example**:

diameter: 68 xPosition: 210 yPosition: 90 colour: blue visible: true


#### Changing State:
- Modify attributes using methods:
  - **Example**: `changeSize(100)` changes the circle's diameter to 100 pixels.
  - **Example**: `changeColour("yellow")` sets the circle's colour to yellow.
- Move the circle using methods such as:
  - `moveHorizontal(50)`
  - `moveVertical(-20)`

#### Visibility:
- An invisible object still exists but has its `visible` attribute set to `false`.

---

## Summary

- **Method Signatures**: Provide essential information about a method's return type, name, and required parameters.
- **Multiple Instances**: Multiple objects of the same class can coexist and behave independently, maintaining their own attributes and state.
- **Object State**: Attributes such as position, size, colour, and visibility define an object’s state and can be modified via methods or inspected using BlueJ’s object inspector.
- **Visibility**: Even invisible objects retain their state, with the `visible` attribute set to `false`.

---

Next: 
* [Chapter 1, Sections 1.5 to 1.8](Textbooks/Objects_First_with_Java/Chapter_1_Objects_and_Classes.pdf)
* [Object interaction](Object_interaction.md)