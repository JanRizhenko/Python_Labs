numbers = [10, -5, 3, -18, 12, 6, -9, 18, -20, 25, -8, 15, 0, 4, -3]

count = 0

for num in numbers:
    if -5 <= num <= 5:
        count += 1
        print(" num = ", num, " count = ", count)

print("Кількість елементів у діапазоні від -5 до 5:", count)