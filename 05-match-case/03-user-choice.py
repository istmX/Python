choice = input("Enter choice: ")

match choice:
    case "start":
        print("Game started")
    case "stop":
        print("Game stopped")
    case _:
        print("Invalid choice")
