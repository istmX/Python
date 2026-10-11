a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator: ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid operator")
