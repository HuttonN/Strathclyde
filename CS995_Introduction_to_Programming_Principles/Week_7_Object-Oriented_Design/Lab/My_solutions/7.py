"""7. Create three classes to match the UML diagram that is given in Figure 1.
• The Shape constructor should assign values to width, height and depth.
• area_hd() should return height × depth.
• area_wd() should return width × depth.
• area_wh() should return width × height.
• The area() for Rectangle should return the value of width × height.
• The volume() for Rectangle should return 0.
• The area() for RectangularPrism should return the value of:
2 × ( width × height + width × depth + height × depth )
• The volume() for RectangularPrism should return the value of:
width × height × depth
• Add __repr__(self) functions for the three classes.
• Create a program that uses the three classes."""

class Shape:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def area_hd(self):
        return self.height * self.depth
    
    def area_wd(self):
        return self.width * self.depth
    
    def area_wh(self):
        return self.width * self.height
    
    def __repr__(self):
        return f"Shape(width={self.width}, height={self.height}, depth={self.depth})"
    
class Rectangle(Shape):

    def area(self):
        return self.area_wd()
    
    def volume(self):
        return 0
    
class RectangularPrism(Shape):

    def area(self):
        return 2*(self.area_wh() * self.area_wd() * self.area_hd())
    
    def volume(self):
        return self.width * self.height * self.depth

    def __repr__(self):
        return f"RectangularPrism(width={self.width}, height={self.height}, depth={self.depth})"

# Example usage
shape = Shape(10, 20, 30)
rectangle = Rectangle(10, 20, 0)  # Depth is not relevant for a rectangle, so it can be set to 0
rect_prism = RectangularPrism(10, 20, 30)

# Displaying area and volume for each object
print(shape)  # Output: Shape(width=10, height=20, depth=30)
print(f"Rectangle area: {rectangle.area()}")  # Output: 200
print(f"Rectangle volume: {rectangle.volume()}")  # Output: 0
print(rectangle)  # Output: Rectangle(width=10, height=20)
print(f"Rectangular Prism area: {rect_prism.area()}")  # Output: 2200
print(f"Rectangular Prism volume: {rect_prism.volume()}")  # Output: 6000
print(rect_prism)  # Output: RectangularPrism(width=10, height=20, depth=30)