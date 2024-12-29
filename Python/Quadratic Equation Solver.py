import cmath

def solve_quadratic(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    roots = solve_quadratic(a, b, c)
    print(f"Roots of the quadratic equation: {roots[0]} and {roots[1]}")

if __name__ == "__main__":
    main()
