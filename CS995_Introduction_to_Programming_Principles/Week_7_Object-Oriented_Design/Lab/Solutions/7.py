class Shape:
    """
    A class to represent a three-dimensional shape.
    """
    def __init__(self,
                 width: 0,
                 height: 0,
                 depth: 0):
        self.width = width
        self.height = height
        self.depth = depth

    def __repr__(self):
        s = f"Shape("
        s += f"width={self.width},"
        s += f"height={self.height},"
        s += f"depth={self.depth})"
        return s

    def area_wh(self):
        return self.width*self.height

    def area_wd(self):
        return self.width*self.depth

    def area_hd(self):
        return self.height*self.depth


class Rectangle(Shape):
    """
    A class to represent a rectangle.
    """
    def __init__(self, width, height):
        super().__init__(width, height, 0)

    def __repr__(self):
        s = f"Rectangle("
        s += f"width={self.width},"
        s += f"height={self.height})"
        return s

    def area(self):
        """
        A function to return the surface area.
        """
        return self.area_wh()

    def volume(self):
        """
        A function to return no volume.
        """
        return 0


class RectangularPrism(Shape):
    """
    A class to represent a rectangular prism.
    """
    def __init__(self, width, height, depth):
        super().__init__(width, height, depth)

    def __repr__(self):
        s = "RectangularPrism("
        s += f"width={self.width},"
        s += f"height={self.height},"
        s += f"depth={self.depth})"
        return s

    def area(self):
        """
        A function to return the surface area.
        """
        total = 2*self.area_wh()
        total += 2*self.area_wd()
        total += 2*self.area_hd()
        return total

    def volume(self):
        """
        A function to return the volume.
        """
        return self.width*self.height*self.depth


if __name__ == "__main__":
    rec = Rectangle(2, 3)
    print(f"{rec}: area={rec.area()}")
    rec_prism = RectangularPrism(1, 2, 3)
    print(f"{rec_prism}: area={rec_prism.area()}, volume={rec_prism.volume()}")
