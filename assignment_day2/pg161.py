# CONDITIONAL TESTS

car = "Volkswagon"
user = input("Enter a car:\n")
print(f"Is {user} a valid car?")
print({user == car})

car1 = "Audi"
user1 = input("Enter car2:\n")
print(f"Is {user1} a valid car?")
print({user1 == car1.lower()})

mother = "Mom"
user2 = input("What do I call my mother?\n")
print(mother==user2)

mother1 = "Mom"
user3 = input("What do I call my mother?\n")
print(mother1 == user3.title())

number = 7
user4 = input("Guess the number in my head\n")
print(number == user4)

father = "Daddy"
user5 = input("What do I call my father?\n")
print(father == user5)

father = "DADDY"
user6 = input("What do I call my father?\n")
print(father == user6.upper())

number2 = 3.14
user7 = float(input("What is the value of PI?\n"))
ans = round(user7, 2)
print(number2 == ans)

number3 = 7
user8 = int(input("Guess the number in my head\n"))
print(number3 <= user8)

food = "Amala"
user9 = input("Enter your favourite food:\n")
print (food != user9)

user_name = input("Enter your name\n")
user_age = int(input("Enter your age\n"))
if len(user_name) >=5 and user_age >= 21:
    print("Status: Adult")
else:
    print("Status: Underagae")

user1_name = input("Enter your name\n")
user2_age = int(input("Enter your age\n"))
if len(user1_name) <=7 or user2_age %2 == 0:
    print("YOOOOWAAAA")
else:
    print("kadan kadan")

