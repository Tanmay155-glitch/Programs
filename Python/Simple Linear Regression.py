# Hardcoded dataset
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([x[i] * y[i] for i in range(n)])
sum_xx = sum([x[i] ** 2 for i in range(n)])

slope = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x ** 2)
intercept = (sum_y - slope * sum_x) / n

print(f"y = {slope:.2f}x + {intercept:.2f}")
