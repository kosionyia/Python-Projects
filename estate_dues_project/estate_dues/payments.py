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


def get_monthly_payment_total(data, member_id, month):
    """Return the total amount a member has paid for a specific month."""

    payments = get_member_payments(data, member_id)

    total = 0

    for payment in payments:
        if payment["month"] == month:
            total += payment["amount"]
    return total


def get_payment_status(data, member_id, month):
    """Return the payment status for a member for a specific month."""

    monthly_dues = data["settings"]["monthly_dues"]

    paid = get_monthly_payment_total(data, member_id, month)

    balance = monthly_dues - paid

    if paid == 0:
        status = "OWING"
    elif paid < monthly_dues:
        status = "INSTALLMENT"
    else:
        status = "UP TO DATE"

    return {
        "paid": paid,
        "balance": max(balance, 0),
        "status": status
    }