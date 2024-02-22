from shapes import Circle, Rectangle

def print_details(shape_obj):
    """
    Prints the area and perimeter of a Shape object.

    Args:
        shape_obj (Shape): An instance of a Shape (Circle or Rectangle).

    Returns:
        None
    """
    area = shape_obj.calculate_area()
    perimeter = shape_obj.calculate_perimeter()

    print(f"Area: {area:.2f} square units")
    print(f"Perimeter: {perimeter:.2f} units")

# Example usage
rectangle = Rectangle(5, 7)
circle = Circle(7)

print("Rectangle details:")
print_details(rectangle)

print("\nCircle details:")
print_details(circle)
