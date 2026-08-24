from estate_dues.storage import load_data, save_data
from estate_dues import members
from estate_dues.logger import log_event


data = load_data()

while True:
    print("\nEstate Union Dues Tracker")
    print("1. Register member")
    print("2. View members")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("\nEnter member name: ")
        phone = input("Enter phone number: ")

        member = members.add_member(data, name, phone)

        save_data(data)

        log_event(
        f"Registered member: {member['name']} "
        f"(ID: {member['id']})"
    )
        print(f"\nMember registered successfully. ID: {member['id']}")

    elif choice == "2":
        all_members = members.get_all_members(data)

        for member in all_members:
            print(
                f"\nID: {member['id']} | "
                f"Name: {member['name']} | "
                f"Phone: {member['phone']}"
            )
        else:
            print("\nNo registered members yet.")
            print("\nSelect 1 to register a new member.")

    elif choice == "3":
        print("\nSee You Next Time!")
        break

    else:
        print("Invalid choice.")

