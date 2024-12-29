cart = {}
total_price = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item == 'done':
        break
    price = float(input(f"Enter price for {item}: "))
    quantity = int(input(f"Enter quantity for {item}: "))
    cart[item] = price * quantity
    total_price += price * quantity

print("Shopping Cart:")
for item, cost in cart.items():
    print(f"{item}: ${cost:.2f}")
print(f"Total price: ${total_price:.2f}")
