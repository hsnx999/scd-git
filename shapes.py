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
        self._radius = radius  # Private attribute with a single underscore

    # Getter method for radius
    def get_radius(self):
        return self._radius

    # Setter method for radius
    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print("Invalid radius value. Radius must be positive.")

    def calculate_area(self):
        return math.pi * self._radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self._length = length  # Private attribute with a single underscore
        self._width = width

    # Getter method for length
    def get_length(self):
        return self._length

    # Setter method for length
    def set_length(self, length):
        if length > 0:
            self._length = length
        else:
            print("Invalid length value. Length must be positive.")

    # Getter method for width
    def get_width(self):
        return self._width

    # Setter method for width
    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            print("Invalid width value. Width must be positive.")

    def calculate_area(self):
        return self._length * self._width

    def calculate_perimeter(self):
        return 2 * (self._length + self._width)

# Example usage
circle = Circle(7)
print(f"Circle Area: {circle.calculate_area()}")
print(f"Circle Perimeter: {circle.calculate_perimeter()}")

rectangle = Rectangle(5, 7)
print(f"Rectangle Area: {rectangle.calculate_area()}")
print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")

# Using getter and setter methods
circle.set_radius(10)
print(f"Updated Circle Radius: {circle.get_radius()}")

rectangle.set_length(8)
rectangle.set_width(6)
print(f"Updated Rectangle Length: {rectangle.get_length()}")
print(f"Updated Rectangle Width: {rectangle.get_width()}")
