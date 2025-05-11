numbers = [12, 7, 8, 5, 9, 8, 15, 3, 8, 10, 6, 8, 4]

number = int(input("Введіть ціле число: "))

count_greater = sum(1 for num in numbers if num > number)

count_less = sum(1 for num in numbers if num < number)

count_not_greater = sum(1 for num in numbers if num <= number)

count_not_less = sum(1 for num in numbers if num >= number)

count_equal = sum(1 for num in numbers if num == number)

count_not_equal = sum(1 for num in numbers if num != number)

print(f"Кількість елементів більших за {number}: {count_greater}")
print(f"Кількість елементів менших за {number}: {count_less}")
print(f"Кількість елементів, не більших за {number}: {count_not_greater}")
print(f"Кількість елементів, не менших за {number}: {count_not_less}")
print(f"Кількість елементів, дорівнюють {number}: {count_equal}")
print(f"Кількість елементів, не дорівнюють {number}: {count_not_equal}")
