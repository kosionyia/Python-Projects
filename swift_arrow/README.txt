SWIFT ARROW COURIERS

Run:
1. Install bcrypt:
   pip install bcrypt

2. Make sure parcels.json is in the same folder.

3. Run:
   python main.py

Rooms:
- main.py: receives commands and displays replies.
- storage.py: loads and saves parcels.json.
- index.py: creates fast indexes for tracking codes and cities.
- cache.py: stores the 10 most recent answers.
- auth.py: handles staff login using bcrypt password hashes.

This version intentionally skips the Day Pass and all Part C features, as requested.

Index:
The tracking index connects a tracking code to the parcel's position in the list, 
so GET parcel does not scan the whole ledger.

Cache:
The cache keeps the 10 most recent answers. Repeating a question can return the saved answer immediately. 
The cache is cleared whenever parcel data changes so old answers are not used.

Hashing:
bcrypt is used for passwords. It stores a scrambled password fingerprint instead of readable passwords. 
When a user signs in, bcrypt checks the typed password against the stored fingerprint.

HASHING - BCRYPT - WHY I USED It.
I used bycrypt because it automatically uses a salt, 
meaning identical passwords do not simply produce identical stored hashes.
Most importantly it is was designed specifically for securely storing passwords 
and it is quite simple to use with python