import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    print(f"Rolled a {sides}-sided dice: {roll_dice(sides)}")

if __name__ == "__main__":
    main()
