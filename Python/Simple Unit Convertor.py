def convert_units(value, unit_from, unit_to):
    conversions = {
        ('meters', 'feet'): value * 3.28084,
        ('feet', 'meters'): value / 3.28084,
        ('celsius', 'fahrenheit'): (value * 9/5) + 32,
        ('fahrenheit', 'celsius'): (value - 32) * 5/9
    }
    return conversions.get((unit_from, unit_to), "Conversion not available")

def main():
    value = float(input("Enter value to convert: "))
    unit_from = input("Enter unit to convert from (meters, feet, celsius, fahrenheit): ").lower()
    unit_to = input("Enter unit to convert to (meters, feet, celsius, fahrenheit): ").lower()
    result = convert_units(value, unit_from, unit_to)
    print(f"Converted value: {result}")

if __name__ == "__main__":
    main()
