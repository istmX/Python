intro_message = "Hi there! I’m learning Python, just like you 😄"
print(intro_message)

user_name = input("Can you please tell me your name: ")

name_res = "That’s a cool name 😎"
print(name_res)

user_age = int(input("Can you tell me your age too: "))

if user_age <= 13:
    print("Wow! You’re young and smart 😄")
elif user_age > 13 and user_age < 18:
    print("Nice! Learning now will help you a lot")
else:
    print("It’s awesome that you’re learning Python")

main_menu = "Here are some things I can help you with:"
print(main_menu)

# Main menu loop keeps running until user chooses exit
while True:
    print("\nHere are some things I can help you with:")
    print("1. Simple Calculator")
    print("2. Multiplication Table")
    print("3. Even or Odd Checker")
    print("4. Guess the Number Game")
    print("5. Exit")

    menu_num = int(input("Enter a number from 1 to 5: "))

    # Calculator
    if menu_num == 1:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        operator = input("Choose an operator (+, -, *, /): ")

        if operator == "+":
            print("Result:", first_number + second_number)
        elif operator == "-":
            print("Result:", first_number - second_number)
        elif operator == "*":
            print("Result:", first_number * second_number)
        elif operator == "/":
            if second_number == 0:
                print("Division by zero is not allowed.")
            else:
                print("Result:", first_number / second_number)
        else:
            print("Invalid operator.")

    # Multiplication table
    elif menu_num == 2:
        number = int(input("Enter a number: "))
        for i in range(1, 11):
            print(number, "x", i, "=", number * i)

    # Even or Odd
    elif menu_num == 3:
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print(number, "is Even")
        else:
            print(number, "is Odd")

    # Guess game
    elif menu_num == 4:
        secret_number = 42
        attempts = 0
        while True:
            guess = int(input("Guess the number: "))
            attempts += 1
            if guess == secret_number:
                print("You guessed it correctly!")
                print("Attempts:", attempts)
                break
            else:
                print("Wrong guess, try again.")

    # Exit
    elif menu_num == 5:
        print("Goodbye! Thanks for using the assistant.")
        break

    # Invalid choice
    else:
        print("Please enter a valid option.")
