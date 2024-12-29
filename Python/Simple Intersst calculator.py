def calculate_simple_interest(principal, rate, time):
    return principal * rate * time / 100

def main():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (in %): "))
    time = float(input("Enter time (in years): "))
    interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple interest: {interest}")

if __name__ == "__main__":
    main()
