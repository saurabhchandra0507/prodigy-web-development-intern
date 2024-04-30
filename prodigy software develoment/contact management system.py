def add_contact(contacts, name, phone_number):
    """Add a new contact"""
    if name not in contacts:
        contacts[name] = phone_number
        print(f"{name} added to contacts.")
    else:
        print(f"{name} is already in contacts.")

def delete_contact(contacts, name):
    """Delete a contact"""
    if name in contacts:
        del contacts[name]
        print(f"{name} deleted from contacts.")
    else:
        print(f"{name} is not in contacts.")

def search_contact(contacts, name):
    """Search for a contact"""
    if name in contacts:
        print(f"Phone number of {name} is: {contacts[name]}")
    else:
        print(f"{name} is not in contacts.")

def print_contacts(contacts):
    """Print all contacts"""
    if contacts:
        print("List of contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts to display.")

def main():
    contacts = {}

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Print All Contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            add_contact(contacts, name, phone_number)
        elif choice == "2":
            name = input("Enter contact name to delete: ")
            delete_contact(contacts, name)
        elif choice == "3":
            name = input("Enter contact name to search: ")
            search_contact(contacts, name)
        elif choice == "4":
            print_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
