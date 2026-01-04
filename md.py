# Dataset (daily temperatures)
temps = [20, 22, 24, 26]

# Range
highest = max(temps)
lowest = min(temps)
data_range = highest - lowest

# Mean
total = 0
for t in temps:
    total = total + t
mean = total / len(temps)

# Variance
sum_of_squares = 0
for t in temps:
    diff = t - mean
    sum_of_squares = sum_of_squares + (diff * diff)

variance = sum_of_squares / len(temps)

# Standard Deviation
std_dev = variance ** 0.5

# Results
print("Temperatures:", temps)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
