# Mini Project: Student Result System
# This project uses exception handling to build a robust
# student result calculator that never crashes on bad input.

# Custom exception for invalid marks
class InvalidMarksError(Exception):
    """Raised when marks are outside the range 0-100."""
    pass


def get_marks(subject):
    """Ask for marks in a subject and validate the input."""
    while True:
        try:
            value = input(f"Enter marks for {subject} (0-100): ")
            marks = float(value)          # may raise ValueError
            if marks < 0 or marks > 100:
                raise InvalidMarksError    # our own exception
            return marks
        except ValueError:
            print("  Please enter a numeric value.")
        except InvalidMarksError:
            print("  Marks must be between 0 and 100.")


def calculate_result(marks_list):
    """Return average, percentage, and grade."""
    average = sum(marks_list) / len(marks_list)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "F"

    return average, grade


def main():
    print("=" * 40)
    print("STUDENT RESULT SYSTEM")
    print("=" * 40)

    name = input("Enter student name: ")

    subjects = ["Math", "Science", "English"]
    marks_list = []

    for subject in subjects:
        marks_list.append(get_marks(subject))

    try:
        average, grade = calculate_result(marks_list)
    except ZeroDivisionError:
        print("Error: no subjects entered.")
        return

    print("\n--- Result ---")
    print(f"Student: {name}")
    for subject, marks in zip(subjects, marks_list):
        print(f"{subject}: {marks}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()
