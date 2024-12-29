print("Choose shape: 1. Circle  2. Rectangle  3. Triangle")
choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    radius = float(input("Enter radius of circle: "))
    area = 3.1416 * radius * radius
    print("Area of circle:", area)
    
elif choice == 2:
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
    print("Area of rectangle:", area)
    
elif choice == 3:
    base = float(input("Enter base of triangle: "))
    height = float(input("Enter height of triangle: "))
    area = 0.5 * base * height
    print("Area of triangle:", area)
    
else:
    print("Invalid choice")
