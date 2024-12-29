arr = [int(x) for x in input("Enter sorted list of numbers: ").split()]
target = int(input("Enter the number to search: "))

low, high = 0, len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print(f"Number {target} found at index {mid}")
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(f"Number {target} not found")
