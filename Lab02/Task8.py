numbers = [float(input("Введіть число 1: ")),float(input("Введіть число 2: ")),float(input("Введіть число 3: "))]
positive_count = sum(1 for num in numbers if num > 0)
print("Кількість позитивних чисел:", positive_count)