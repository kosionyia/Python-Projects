"""
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "city": "Lagos"
}

person_2 = {
    "first_name": "Sarah",
    "last_name": "Smith",
    "age": 30,
    "city": "Abuja"
}

person_3 = {
    "first_name": "David",
    "last_name": "Brown",
    "age": 22,
    "city": "Port Harcourt"
}

people = [person, person_2, person_3]

for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()

"""
Make several dictionaries, where each dictionary represents a
different pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your
list and as you do, print everything you know about each pet.
"""
pet_1 = {
    "animal": "dog",
    "owner": "John"
}

pet_2 = {
    "animal": "cat",
    "owner": "Sarah"
}

pet_3 = {
    "animal": "parrot",
    "owner": "David"
}

pet_4 = {
    "animal": "rabbit",
    "owner": "Grace"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}")
    print()


"""
Make a dictionary called favorite_places. Think of
three names to use as keys in the dictionary, and store one to three favorite
places for each person. To make this exercise a bit more interesting, ask
some friends to name a few of their favorite places. Loop through the
dictionary, and print each person’s name and their favorite places.

"""
favorite_places = {
    "John": ["Lagos", "London", "Dubai"],
    "Sarah": ["Abuja", "Paris"],
    "David": ["New York", "Cape Town", "Rome"]
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")

    for place in places:
        print(f"\t{place}")

    print()

"""
Modify your program from Exercise 6-2 (page
98) so each person can have more than one favorite number. Then print
each person’s name along with their favorite numbers.
"""
favorite_numbers: dict[str, list[int]] = {
    "Seyi": [7, 12, 21],
    "John": [5, 10],
    "David": [3, 8, 15],
    "Mary": [2, 6, 9],
    "Grace": [4, 11]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")

    for number in numbers:
        print(f"\t{number}")

    print()

"""
Make a dictionary called cities. Use the names of three cities
as keys in your dictionary. Create a dictionary of information about each city
and include the country that the city is in, its approximate population, and
one fact about that city. The keys for each city’s dictionary should be
something like country, population, and fact. Print the name of each city and
all of the information you have stored about it.
"""
cities = {
    "Lagos": {
        "country": "Nigeria",
        "population": "15 million",
        "fact": "Lagos is the largest city in Nigeria."
    },
    "London": {
        "country": "England",
        "population": "9 million",
        "fact": "London is the capital of the United Kingdom."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is one of the world's most populous metropolitan areas."
    }
}

for city, information in cities.items():
    print(f"\nCity: {city}")

    for key, value in information.items():
        print(f"{key.title()}: {value}")


"""
We’re now working with examples that are complex
enough that they can be extended in any number of ways. Use one of the
example programs from this chapter, and extend it by adding new keys and
values, changing the context of the program, or improving the formatting of
the output.
"""
cities = {
    "Lagos": {
        "country": "Nigeria",
        "population": "15 million",
        "fact": "Lagos is one of the largest cities in Africa.",
        "language": "English",
        "famous_for": "Beaches, music, and entertainment"
    },
    "London": {
        "country": "England",
        "population": "9 million",
        "fact": "London is the capital of the United Kingdom.",
        "language": "English",
        "famous_for": "Big Ben and the London Eye"
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is one of the world's most populous cities.",
        "language": "Japanese",
        "famous_for": "Technology and modern culture"
    }
}

for city, information in cities.items():
    print(f"\n{'=' * 30}")
    print(f"City: {city}")
    print(f"{'=' * 30}")

    for key, value in information.items():
        print(f"{key.title()}: {value}")