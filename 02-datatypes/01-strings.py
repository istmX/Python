text = input("Enter any text: ")

print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Length:", len(text))

print("Starts with A:", text.startswith("A"))
print("Ends with Z:", text.endswith("Z"))

print("Is alphabet only:", text.isalpha())
print("Is digit only:", text.isdigit())
