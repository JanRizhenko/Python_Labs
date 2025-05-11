variant = 18
numbers = [10, -5, 3, -18, 12, 6, -9, 18, -20, 25, -8, 15]

sum = 0

for num in numbers:
    if -variant <= num <= variant:
        sum += num

print("Сума елементів у діапазоні від", -variant, "до", variant, "=", sum)
