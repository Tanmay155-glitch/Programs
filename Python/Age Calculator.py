from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    age = calculate_age(birthdate)
    print(f"Your age is: {age} years")

if __name__ == "__main__":
    main()
