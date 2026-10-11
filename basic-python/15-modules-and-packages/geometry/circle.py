# circle.py — a module inside the geometry package

from geometry import PI


def area(radius):
    """Return the area of a circle with the given radius."""
    return PI * radius * radius


def circumference(radius):
    """Return the circumference of a circle with the given radius."""
    return 2 * PI * radius
