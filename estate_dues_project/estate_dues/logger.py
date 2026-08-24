"""
This is our diary, where we log what has happened
and the time stap too.
"""

from datetime import datetime
from pathlib import Path


LOG_FILE = Path("estate_log.txt")


def log_event(message):
    """Add a timestamped event to the estate log."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with LOG_FILE.open("a") as file:
        file.write(f"{timestamp} - {message}\n")