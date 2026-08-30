import json
import os

DATA_FILE = "parcels.json"

def load_parcels():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("\n400 — Could not read parcels.json. Starting with an empty ledger.")
        return []

def save_parcels(parcels):
    with open(DATA_FILE, "w") as file:
        json.dump(parcels, file, indent=2)
