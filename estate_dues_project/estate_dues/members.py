"""
This is responsible forr member registration, finding a member and the list of members.
"""
def add_member(data, name, phone):

    """Add a new member to the estate."""

    if data["members"]:
        highest_id = max(member["id"] for member in data["members"])
        new_id = highest_id + 1
    else:
        new_id = 1

    member = {
        "id": new_id,
        "name": name,
        "phone": phone
    }

    data["members"].append(member)

    return member


def get_member(data, member_id):
    for member in data["members"]:
        if member["id"] == member_id:
            return member

    return None


def get_all_members(data):

    """Return all registered members."""

    return data["members"]
    