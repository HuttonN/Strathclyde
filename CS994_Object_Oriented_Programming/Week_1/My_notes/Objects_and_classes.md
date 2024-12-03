# Objects and Classes

In this section, we will look at two fundamental concepts of object-oriented programming:  
* objects  
* classes  

We will also explore how they interact and how they form the foundation for writing programs in object-oriented languages.

## Objects

Objects represent individual entities within a program, modeling elements from the problem domain. They are central to object-oriented programming, allowing us to encapsulate both data and behavior. 

### Examples of Objects

Objects vary based on the application domain:
- **Word processor**: Words, sentences, paragraphs.
- **Video game**: Characters, enemies, or levels.
- **Music app**: Tracks, albums, artists.

### Attributes and State

Every object has:
- **Attributes**: Characteristics of the object (e.g., color, size).
- **State**: The current values of the object's attributes.  

Example:
- A `Circle` object might have:
  - `xPosition: 10`
  - `yPosition: 15`
  - `diameter: 30`
  - `color: "red"`

### Behavior

Objects can perform actions defined by their methods. These methods enable objects to:
- Retrieve or modify their attributes.
- Interact with other objects.

#### Example

```java
circle1.makeVisible();      // Makes the circle visible.
circle1.moveHorizontal(50); // Moves the circle 50 units to the right.
circle1.changeColor("blue"); // Changes the circle's color to blue.
```

## Classes

Classes are templates or blueprints used to create objects. They define:
- The structure (fields/attributes) of the objects.
- The behavior (methods) that the objects can perform.

### Example: The `Car` Class

A `Car` class may define:
- **Attributes**:
  - `color`
  - `engineSize`
  - `fuelType`
- **Methods**:
  - `startEngine()`
  - `drive(int distance)`
  - `refuel(int amount)`

### Creating Instances

Objects are created from classes. An instance of a class is a specific object with its own state.  

Example:
```java
Car myCar = new Car(); // Creates a new instance of the Car class.
myCar.color = "red";
myCar.startEngine();
```

In BlueJ, this involves right-clicking a class (e.g., Circle) and selecting new Circle() to create an object. Each object is then displayed on the Object Bench.

### Methods

Methods define the actions objects can perform. They may:
* Return information about the object.
* Change the object's state.
* Interact with other objects.

### Parameters

Methods often require additional information to execute, provided as parameters. Each parameter has:

* A type (e.g., ```int```, ```String```).
* A name describing its purpose.

#### Example

```java
void setColor(String color); // Changes the object's color.
```

To invoke this method:

```java
circle1.setColor("green");
```

### Multiple Instances

A single class can create multiple objects, each with a unique state.

Example:
* ```circle1: color = "red", diameter = 20.```
* ```circle2: color = "blue", diameter = 30.```

These objects are independent and can have their own attributes while sharing the same methods.

### State

The state of an object consists of all its attributes and their values at a given moment. Changes to an object’s attributes through methods modify its state.

Example:
```java
circle1.moveHorizontal(10); // Changes xPosition, altering the state.
```

In BlueJ, the state of an object can be inspected by using the Inspect function, which displays the current values of its fields.

## Summary

Objects and classes form the foundation of object-oriented programming:
* Objects encapsulate state (data) and behavior (methods).
* Classes serve as templates for creating objects.
* Methods allow interaction with and between objects.
* Objects can have unique states, even when created from the same class.