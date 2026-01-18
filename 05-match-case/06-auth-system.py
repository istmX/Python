role = input("Enter role: ")

match role:
    case "admin":
        print("Full access")
    case "user":
        print("Limited access")
    case "guest":
        print("Read only")
    case _:
        print("No access")
