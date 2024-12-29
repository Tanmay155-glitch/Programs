import random

def generate_random_number(start, end):
    return random.randint(start, end)

def main():
    start = int(input("Enter the start range: "))
    end = int(input("Enter the end range: "))
    print(f"Random number between {start} and {end}: {generate_random_number(start, end)}")

if __name__ == "__main__":
    main()
