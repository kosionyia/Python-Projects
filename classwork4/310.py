"""
Using your latest Restaurant class, store it in a
module. Make a separate file that imports Restaurant. Make a Restaurant
instance, and call one of Restaurant’s methods to show that the import
statement is working properly.
"""

from modules import mod_310, mod3_310

# Create a new Restaurant instance
my_cafe = mod_310.Restaurant("The Daily Grind", "Cafe/Bakery")

my_cafe.describe_restaurant()
my_cafe.open_restaurant()

"""
Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly.
"""

# Create an Admin instance
admin_user = mod3_310.Admin("Alice", "Smith", "female")
admin_user.describe_user()

# Call show_privileges() to verify the import is working properly
admin_user.privileges.show_privileges()
