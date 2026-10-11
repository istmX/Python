print("1. Check Balance")
print("2. Deposit")
print("3. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance is 1000")
    case 2:
        amount = int(input("Enter amount: "))
        print("Deposited", amount)
    case 3:
        print("Exited")
    case _:
        print("Invalid option")
