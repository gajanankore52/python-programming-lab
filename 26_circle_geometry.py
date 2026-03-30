# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self,radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        
        self.radius = radius
        
    @property
    def area(self):
        
        return math.pi * (self.radius **2)
    @property
    def perimeter(self):
        
        return 2 * math.pi * self.radius
        
# Example Usage

radius_input = 5
my_circle = Circle(radius_input)
print(f"Radius: {radius_input}")        
print(f"Area: {my_circle.area:.2f}")
print(f"Perimeter: {my_circle.perimeter:.2f}")

