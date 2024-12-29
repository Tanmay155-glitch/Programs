import numpy as np

# Given numbers
numbers = [20, 22, 19, 24, 23, 21, 25]

# Calculate the mean
mean = np.mean(numbers)

# Calculate the deviations from the mean
deviations = [num - mean for num in numbers]

# Calculate the squared deviations
squared_deviations = [dev ** 2 for dev in deviations]

# Calculate the sum of squared deviations
sum_squared_deviations = sum(squared_deviations)

# Calculate the sample variance
sample_variance = sum_squared_deviations / (len(numbers) - 1)

# Calculate the sample standard deviation
sample_std_dev = np.sqrt(sample_variance)

print("Mean is:",mean)
print("Sample Variance:", sample_variance)
print("Sample Standard Deviation:",sample_std_dev)
