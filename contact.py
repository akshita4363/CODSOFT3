import os

CONTACTS_FILE = "contacts.txt"
RECORD_LENGTH = 50  # Fixed length for each record (adjust as needed)

# Function to add a new contact
def add_contact():
    print("\nAdding a new contact...")
    with open(CONTACTS_FILE, 'ab') as file:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        # Formatting and encoding the record before writing
        record = f"{name:30}{phone:20}\n".encode()
        file.write(record)

    print("Contact added successfully!")

# Function to search for a contact
def search_contact():
    print("\nSearching for a contact...")
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found!")
        return

    name_query = input("Enter name to search: ").encode()

    with open(CONTACTS_FILE, 'rb') as file:
        position = 0
        file_size = os.path.getsize(CONTACTS_FILE)
        num_records = file_size // RECORD_LENGTH

        for i in range(num_records):
            file.seek(position)
            record = file.read(RECORD_LENGTH)

            if name_query in record:
                print(f"Contact found: {record.decode().strip()}")
                return
            position += RECORD_LENGTH

    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    print("\nDeleting a contact...")
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found!")
        return

    name_query = input("Enter name to delete: ")

    with open(CONTACTS_FILE, 'rb') as file:
        records = file.readlines()

    with open(CONTACTS_FILE, 'wb') as file:
        found = False
        for record in records:
            if name_query.encode() in record:
                found = True
                continue  # Skip writing this record (deleting it)
            file.write(record)

    if found:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main function to display options
def main():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
