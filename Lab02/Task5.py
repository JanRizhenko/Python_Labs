import math

numbers = [float(input("Введіть число 1: ")),float(input("Введіть число 2: ")),float(input("Введіть число 3: "))]
max_number = max(numbers)
sin_max_number = math.sin(max_number)
print(f"Синус максимального числа({max_number}):", sin_max_number)