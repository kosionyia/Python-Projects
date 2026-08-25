ESTATE UNION DUES TRACKER
=========================

DESCRIPTION
-----------
The Estate Union Dues Tracker is a Python program
for managing residents' monthly estate dues.

The program allows the chairman to:

- Register members
- Automatically assign member IDs
- Record dues payments
- Record installment payments (payment for the same month, more than once.)
- View all members
- View a member's payment history
- Check whether a member is owing, paid in installment, or is up to date
- Keep data after the program is closed and restarted
- Keep a readable diary of registrations and payments


FOLDER STRUCTURE
----------------

main.py
    The main program file. It displays the menu and coordinates
    the functions from the estate_dues package.

estate_dues/
    The Python package containing the program modules.

    __init__.py
        Identifies estate_dues as a Python package.

    storage.py
        Loads data from data.json and saves data back to the file.

    members.py
        Handles registering members, finding members, and
        retrieving all members.

    payments.py
        Handles recording payments, payment history,
        and payment status.

    logger.py
        Records timestamped events in estate_log.txt.

data.json
    Stores members, payments, and monthly dues so that the
    information survives when the program is closed.

estate_log.txt
    A plain-text diary containing timestamped registrations
    and payment events.


HOW TO RUN
----------

1. Make sure Python is installed.

2. Open a terminal in the project folder.

3. Run:

    python main.py

4. Follow the menu instructions.


DATA CONSISTENCY
----------------

The program saves information to data.json.

If data.json does not exist when the program is run for the
first time, the program creates a fresh empty data structure.

If data.json contains invalid or corrupted JSON, the program
handles the problem gracefully instead of crashing.


PAYMENT INSTALLMENTS
--------------------

Members can make more than one payment toward the same month.

For example, if monthly dues are ₦5,000, a member can pay:

    ₦2,000

and later:

    ₦3,000

The program adds the payments together when calculating the
member's monthly payment status.


LOGGING
-------

Registrations and payments are recorded in estate_log.txt.

The log file uses append mode so that new events are added to
the end of the file without deleting previous events.