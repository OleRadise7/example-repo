# Finance Calculators

A small command-line program written in Python that helps a user work out
two common financial calculations.

When the program runs, the user is asked to choose one of two options:

- **investment** – calculates how much an investment will be worth after a
  number of years. The user enters the deposit amount, the interest rate and
  the number of years, then chooses between *simple* and *compound* interest.
- **bond** – calculates the monthly repayment on a home loan (bond). The user
  enters the present value of the house, the annual interest rate and the
  number of months over which the bond will be repaid.

The program uses `if`, `elif` and `else` control structures to decide which
calculation to run, and prints a message if an invalid option is entered.

## How to run

```
python3 finance_calculators.py
```

This program was created as the capstone project for the *Variables and
Control Structures* module of the HyperionDev Software Engineering bootcamp.
