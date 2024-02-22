import math

class Shape:
    def calculate_area(self):
        """
        Placeholder method for calculating the area (to be implemented in derived classes).
        """
        pass

    def calculate_perimeter(self):
        """
        Placeholder method for calculating the perimeter (to be implemented in derived classes).
        """
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage
circle = Circle(7)
print(f"Circle Area: {circle.calculate_area()}")
print(f"Circle Perimeter: {circle.calculate_perimeter()}")

rectangle = Rectangle(5, 7)
print(f"Rectangle Area: {rectangle.calculate_area()}")
print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")

triangle = Triangle(5, 4, 4, 3, 5)
print(f"Triangle Area: {triangle.calculate_area()}")
print(f"Triangle Perimeter: {triangle.calculate_perimeter()}")

