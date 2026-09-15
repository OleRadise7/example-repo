

# Import the math module to use mathematical functions
import math



# DISPLAY MAIN MENU

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")
print("Enter either 'investment' or 'bond' from the menu above to proceed:")

# Get user input - input is Case insensitive using .strip() remives extra spaces, and .lower() converts the input to lowercases
user_choice = input().strip().lower()

# INVESTMENT CALCULATOR
if user_choice == "investment":

    # Get deposit amount from user. used a float instead of integers because we are working with money and decimals
    P = float(input("Enter the amount of money you are depositing: "))

    # Get interest rate as a percentage %
    interest_rate = float(input("Enter the interest rate (as a percentage): "))

    # Convert percentage to decimal
    r = interest_rate / 100

    # Get number of years that the money is being invested. Question: Can this also be a float e.g 2.5 years?
    t = int(input("Enter the number of years you plan on investing: "))

    # Ask users if they want simple or compound interest
    interest = input("Do you want 'simple' or 'compound' interest? ").strip().lower()

    # SIMPLE INTEREST
    if interest == "simple":
        # Formula: A = P * (1 + r * t)
        A = P * (1 + r * t)
        print(f"\nTotal amount after {t} years (Simple Interest): R{A:.2f}")

    # COMPOUND INTEREST
    elif interest == "compound":
        # Formula: A = P * (1 + r)^t
        A = P * math.pow((1 + r), t)
        print(f"\nTotal amount after {t} years (Compound Interest): R{A:.2f}")

    else:
        print("Invalid interest type entered. Please choose 'simple' or 'compound'.")


# BOND CALCULATOR
elif user_choice == "bond":

    # Get present value of the house
    P = float(input("Enter the present value of the house: "))

    # Get annual interest rate
    annual_interest = float(input("Enter the annual interest rate (as a percentage): "))

    # Convert annual interest rate to monthly decimal rate
    i = (annual_interest / 100) / 12

    # Get number of months for repayment
    n = int(input("Enter the number of months you plan to repay the bond: "))

    # Bond repayment formula:
    # repayment = (i * P) / (1 - (1 + i)**(-n))
    repayment = (i * P) / (1 - (1 + i) ** (-n))

    print(f"\nYour monthly bond repayment will be: R{repayment:.2f}")



# INVALID INPUT

else:
    print("Invalid selection. Please restart the program and enter either 'investment' or 'bond'.")

    # END Program