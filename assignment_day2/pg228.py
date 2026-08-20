# topping = ""
# while topping != "quit":
#     topping = input("Enter a pizza toping or 'quit' to finish\n")

#     if topping != "quit":
#         print(f"{topping} successfully entered")


# while True:
#     user_age = input("Enter Your Age To View Ticket Prize or 0 to quit\n")
#     if user_age == 'quit':
#         break
#     age = int(user_age)
#     if age < 3:
#         print("Tickets are free for you")
#     elif age <= 12:
#       print("Tickets are for $10")
#     else:
#       print("Tickets are for $15")

#     #   WHILE STATEMENT
# user_age = ''
# while user_age != 'quit':
#     user_age = input("Enter Your Age To View Ticket Prize or 0 to quit\n")
#     if user_age == 'quit':
#         break

#     age = int(user_age)
#     if age < 3:
#         print("Tickets are free for you")
#     elif age <= 12:
#       print("Tickets are for $10")
#     else:
#       print("Tickets are for $15")

#     #   ACTIVE VARIABLE

active = True
while active:
    user_age = input("Enter Your Age To View Ticket Prize or 0 to quit\n")
    if user_age == 'quit':
        active = False

    age = int(user_age)
    if age < 3:
        print("Tickets are free for you")
    elif age <= 12:
      print("Tickets are for $10")
    else:
      print("Tickets are for $15")

#     #   BREAK STATEMENT
# while True:
#     user_age = int(input("Enter Your Age To View Ticket Prize or 0 to quit\n"))
#     if user_age == 'quit':
#         break
#     if user_age < 3:
#         print("Tickets are free for you")
#     elif user_age <= 12:
#       print("Tickets are for $10")
#     else:
#       print("Tickets are for $15")