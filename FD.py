####Frequency distribution of fruit
fruits = ["apple", "banana", "apple", "orange", "banana",
          "apple", "banana", "orange", "apple", "banana"]

apple_count = 0
banana_count = 0
orange_count = 0

for fruit in fruits:
    if fruit == "apple":
        apple_count += 1
    elif fruit == "banana":
        banana_count += 1
    elif fruit == "orange":
        orange_count += 1
print("Apple  :", apple_count)
print("Banana :", banana_count)
print("Orange :", orange_count)
