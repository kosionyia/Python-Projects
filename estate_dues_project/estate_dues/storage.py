"""
This module is for saving and loading data
"""

import json


DATA_FILE = "data.json"

def create_empty_data():

    """Return the starting structure for a new estate database."""
    
    return {
        "settings": {
            "monthly_dues": 5000
        },
        "members": [],
        "payments": []
    }


def load_data():
    """Load estate data from the JSON file.

    If the data file does not exist, return a fresh empty
    data structure. If the file exists but contains invalid
    JSON, display an error message and return a fresh structure.
    """

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return create_empty_data()

    except json.JSONDecodeError:
        print("Sorry, the data file appears to be corrupted.")
        print("The existing data could not be loaded.")
        print("The program will start with fresh data.")

        return create_empty_data()


def save_data(data):

    """Save the current estate data to the JSON file."""

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)