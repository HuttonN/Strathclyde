"""
Write a program that contains a floating point variable, which is the
radius of a circle. The program should use the math library to
calculate the area of the circle. The area of the circle is given by:

a =πr2

where a is the area, π is available in the math library as math.pi
and r is the radius. The square of a r can be calculating by using
math.pow(r,2) or r**2. The program should print the radius and the
area.
"""

import math

radius = 6.7

area = math.pi*math.pow(radius, 2)

print(area)
