# Dataset
x = [1, 2, 3]
y = [2, 4, 6]

# Number of points
n = 3

# Calculate sums manually
sum_x = x[0] + x[1] + x[2]
sum_y = y[0] + y[1] + y[2]
sum_xy = x[0]*y[0] + x[1]*y[1] + x[2]*y[2]
sum_x2 = x[0]*x[0] + x[1]*x[1] + x[2]*x[2]

# Calculate slope (m)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

# Calculate intercept (b)
b = (sum_y - m * sum_x) / n

# Print slope and intercept
print("Slope (m):", m)
print("Intercept (b):", b)

# Predict y for x = 4
x_value = 4
y_value = m * x_value + b
print("Prediction for x =", x_value, "is y =", y_value)
