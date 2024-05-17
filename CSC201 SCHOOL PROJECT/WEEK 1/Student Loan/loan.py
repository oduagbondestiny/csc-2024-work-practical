
# Get user input for initial loan amount, annual interest rate, and payback period
# loan_amount = float(input("Enter the initial loan amount: "))  # Example: 25600
# annual_interest_rate = float(input("Enter the annual interest rate (%): "))  # Example: 3.4
# payback_period = int(input("Enter the payback period in years: "))  # Example: 10

# For demonstration, let's use the given values directly
loan_amount = 25600  # Initial loan amount in dollars
annual_interest_rate = 3.4  # Annual interest rate in percentage
payback_period = 10  # Payback period in years

# Convert annual interest rate from percentage to decimal
monthly_interest_rate = annual_interest_rate / 100 / 12

# Calculate the total number of monthly payments
total_payments = payback_period * 12

# Calculate the monthly payment using the loan formula
monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)

# Print the monthly payment amount
print(f"The monthly payment for the loan is: ${monthly_payment:.2f}")
