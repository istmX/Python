# User-Defined Exceptions
# You can create your own exception types by inheriting from Exception.
# This makes your error messages clearer and more specific.

class InvalidMarksError(Exception):
    """Raised when marks are outside the valid range (0-100)."""
    pass


class AgeLimitError(Exception):
    """Raised when an age requirement is not met."""
    pass


def set_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(f"Marks must be between 0 and 100, got {marks}.")
    print(f"Marks set to {marks}.")


def register_for_exam(age):
    if age < 17:
        raise AgeLimitError(f"Must be at least 17 years old, got {age}.")
    print("Registration successful.")


# Test the custom exceptions
try:
    set_marks(150)
except InvalidMarksError as error:
    print("Invalid marks:", error)

try:
    register_for_exam(15)
except AgeLimitError as error:
    print("Registration error:", error)

# Custom exceptions work with the same try/except machinery.
# They let calling code catch YOUR specific errors separately
# from built-in ones.

# Best practice: name your exceptions with an "Error" suffix
# and derive them from Exception (or a more specific built-in).
