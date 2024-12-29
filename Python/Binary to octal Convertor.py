binary = input("Enter binary number: ")
decimal = int(binary, 2)
octal = oct(decimal)[2:]

print(f"Octal equivalent: {octal}")
