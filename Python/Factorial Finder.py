import math

def factorial(n):
    return math.factorial(n)

def main():
    n = int(input("Enter a number to find its factorial: "))
    print(f"Factorial of {n}: {factorial(n)}")

if __name__ == "__main__":
    main()
