# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self,radius):
        """Initialize the circle with a radius."""
        self.radius = radius
        
    
    def calculate_area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius **2)
    
    def calculate_perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius
        
# Example Usage

radius_input = 5
my_circle = Circle(radius_input)
print(f"Radius: {radius_input}")        
print(f"Area: {my_circle.calculate_area():.2f}")
print(f"Perimeter: {my_circle.calculate_perimeter():.2f}")

