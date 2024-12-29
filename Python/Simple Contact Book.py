def add_contact(contacts, name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def view_contacts(contacts):
    print("\nContacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}
    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. View contacts")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(contacts, name, phone)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
