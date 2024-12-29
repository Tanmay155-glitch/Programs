bill = float(input("Enter the bill amount: "))
tip_percentage = int(input("Enter the tip percentage: "))
tip = bill * (tip_percentage / 100)
total = bill + tip

print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")
