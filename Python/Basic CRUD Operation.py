def create_entry(data, key, value):
    data[key] = value
    print(f"Entry {key} added.")

def read_entry(data, key):
    return data.get(key, "Entry not found")

def update_entry(data, key, value):
    if key in data:
        data[key] = value
        print(f"Entry {key} updated.")
    else:
        print("Entry not found")

def delete_entry(data, key):
    if key in data:
        del data[key]
        print(f"Entry {key} deleted.")
    else:
        print("Entry not found")

def main():
    data = {}
    while True:
        print("\nOptions:")
        print("1. Create entry")
        print("2. Read entry")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            create_entry(data, key, value)
        elif choice == '2':
            key = input("Enter key: ")
            print(f"Value: {read_entry(data, key)}")
        elif choice == '3':
            key = input("Enter key: ")
            value = input("Enter new value: ")
            update_entry(data, key, value)
        elif choice == '4':
            key = input("Enter key: ")
            delete_entry(data, key)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
