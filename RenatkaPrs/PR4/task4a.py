numbers = [8, 15, 11, 3, 8, 10, 11, 25, 8, 5, 11, 9]

count = 0

for num in numbers:
    if num == 8 or num == 11:
        count += 1
        print(" num = ", num, " count = ", count)

print("Кількість елементів, що дорівнюють 8 або 11:", count)
