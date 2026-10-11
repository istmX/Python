# Mini Project: Contact Book
# This project saves contacts to a file so they persist
# between program runs. It uses file handling and exception handling.

CONTACTS_FILE = "contacts.txt"


def load_contacts():
    """Read contacts from the file into a dictionary."""
    contacts = {}
    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                name, phone = line.split("|")
                contacts[name] = phone
    except FileNotFoundError:
        # First run: the file does not exist yet. That is fine.
        pass
    return contacts


def save_contacts(contacts):
    """Write all contacts back to the file."""
    with open(CONTACTS_FILE, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}|{phone}\n")


def show_menu():
    print("\n--- Contact Book ---")
    print("1. View all contacts")
    print("2. Add a contact")
    print("3. Search a contact")
    print("4. Delete a contact")
    print("5. Exit")


def main():
    contacts = load_contacts()
    print("Welcome to Contact Book!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if not contacts:
                print("No contacts yet.")
            else:
                for name, phone in sorted(contacts.items()):
                    print(f"{name}: {phone}")

        elif choice == "2":
            name = input("Enter name: ").strip()
            phone = input("Enter phone: ").strip()
            if not name or not phone:
                print("Name and phone cannot be empty.")
                continue
            contacts[name] = phone
            save_contacts(contacts)
            print(f"Contact '{name}' saved.")

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            if name in contacts:
                print(f"{name}: {contacts[name]}")
            else:
                print(f"'{name}' not found.")

        elif choice == "4":
            name = input("Enter name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print(f"Contact '{name}' deleted.")
            else:
                print(f"'{name}' not found.")

        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
