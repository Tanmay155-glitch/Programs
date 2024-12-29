a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD Calculation
x, y = a, b
while y:
    x, y = y, x % y
gcd = x
lcm = a * b // gcd

print(f"GCD of {a} and {b} is {gcd}")
print(f"LCM of {a} and {b} is {lcm}")
