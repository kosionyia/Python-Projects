

# dream_country = ["Greece", "Paris", "Czech", "Finland", "Denmark"]
# print(f"The first three items on the list are: {dream_country[:3]}")
# print(f"Three items from the middle of the list are: {dream_country[2:5]}")
# print(f"The last three items in the list are: {dream_country[-3:]}")


pizza = [
   "Cheese", 
   "Pepperoni Feast", 
   "Margherita", 
   "Spicy Pepperoni", 
   "Veggie"
]

friend_pizza = [
   "Cheese", 
   "Pepperoni Feast", 
   "Margherita", 
   "Spicy Pepperoni", 
   "Veggie"
]

pizza.append("extra cheese")
friend_pizza.append("pepperoni")
for i in pizza:
    print(f"My favourite pizzas are: {i}")
for z in friend_pizza:
    print(f"My friend's favourit pizzas are: {z}")
