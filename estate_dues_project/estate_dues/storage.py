"""
This is for saving and loading data
"""

import json
from pathlib import Path


DATA_FILE = Path("data.json")


def load_data():
    """Load estate data from the JSON file.

    If the data file does not exist, return a fresh empty
    data structure. If the file exists but contains invalid
    JSON, display an error message and return a fresh structure.
    """
    if not DATA_FILE.exists():
        return {
            "settings": {
                "monthly_dues": 5000
            },
            "members": [],
            "payments": []
        }

    try:
        with DATA_FILE.open("r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Sorry, the data file appears to be corrupted.")
        print("The program will start with fresh data.")

        return {
            "settings": {
                "monthly_dues": 5000
            },
            "members": [],
            "payments": []
        }


def save_data(data):

    """Save the current estate data to the JSON file."""

    with DATA_FILE.open("w") as file:
        json.dump(data, file, indent=4)