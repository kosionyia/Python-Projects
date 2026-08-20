sandwich_orders = ["tuna", "chicken", "beef", "cheese", "turkey"]

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)



sandwich_orders = [
    "tuna",
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "cheese"
]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)


    responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    responses[name] = place

    repeat = input("Would you like to let another person respond? (yes/no): ")

    if repeat == "no":
        polling_active = False

print("\n--- Poll Results ---")

for name, place in responses.items():
    print(f"{name} would like to visit {place}.")