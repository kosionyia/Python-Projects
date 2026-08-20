# username = ["godswill_o",
#             "shadesOfRuby",
#             "mitchelle",
#             "kosi.kaira",
#             "admin"]

# for user in username:
#     if user == "admin":
#         print(f"Hello admin, would you like to see a status report?")
#     else:
#         print(f"Hello {user}, thank you for loggin in again.")

# if username == []:
#     print("We need to find some users!")


current_users = ["Godswill_o",
            "ShadesOfRuby",
            "Mitchelle",
            "Kosi.kaira",
            "Admin"]

new_users = ["ifeanyi",
             "obinna",
             "charles",
             "mitchelle",
             "kamkam"]

current_user_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_user_lower:
        print(f"{new_user} has already been used. You will need to enter a new username.")
    else:
        print(f"{new_user} is available.")


numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
