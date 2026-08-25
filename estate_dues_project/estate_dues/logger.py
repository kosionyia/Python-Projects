"""
This is our diary, where we log what has happened
and the time stap too.
"""

from datetime import datetime


LOG_FILE = "estate_log.txt"


def log_event(message):
    """Add a timestamped event to the estate log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} - {message}\n")