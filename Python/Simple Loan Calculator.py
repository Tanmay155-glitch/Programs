principal = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (in %): "))
years = int(input("Enter loan term (in years): "))

monthly_rate = rate / 12 / 100
num_payments = years * 12
monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** -num_payments)

print(f"Your monthly payment is: {monthly_payment:.2f}")
