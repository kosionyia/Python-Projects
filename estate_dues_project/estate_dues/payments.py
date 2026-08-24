"""
This is for recording payments, getting a member's payment history, determining
who has paid and who is owing.
"""

from datetime import datetime
from estate_dues.members import get_member


def record_payment(data, member_id, month, amount):
    """Record a dues payment for an existing member."""

    member = get_member(data, member_id)

    if member is None:
        return None

    if data["payments"]:
        highest_id = max(
            payment["id"] for payment in data["payments"]
        )
        new_id = highest_id + 1
    else:
        new_id = 1

    date_paid = datetime.now().strftime("%Y-%m-%d")

    payment = {
        "id": new_id,
        "member_id": member_id,
        "month": month,
        "amount": amount,
        "date_paid": date_paid
    }
    data["payments"].append(payment)
    return payment


def get_member_payments(data, member_id):
    """Return all payments made by a specific member."""

    payments = []

    for payment in data["payments"]:
        if payment["member_id"] == member_id:
            payments.append(payment)

    return payments