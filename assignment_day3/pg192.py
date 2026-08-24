"""
Use a dictionary to store information about a person you
know. Store their first name, last name, age, and the city in which they live.
You should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "city": "Lagos"
}


print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("City:", person["city"])

"""
Use a dictionary to store people’s favorite
numbers. Think of five names, and use them as keys in your dictionary.
Think of a favorite number for each person, and store each as a value in
your dictionary. Print each person’s name and their favorite number. For
even more fun, poll a few friends and get some actual data for your
program.
"""
favorite_numbers = {
    "Seyi": 7,
    "John": 12,
    "David": 3,
    "Mary": 21,
    "Grace": 10
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

"""
A Python dictionary can be used to model an actual
dictionary. However, to avoid confusion, let’s call it a glossary.
Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
Print each word and its meaning as neatly formatted output. You might print
the word followed by a colon and then its meaning, or print the word on one
line and then print its meaning indented on a second line. Use the newline
character (\n) to insert a blank line between each word-meaning pair in your
output.

"""
glossary = {
    "variable": "A name that refers to a value stored in a program.",
    "string": "A sequence of characters enclosed in quotation marks.",
    "list": "A collection of items stored in a specific order.",
    "loop": "A way to repeatedly execute a block of code.",
    "dictionary": "A collection of key-value pairs."
}

for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")

