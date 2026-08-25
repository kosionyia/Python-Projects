USERS = {
"mrs_okafor": {
    "password": "library2024",
    "role": "Chief Librarian" 
}, 
"bello_jr": {
    "password": "windowboy",
    "role": "Member" 
}, 
"amina_s": {
    "password": "books4life",
    "role": "Member" 
}, 
"tunde_reads": {
    "password": "password123",
    "role": "Member" 
}, 
"chichi_o": {
    "password": "novels!",
    "role": "Member" 
}, 
"baba_musa": {
    "password": "retired55",
    "role": "Member" 
}, 
}

def login(username, password):
    """Check a username and password and return the user's information."""
    
    if username not in USERS:
        return None

    if USERS[username]["password"] != password:
        return None

    return {
        "username": username,
        "role": USERS[username]["role"]
    }


def authenticate():
    """Ask the visitor for login details.

    The visitor gets a maximum of three attempts.
    Returns the authenticated user or None if all attempts fail.
    """

    attempts = 0
    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")

        user = login(username, password)

        if user is not None:
            print("\n200 — Sign in successful.")
            return user

        attempts += 1
        print("\n401 — Sign in failed. Enter correct details")
        print(f"You have {3 - attempts} attempts remaining.\n")

    print("403 — Three failed attempts. The grille is closed.")
    return None


def can_delete(user):
    """Return True only if the user is the Chief Librarian."""
    
    return user["role"] == "Chief Librarian"




