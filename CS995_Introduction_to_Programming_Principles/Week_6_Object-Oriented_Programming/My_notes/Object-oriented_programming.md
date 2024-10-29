# Object-oriented programming

## Single data member

Python in an OOP language and so everything in Python is an object, with its properties and methods. A Class is like an object constructor, or "blueprint" for creating objects.

Lets study the following example:

```python
class MyClass:
    def __init__(self,name):
        self.name = name
```

Notes:

* In the PEP 8 coding style, the class name should be in Pascal case meaning that the first letter of each compound word is capitalized
* To create a class, the keyword ```class``` is used followed immediately by the name of the class
* A function that's part of a class is called a method
* The method ```__init__()``` is special and is run automatically when a new instance of a class is created. It is used to assign values to object properties, or other operations that are necessary when the object is created. It is called the contructor. In Python we can only define one constructor per class
* The ```self``` variable is a reference to the current instance of the class and is used to access variables that belong to the class

Having defined a class we can create instances of the class:

```python
m1 = MyClass("A new object")
m2 = MyClass("A new object")
```

When calling the class name (```MyClass``` in the above example) as a function it calls the constructor. 

Now we have 2 objects we can work with the data member (```name``` in this case):

```python
m1.name = "Updated name"
print("m1.name = " + m1.name)
print("m2.name = " + m2.name)
```

So, we've changed the name of m1. The output of the prints is as follows:

```python
m1.name = Updated name
m2.name = A new object
```

We can use the name because, by default, data members and member functions are public

## Objects and data members

When we 

## Single member function