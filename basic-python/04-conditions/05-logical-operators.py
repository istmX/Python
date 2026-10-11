age = int(input("Enter age: "))
citizen = input("Are you a citizen (yes/no): ")

if age >= 18 and citizen == "yes":
    print("Eligible to vote")
else:
    print("Not eligible")
