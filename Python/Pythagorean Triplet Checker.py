a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("The numbers form a Pythagorean triplet")
else:
    print("The numbers do not form a Pythagorean triplet")
