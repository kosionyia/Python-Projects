from datetime import datetime
LOG_FILE = "window_ledger.txt"

def log (username, request, code):
    time = datetime.now().strftime()

    with open(LOG_FILE, "a") as file:
        file.write(f"{time} | {username} | {request} | {code}")