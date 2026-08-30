import bcrypt

USERS = {
    "oga_musty": {
        "name": "Oga Musty",
        "position": "Station Master",
        "password_hash": bcrypt.hashpw(b"stationmaster1", bcrypt.gensalt())
    },
    "kemi_dispatch": {
        "name": "Kemi",
        "position": "Clerk",
        "password_hash": bcrypt.hashpw(b"parcels4kemi", bcrypt.gensalt())
    },
    "ibrahim_k": {
        "name": "Ibrahim",
        "position": "Clerk",
        "password_hash": bcrypt.hashpw(b"fastdelivery", bcrypt.gensalt())
    },
    "ngozi_front": {
        "name": "Ngozi",
        "position": "Clerk",
        "password_hash": bcrypt.hashpw(b"desk2026", bcrypt.gensalt())
    }
}

def login():
    username = input("Username: ").strip()
    password = input("Password: ")

    if username not in USERS:
        print("\n401 — Invalid username or password.")
        return None

    user = USERS[username]

    if bcrypt.checkpw(password.encode(), user["password_hash"]):
        return user

    print("\n401 — Invalid username or password.")
    return None
