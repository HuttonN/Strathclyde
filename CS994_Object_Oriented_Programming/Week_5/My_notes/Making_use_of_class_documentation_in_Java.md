# Making use of class documentation in Java

In this video note, we will explore the **documentation** and **code completion** features of the BlueJ environment using the Scribble project.

---

## Project Setup

- The original Scribble project includes a class called `DrawDemo` with examples of how to use the `Pen` and `Canvas` classes.
- For this video:
  - We use a modified version called **MyScribble**.
  - The `DrawDemo` class has been replaced with a new, minimal class.
- We will add code incrementally to illustrate BlueJ features.

---

## Adding a Pen Field

1. Add a `Pen` field to the class for drawing purposes.
2. Initialize the field in the constructor:
   - Open the `Pen` class source code to check its constructor:
     - The constructor takes no parameters.
```java
public class MyScribble {
    private Pen pen;

    public MyScribble() {
        pen = new Pen();
    }
}
```

3. Compile as usual.

---

## Drawing a Line

### First Steps
- Add a method to draw a line of a fixed length.
- Check the `Pen` class for an appropriate method:
  - Look for methods like `drawLine` or alternatives.

### Using the Documentation View
- Scrolling through the `Pen` class source code can be overwhelming.
- Switch to **Documentation View** in BlueJ:
  - Select `Tools > Toggle Documentation View` or use the documentation menu.
  - Provides a concise list of methods.
  - Observations:
    - The `move` method is suitable for drawing a line.
    - The class has multiple constructors.

### Writing the Method
```java
public void drawLine() {
    pen.move(100); // Moves the pen 100 units forward
}
```

- Compile and test to ensure it works.

---

## Drawing a Pentagon

### Method Definition
- Add a method to draw a pentagon.
- Take the length of the sides as a parameter.
```java
public void drawPentagon(int sideLength) {
    for (int i = 0; i < 5; i++) {
        pen.move(sideLength);
        pen.turn(360 / 5); // Turns 1/5th of a full circle
    }
}
```

### Code Completion
- Use **Ctrl + Space** after typing `pen.` to access a list of available methods.
  - Bold methods belong to the `Pen` class.
  - Start typing to narrow down the list.
  - Select the `turn` method and specify the degrees (360 / 5).

### Testing
- Compile and test the method.

---

## Refactoring for Clarity

### Observations
- The value `360 / 5` is cryptic and can be improved with a variable:

int angle = 360 / 5;

- The value `5` appears multiple times (representing the number of sides):
```java
int sides = 5;
int angle = 360 / sides;
```

### Updated Method

```java
public void drawPentagon(int sideLength) {
    int sides = 5;
    int angle = 360 / sides;
    for (int i = 0; i < sides; i++) {
        pen.move(sideLength);
        pen.turn(angle);
    }
}
```

- Compile and test to ensure correctness.

---

## Drawing Other Shapes

### Observations
- Changing the `sides` variable to `4` draws a square.
- Changing it to `3` draws a triangle.

### Generalizing the Method
- Remove the `sides` variable.
- Add a parameter to the method for the number of sides:

```java
public void drawPolygon(int sideLength, int sides) {
    int angle = 360 / sides;
    for (int i = 0; i < sides; i++) {
        pen.move(sideLength);
        pen.turn(angle);
    }
}
```

---

## Conclusion

- The **Documentation View** and **Code Completion** in BlueJ simplify library usage.
- Refactoring improves code clarity and flexibility.
- Exercises in the book will further enhance your understanding of generalizing methods for drawing polygons.
