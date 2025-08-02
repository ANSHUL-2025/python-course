import math

def calculate_circumference(radius):
    """
    Calculate the circumference of a circle given the radius.
    Formula: C = 2 * π * r
    """
    if radius < 0:
        return "Radius cannot be negative."
    circumference = 2 * math.pi * radius
    return circumference

# Example usage
r = float(input("Enter the radius of the circle: "))
result = calculate_circumference(r)
print(f"The circumference of the circle is: {result}")