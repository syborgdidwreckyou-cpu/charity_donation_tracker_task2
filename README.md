# Charity Donation Tracker

A small Python application for a non-profit charity to record positive donation amounts and calculate the total received. This project demonstrates Behaviour-Driven Development (BDD) using Gherkin and `behave`.

## Requirements

- Python 3.9 or newer
- `behave`

## Run the BDD tests

From the project root directory, install the test framework:

```bash
python -m pip install behave
```

Then run:

```bash
python -m behave
```

The feature file contains three scenarios:
1. A valid donation is accepted.
2. A negative donation is rejected.
3. The total of two valid donations is calculated correctly.

## Project files

- `donation_tracker.py` — application logic.
- `features/donations.feature` — Gherkin acceptance scenarios.
- `features/steps/donation_steps.py` — Python step definitions used by `behave`.

## Scope and limitations

This is an educational prototype. It does not process real payments, store data permanently, or replace a charity's accounting system. Donations are held in memory and are lost when the program ends.
