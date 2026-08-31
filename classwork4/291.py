"""
Start with your program from Exercise 9-1 (page
162). Add an attribute called number_served with a default value of 0. Create
an instance called restaurant from this class. Print the number of customers
the restaurant has served, and then change this value and print it again.
"""
class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f"{self.name} is open.")

        # restaurant = Restaurant("Kilimanjaro", "Spaghetti")
        # print(restaurant.number_served)

        # restaurant.number_served = 12
        # print(f"{restaurant.number_served}")

        """
        Add a method called set_number_served() that lets you set the number of
        customers that have been served. Call this method with a new number and
        print the value again.
        """

    def set_number_served(self, served):
        self.number_served = served
        print(f"{self.name} has served {served} customers")

        # rest1 = Restaurant("Kili", "Bolongese")
        # rest1.set_number_served(34)

        """
        Add a method called increment_number_served() that lets you increment the
        number of customers who’ve been served. Call this method with any
        number you like that could represent how many customers were served in,
        say, a day of business.
        """

    def increment_number_served(self, number):
            self.number_served += number
            print(f"{self.name} served {number} customers today.")

"""
Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called
increment_login_attempts() that increments the value of login_attempts by 1.
Write another method called reset_login_attempts() that resets the value of
login_attempts to 0.
"""
class User():
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.gender.title()}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()}, Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

        """
        Make an instance of the User class and call increment_login_attempts()
        several times. Print the value of login_attempts to make sure it was
        incremented properly, and then call reset_login_attempts(). Print
        login_attempts again to make sure it was reset to 0.

        """
        
person1 = User("chioma", "aniji", "female")
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
person1.increment_login_attempts()
print(person1.login_attempts)

person1.reset_login_attempts()
print(person1.login_attempts)