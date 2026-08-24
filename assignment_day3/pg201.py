"""
Now that you know how to loop through a dictionary,
clean up the code from Exercise 6-3 (page 99) by replacing your series of
print() calls with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.

"""

glossary = {
    "variable": "A name that refers to a value stored in a program.",
    "string": "A sequence of characters enclosed in quotation marks.",
    "list": "A collection of items stored in a specific order.",
    "loop": "A way to repeatedly execute a block of code.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A block of code that performs a particular task.",
    "tuple": "A collection of items that cannot be changed.",
    "integer": "A whole number, such as 5 or 100.",
    "boolean": "A value that can be either True or False.",
    "conditional": "A statement that runs code based on a condition."
}

for word, meaning in glossary.items():
    print(f"{word}:")
    print(f"\t{meaning}\n")

"""
Make a dictionary containing three major rivers and the
country each river runs through. One key-value pair might be 'nile': 'egypt'.
Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
Use a loop to print the name of each river included in the dictionary.
Use a loop to print the name of each country included in the dictionary.

"""
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china"
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country.title())


"""
Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already
taken the poll, print a message thanking them for responding. If they have
not yet taken the poll, print a message inviting them to take the poll.
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people_to_poll = ['jen', 'mike', 'sarah', 'david', 'phil', 'grace']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")