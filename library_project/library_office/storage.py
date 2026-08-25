"""
This module is for saving and loading book data
"""

import json

DATA_FILE = "books.json"

DEFAULT_BOOKS = [
    {
        "id": 1,
        "title": "Things Fall Apart",
        "author": "Chinua Achebe",
        "status": "on shelf"
    },
    {
        "id": 2,
        "title": "Purple Hibiscus",
        "author": "Chimamanda Adichie",
        "status": "borrowed"
    },
    {
        "id": 3,
        "title": "The Famished Road",
        "author": "Ben Okri",
        "status": "on shelf"
    },
    {
        "id": 4,
        "title": "Sozaboy",
        "author": "Ken Saro-Wiwa",
        "status": "on shelf"
    },
    {
        "id": 5,
        "title": "Jagua Nana",
        "author": "Cyprian Ekwensi",
        "status": "borrowed"
    },
    {
        "id": 6,
        "title": "The Joys of Motherhood",
        "author": "Buchi Emecheta",
        "status": "on shelf"
    },
    {
        "id": 7,
        "title": "Arrow of God",
        "author": "Chinua Achebe",
        "status": "on shelf"
    },
    {
        "id": 8,
        "title": "Stay With Me",
        "author": "Ayobami Adebayo",
        "status": "borrowed"
    },
    {
        "id": 9,
        "title": "The Fishermen",
        "author": "Chigozie Obioma",
        "status": "on shelf"
    },
    {
        "id": 10,
        "title": "Half of a Yellow Sun",
        "author": "Chimamanda Adichie",
        "status": "on shelf"
    }
]

def load_data():
    """Load books from the JSON file.

    If the file does not exist, return the default ten books.
    If the file contains invalid JSON, return the default ten books.
    """
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        """ The isinstance() checks for the structure of the data """

        if not isinstance(data, list):
            raise TypeError("Invalid data format.")

        return data

    except FileNotFoundError:
        books =  DEFAULT_BOOKS.copy()
        save_data(books)
        return books

    except (json.JSONDecodeError, TypeError):
        print("The library ledger is corrupted. Starting with the default books.")
        return DEFAULT_BOOKS.copy()
    
def save_data(books):
    """Save the current list of books to the JSON ledger."""
    with open(DATA_FILE, "w") as file:
        json.dump(books, file, indent=4)


