"""
Write a function that accepts a list of items a person
wants on a sandwich. The function should have one parameter that collects
as many items as the function call provides, and it should print a summary
of the sandwich that’s being ordered. Call the function three times, using a
different number of arguments each time.
"""
def make_sandwich(*items):
    print("\nSandwich order:")
    
    for item in items:
        print(f"- {item}")


make_sandwich("bread", "cheese", "chicken")

make_sandwich("bread", "lettuce", "tomato", "cheese", "beef")

make_sandwich("bread", "egg")

"""
Start with a copy of user_profile.py from page 148.
Build a profile of yourself by calling build_profile(), using your first and last
names and three other key-value pairs that describe you.
"""
def build_profile(first, last, **user_info):

    """Build a dictionary containing everything we know about
a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Kosi', 'Onyia',
 location='Enugu',
 field='Cybersecurity',
 gender = 'Female'
 )
print(user_profile)

"""
Write a function that stores information about a car in a
dictionary. The function should always receive a manufacturer and a model
name. It should then accept an arbitrary number of keyword arguments. Call
the function with the required information and two other name-value pairs,
such as a color or an optional feature. Your function should work for a call
like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.

"""
def make_car(manufacturer, model, **kwargs):
    car ={
        "manufacturer": manufacturer,
        "model":  model
    }
    car.update(kwargs)
    return car

car = make_car(
    "subaru",
    "outback",
    color="blue",
    tow_package=True
)

print(car)
