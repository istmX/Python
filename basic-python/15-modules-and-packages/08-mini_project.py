# Mini Project: Geometry Calculator
# This project uses the custom "geometry" package to calculate
# areas and perimeters based on user input.

from geometry.circle import area as circle_area
from geometry.circle import circumference
from geometry.rectangle import area as rectangle_area
from geometry.rectangle import perimeter


def get_positive_number(prompt):
    """Ask the user for a positive number and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=" * 40)
    print("GEOMETRY CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose a shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            radius = get_positive_number("Enter the radius: ")
            print(f"Area: {circle_area(radius):.2f}")
            print(f"Circumference: {circumference(radius):.2f}")

        elif choice == "2":
            length = get_positive_number("Enter the length: ")
            width = get_positive_number("Enter the width: ")
            print(f"Area: {rectangle_area(length, width):.2f}")
            print(f"Perimeter: {perimeter(length, width):.2f}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# The main guard: run only when executed directly, not on import.
if __name__ == "__main__":
    main()
