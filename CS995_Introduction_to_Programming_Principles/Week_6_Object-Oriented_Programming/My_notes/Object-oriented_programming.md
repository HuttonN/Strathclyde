# Object-Oriented Programming (OOP) in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. Objects are instances of classes, which serve as blueprints for creating objects. OOP allows for better organization of code by grouping data (attributes) and behavior (methods) into reusable components.

Key concepts introduced in this lecture:

1. **Classes and Objects:** Classes define the structure, while objects are instances of these classes.
1. **Constructors:** Special methods to initialize objects.
1. **Data Members:** Variables associated with objects.
1. **Inheritance:** Sharing functionality between related classes.

## Classes and Objects

### Defining a Class

In Python, a class is defined using the class keyword. The syntax is:

```python
class ClassName:
    def __init__(self, parameters):
        self.attribute = value
```

* **PascalCase** is used for naming classes (e.g., ```MyClass```).
* Use **snake_case** for variables and methods.

#### Example: A Simple Class

```python
class Car: 
    def init(self, make, model): 
        self.make = make 
        self.model = model

    def description(self):
        return f"{self.make} {self.model}"
```

### The `__init__` Method (Constructor)

A constructor is a function which is called when you want an instance of a class. The ```__init__``` method in Python is used to initialize an object's state when it's created. Other programming languages use more conventional names for constructors, but Python uses ```__init__```. Another 'odd' thing about Python is that we can only define one constructor. If you want different inputs then what you can do is assign default values.

```python
class Person: 
    def init(self, name="Unknown", age=0): 
        self.name = name 
        self.age = age
```

#### Usage of `self`

* The `self` keyword is a reference to the current instance of the class. It allows us to access the object’s attributes and methods within the class.
* `self` is required as the first parameter in any method that belongs to a class.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
When creating a ```Person``` object, ```self.name``` and ```self.age``` refer to attributes that belong to the specific instance of ```Person```. 

Example:

```python
p = Person("John", 30) 
print(p.name) # Output: John
```

### Attributes and Methods

* **Attributes:** Also known as data members, these are variables that belong to an object.
* **Methods:** Functions that belong to a class and act on the object’s attributes.

#### Example: Class with Data Member and Method
```python
class Rectangle: 
    def init(self, width, height): 
        self.width = width 
        self.height = height

    def area(self):
        return self.width * self.height

```

Usage:

```python
rect = Rectangle(5, 10) 
print(rect.area()) # Output: 50
```

### Objects and Data Members

When you create an object, a block of memory is allocated for it:

* **Object reference** points to the start of the memory block.
* **Data members** are offsets within the memory block, defined by their types.

Example:

```python
class MyClass:
    def __init__(self):
        self.x = 10  # Data member

my_object = MyClass()  # Create object
print(my_object.x)     # Access and print data member
```

![objects in memory](images/objects_and_memory.png)

### Member Functions

A class can also include member functions that operate on its data members.

Example:

```python
class MyClass:
    def __init__(self):
        self.name = "MyClass"

    def full_name(self):
        return self.name + " is an example"

m = MyClass()
m.name = "New name"
print("full_name = " + m.full_name())  # Output: New name is an example
```


### Data Classes

One type of class often used are Data Classes which hold mostly data with one or two member functions in there to return so-called transient values. E.g if given map coordinates you might have a function to return an angle.

Summary:
* Read/write to input/output
    * Often referred to as the "data model"
* Member functions to return transient data
    * Calculate simple features from stored values
    * e.g. angle from coordinates
* Limit functionality of member functions

Example:

```python
class Point: 
    def init(self, x, y): 
        self.x = x 
        self.y = y

    def distance_to_origin(self):
        return (self.x**2 + self.y**2)**0.5
```

### Algorithm Classes

Algorithm classes contain methods that perform operations. These typically work on data passed in as arguments rather than being stored as attributes.

Example:

```python
class MathUtils: 
    @staticmethod def factorial(n): 
        if n == 0: 
            return 1 
        return n * MathUtils.factorial(n - 1)
```

## Practical Considerations

### Public and Private Members

- **Public members:** Accessible from outside the class.
- **Private members:** Prefixed with `__` and cannot be accessed directly from outside the class.

Example:

```python
class MyClass: 
    def init(self): 
        self.public_var = "I am public"
        self.__private_var = "I am private"
```

### When Not to Use Classes

- If functionality doesn’t logically belong to an object or group, use standalone functions instead of forcing the use of a class.

Example:

```python
def is_even(n): 
    return n % 2 == 0
```

## Inheritance in OOP

### Concept of Inheritance

Inheritance allows a derived class or subclass to inherit the attributes and methods of a base class or superclass. This can avoid code duplication by reusing functionality from a base class.

### Superclass and Subclass

* **Superclass (Parent):** The class being inherited from.
* **Subclass (Child):** The class that inherits from the superclass.

#### Example

```python
class Animal: 
    def init(self, species): 
        self.species = species
    
    def sound(self):
        pass  # To be implemented by subclasses

class Dog(Animal): 
    def sound(self): 
        return "Woof"
```

### The `super()` Function

The ```super()``` function allows us to call methods from the superclass in the subclass, commonly used to call the superclass's constructor.

Example:

```python
class Shape:
    def __init__(self):
        self.sides = 0

class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.sides = 3

triangle = Triangle()
print("Triangle has", triangle.sides, "sides")
```

---

## Summary

- OOP provides a way to structure code around objects.
- **Key components:** Classes, objects, methods, inheritance, and data encapsulation.
- Use classes when they make logical sense for grouping related data and behavior.
