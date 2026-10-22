"""Step definitions that connect Gherkin scenarios to the application."""

from behave import given, when, then
from decimal import Decimal

from donation_tracker import DonationTracker


@given("the donation tracker is empty")
def step_tracker_is_empty(context):
    context.tracker = DonationTracker()
    context.last_result = None


@when("a donor records a donation of {amount}")
def step_record_donation(context, amount):
    context.last_result = context.tracker.add_donation(amount)


@then("the donation should be recorded successfully")
def step_donation_recorded(context):
    assert context.last_result is True, "Expected the donation to be accepted"


@then("the system should reject the donation")
def step_donation_rejected(context):
    assert context.last_result is False, "Expected the donation to be rejected"


@then("the donation count should be {expected_count:d}")
def step_donation_count(context, expected_count):
    assert context.tracker.donation_count() == expected_count, (
        f"Expected {expected_count} donations, "
        f"got {context.tracker.donation_count()}"
    )


@given("a donation of {amount} has been recorded")
def step_a_donation_has_been_recorded(context, amount):
    result = context.tracker.add_donation(amount)
    assert result is True, f"Setup donation {amount} should be valid"


@when("the total donations are requested")
def step_request_total(context):
    context.total = context.tracker.total_donations()


@then("the total donations should be {expected_total}")
def step_total_is(context, expected_total):
    assert context.total == Decimal(expected_total), (
        f"Expected total {expected_total}, got {context.total}"
    )
