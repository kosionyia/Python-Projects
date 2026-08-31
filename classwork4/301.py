"""
An ice cream stand is a specific kind of restaurant.
Write a class called IceCreamStand that inherits from the Restaurant class you
wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version
of the class will work; just pick the one you like better. Add an attribute
called flavors that stores a list of ice cream flavors. Write a method that
displays these flavors. Create an instance of IceCreamStand, and call this
method.
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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = "chocolate", "vanilla", "strawberry"
    def display_flavors(self):
        print(f"the flavors are {self.flavors}")

            # kosi = IceCreamStand("kili", "rice")
            # kosi.display_flavors()

        """
            An administrator is a special kind of user. Write a class called
            Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or
            Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
            strings like "can add post", "can delete post", "can ban user", and so on. Write a
            method called show_privileges() that lists the administrator’s set of
            privileges. Create an instance of Admin, and call your method.
            """

class User():
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is a {self.gender.title()}")


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_priviledges(self):
        print(f"{self.privileges} are your priviledges.")

        # kam = Admin("kamsi", "onyia", "female")
        # kam.show_priviledges()
        """
        Privileges: Write a separate Privileges class. The class should have
        one attribute, privileges, that stores a list of strings as described in Exercise
        9-7. Move the show_privileges() method to this class. Make a Privileges
        instance as an attribute in the Admin class. Create a new instance of Admin
        and use your method to show its privileges.

        """
class Privileges():
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.priviledges = privileges

    def show_priviledges(self):
        print(f"\n Privileges")
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin1(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()


admin_user = Admin1("Oluwa", "Seyi", "Male")
admin_user.describe_user()

admin_user.privileges.show_priviledges()

"""
 Use the final version of electric_car.py from this
section. Add a method to the Battery class called upgrade_battery(). This
method should check the battery size and set the capacity to 65 if it isn’t
already. Make an electric car with a default battery size, call get_range()
once, and then call get_range() a second time after upgrading the battery.
You should see an increase in the car’s range.
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 240
        elif self.battery_size == 65:
            range = 365
            
        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Upgraded the battery to 65 kWh.")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()

my_leaf.battery.get_range()