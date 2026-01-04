
# Mini Statistical Analyzer

# Step 1: Take dataset input from user
data_input = input("Enter numbers separated by space: ")
data = data_input.split()  # Split input into list of strings
data = [int(x) for x in data]  # Convert strings to integers

# Frequency Distribution

freq = {}
for num in data:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("\nFrequency Distribution:")
for key in freq:
    print(f"{key}: {freq[key]}")


# Mean

mean = sum(data) / len(data)
print("\nMean:", mean)


# Median

data_sorted = sorted(data)
n = len(data_sorted)
middle = n // 2
if n % 2 == 0:
    median = (data_sorted[middle - 1] + data_sorted[middle]) / 2
else:
    median = data_sorted[middle]
print("Median:", median)

# -------------------------------
# Mode
# -------------------------------
max_freq = max(freq.values())
mode = [k for k, v in freq.items() if v == max_freq]
print("Mode:", mode)

# -------------------------------
# Range
# -------------------------------
data_range = max(data) - min(data)
print("Range:", data_range)

# -------------------------------
# Variance
# -------------------------------
squared_diff = [(x - mean)**2 for x in data]
variance = sum(squared_diff) / len(data)
print("Variance:", variance)

# -------------------------------
# Standard Deviation
# -------------------------------
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)

# -------------------------------
# Optional: Simple Histogram
# -------------------------------
print("\nHistogram:")
for key in sorted(freq):
    print(f"{key}:", "*" * freq[key])











