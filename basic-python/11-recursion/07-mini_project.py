# Mini Project: Recursion Toolbox
# This project uses recursion for two classic tasks:
# checking palindromes and calculating the sum of digits.

def is_palindrome(text):
    """Return True if the text reads the same forwards and backwards."""
    # Base case 1: empty string or single letter is a palindrome
    if len(text) <= 1:
        return True

    # Base case 2: first and last letters differ -> not a palindrome
    if text[0] != text[-1]:
        return False

    # Recursive case: check the middle part (without first and last letters)
    return is_palindrome(text[1:-1])


def sum_of_digits(number):
    """Return the sum of all digits using recursion."""
    # Base case: a single digit is its own sum
    if number < 10:
        return number

    # Recursive case: last digit + sum of the remaining digits
    return (number % 10) + sum_of_digits(number // 10)


def power(base, exponent):
    """Calculate base^exponent using recursion."""
    # Base case: anything to the power of 0 is 1
    if exponent == 0:
        return 1

    # Recursive case: base * base^(exponent-1)
    return base * power(base, exponent - 1)


# ---- Try the tools ----
print("=" * 40)
print("RECURSION TOOLBOX")
print("=" * 40)

print("\n--- Palindrome Checker ---")
for word in ["level", "hello", "madam", "python", "racecar"]:
    result = "is" if is_palindrome(word) else "is NOT"
    print(f"'{word}' {result} a palindrome")

print("\n--- Sum of Digits ---")
for number in [123, 4567, 9, 1001]:
    print(f"Sum of digits of {number} = {sum_of_digits(number)}")

print("\n--- Power Calculator ---")
print(f"2^10 = {power(2, 10)}")
print(f"5^3 = {power(5, 3)}")
print(f"7^0 = {power(7, 0)}")

print("\n" + "=" * 40)
