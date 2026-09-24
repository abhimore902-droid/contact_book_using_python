#empty dictionary
contacts = {}

while True:
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Save Names")
    print("6. Save Email")
    print("7. Save Phone Numbers")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        contacts[name] = phone
        print(f"Contact {name} added successfully.")

    elif choice == '2':
        if contacts:
            print("Contacts List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

    elif choice == '3':
        search_name = input("Enter the name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print(f"Contact {search_name} not found.")

    elif choice == '4':
        delete_name = input("Enter the name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact {delete_name} deleted successfully.")
        else:
            print(f"Contact {delete_name} not found.")

    elif choice == '5':
        save_name = input("Enter the name to save: ")
        if save_name in contacts:
            with open("names.txt", "a") as file:
                file.write(f"{save_name}\n")
            print(f"Name {save_name} saved to names.txt.")
        else:
            print(f"Contact {save_name} not found.")

    elif choice == '6':
        save_email = input("Enter the name to save email: ")
        if save_email in contacts:
            email = input("Enter the email address: ")
            with open("emails.txt", "a") as file:
                file.write(f"{save_email}: {email}\n")
            print(f"Email for {save_email} saved to emails.txt.")
        else:
            print(f"Contact {save_email} not found.")

    elif choice == '7':
        save_phone = input("Enter the name to save phone number: ")
        if save_phone in contacts:
            with open("phone_numbers.txt", "a") as file:
                file.write(f"{save_phone}: {contacts[save_phone]}\n")
            print(f"Phone number for {save_phone} saved to phone_numbers.txt.")
        else:
            print(f"Contact {save_phone} not found.")   

    elif choice == '8':
        print("Exiting Contact Book. Goodbye!")
        break       

    else:
        print("Invalid choice. Please try again.")  

                        