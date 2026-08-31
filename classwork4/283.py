"""
Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.name} is open.")

restaurant = Restaurant("Skrept", "Jambalaya")
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
Start with your class from Exercise 9-1. Create
three different instances from the class, and call describe_restaurant() for
each instance.
"""
rest1 = Restaurant("Aquafina", "Water").describe_restaurant()
rest2 = Restaurant("Eva", "Chinese Rice").describe_restaurant()
rest3 = Restaurant("Nestle", "Sparkling Water").describe_restaurant()


"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that prints a
summary of the user’s information. Make another method called greet_user()
that prints a personalized greeting to the user.
Create several instances representing different users, and call both
methods for each user
"""
class User():
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.gender.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, Welcome!")

person1 = User("amara", "ekwebelem", "female").describe_user()
person1 = User("rita", "okonkwo", "female").describe_user()
person1 = User("ifeanyi", "charles", "male").describe_user()
person1 = User("augustine", "chukwu", "male").describe_user()

person1 = User("amara", "ekwebelem", "female").greet_user()
person1 = User("rita", "okonkwo", "female").greet_user()
person1 = User("ifeanyi", "charles", "male").greet_user()
person1 = User("augustine", "chukwu", "male").greet_user()