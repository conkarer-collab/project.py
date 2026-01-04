###### List of ages
ages = [10, 12, 14, 16, 18]

# Calculate Mean (Average)
total = 0
for age in ages:
    total = total + age

mean = total / len(ages)

# Calculate Median (Middle value)
ages.sort()
middle_index = len(ages) // 2
median = ages[middle_index]

print("Ages:", ages)
print("Mean:", mean)
print("Median:", median)

