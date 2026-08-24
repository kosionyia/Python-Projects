from estate_dues.storage import load_data, save_data
from estate_dues import members



data = load_data()

while True:
    print("\nEstate Union Dues Tracker")
    print("1. Register member")
    print("2. View members")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter member name: ")
        phone = input("Enter phone number: ")

        member = members.add_member(data, name, phone)

        save_data(data)

        print(f"Member registered successfully. ID: {member['id']}")

    elif choice == "2":
        all_members = members.get_all_members(data)

        for member in all_members:
            print(
                f"ID: {member['id']} | "
                f"Name: {member['name']} | "
                f"Phone: {member['phone']}"
            )

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")