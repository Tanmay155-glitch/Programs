print("Unit Converter")
value = float(input("Enter value: "))
print("Choose conversion: 1. Meters to Kilometers  2. Grams to Kilograms")
choice = int(input("Enter choice (1/2): "))

if choice == 1:
    print(f"{value} meters is {value / 1000} kilometers")
elif choice == 2:
    print(f"{value} grams is {value / 1000} kilograms")
else:
    print("Invalid choice")
