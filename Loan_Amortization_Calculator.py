# Grace Hamdorf

# Loan Amoritization Project

#   User Inputs

# loan amount
loan_amount = float(input("Loan amount ($):"))

# annual interest rate written as a %
annual_interest_rate = float(input("Annual interest rate (%):"))

# length of loan in years
length_loan = float(input("Length of your loan (in years):"))


#   Calculations

# convert annual interest rate to a decimal
annual_interest_decimal = annual_interest_rate / 100

# convert the annual rate to a monthly rate
monthly_rate = annual_interest_decimal / 12

# convert the number of payments to months
number_payments = length_loan * 12


#   Calculate Constant Monthly Payment
monthly_pmt = (
    loan_amount
    * (monthly_rate * (1 + monthly_rate) ** number_payments)
    / ((1 + monthly_rate) ** number_payments - 1)
)
print(f"Monthly Payment: ${monthly_pmt:,.2f}")


#   Header Formatting
print(" ")

print(
    f"{'Month':8} {'Payment':<10} {'Principal':<10} {'Interest':<10} {'Balance':<10}"
)


#   While Loop For Each Month
count = 1

while count <= number_payments:
    payment = monthly_pmt
    interest = loan_amount * monthly_rate
    principal = monthly_pmt - interest
    balance = loan_amount - principal
    print(
        f"{count:<8} ${payment:<10,.2f} ${principal:<10,.2f} ${interest:<10,.2f} ${balance:<10,.2f}"
    )
    count += 1
    loan_amount = balance
