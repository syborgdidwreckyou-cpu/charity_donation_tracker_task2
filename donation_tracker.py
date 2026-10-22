"""Core functionality for a simple charity donation tracker."""

from decimal import Decimal, InvalidOperation


class DonationTracker:
    """Stores valid donations and calculates the total amount."""

    def __init__(self):
        self.donations = []

    def add_donation(self, amount):
        """Record a positive donation amount.

        Returns True when the donation is recorded, otherwise False.
        Invalid values are rejected without changing the donation list.
        """
        try:
            donation = Decimal(str(amount))
        except (InvalidOperation, ValueError, TypeError):
            return False

        if not donation.is_finite() or donation <= 0:
            return False

        # Store to two decimal places to represent currency values.
        donation = donation.quantize(Decimal("0.01"))
        self.donations.append(donation)
        return True

    def total_donations(self):
        """Return the total of all recorded donations."""
        return sum(self.donations, Decimal("0.00"))

    def donation_count(self):
        """Return the number of accepted donations."""
        return len(self.donations)
