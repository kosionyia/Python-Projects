"""
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should
print a sentence summarizing the size of the shirt and the message printed
on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.

"""

# def make_shirt(size, message):
#     print(f"The size of your shirt is {size}, and your message\n{message}.")

# make_shirt("xl", "I am loved at home.")
# make_shirt(size = "2xl", message = "I am a gangstar.")

"""
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a
different message.


"""

def make_shirt (size = "Large", message = "I love python"):
    print(f"My size is {size}, and {message}.")

make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "2XL", message = "I no like python oo")


"""
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.

"""

def describe_city(city, country = "Brazil"):
    print(f"{city} is in {country}")

describe_city("Porto Alegre")
describe_city("Canela")
describe_city("LIma", "Peru")