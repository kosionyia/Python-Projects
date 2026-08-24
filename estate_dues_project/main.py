from estate_dues.storage import load_data, save_data
from estate_dues import members
from estate_dues import payments
from estate_dues.logger import log_event


def main():

    data = load_data()

    while True:
        print("\n=== Estate Union Dues Tracker ===")
        print("1. Register member")
        print("2. View members")
        print("3. Record payment")
        print("4. View member payment history")
        print("5. Check payment status")
        print("6. Exit")

        choice = input("\nChoose an option: ")

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
                print("Select 1 to register a new member.")

        elif choice =="3":
            try:
                member_id = int(input("Enter member ID: "))
                month = input("Enter month (e.g. August 2026): ")
                amount = float(input("Enter amount paiid: "))

                payment = payments.record_payment(
                    data, member_id, month, amount
                )

                if payment is None:
                    print("Member not found. Pyament was not recorded.")
                else:
                    save_data(data)

                    member = members.get_member(data, member_id)

                    log_event(
                        f"Payment recorded: {member['name']}"
                        f"paid ₦{amount:,.2f} for {month}"
                    )

                    print("\nPayment recorded successfully!")

            except ValueError:
                print("\nPlease eneter a valide member ID and amount,")


        elif choice == "4":
            try:
                member_id = int(input("Enter member ID: "))

                member = members.get_member(data, member_id)

                if member is None:
                    print("Member not found.")
                    continue

                payment_history = payments.get_member_payments(
                    data, member_id
                )
                print(f"\nPayment history for {member['name']}:")

                if not payment_history:
                    print("No payments found.")
                else:
                    for payment in payment_history:
                        print(
                            f"Payment ID: {payment['id']} | "
                            f"Month: {payment['month']} | "
                            f"Amount: ₦{payment['amount']:,.2f} | "
                            f"Date: {payment['date_paid']}"
                        )

            except ValueError:
                print("Please enter a valid member ID.")

        elif choice == "5":
            try:
                member_id = int(input("Enter member ID: "))
                month = input("Enter month (e.g. August 2026): ")

                member = members.get_member(data, member_id)

                if member is None:
                    print("Member not found.")
                    continue

                status = payments.get_payment_status(
                    data,  member_id, month
                    )

                print(f"\nMember: {member['name']}")
                print(f"Month: {month}")
                print(f"Paid: ₦{status['paid']:,.2f}")
                print(f"Balance: ₦{status['balance']:,.2f}")
                print(f"Status: {status['status']}")

            except ValueError:
                print("Please enter a valid member ID.")

        elif choice == "6":
            print("\nSee You Next Time!")
            break

        else:
            print("\nInvalid choice. Please selected an option from 1-6.")

if __name__ == "__main__":
    main()