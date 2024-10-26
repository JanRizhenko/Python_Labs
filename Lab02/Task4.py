import math

numbers = [float(input("Введіть значення 1:")),float(input("Введіть значення 2:")),float(input("Введіть значення 3:")),float(input("Введіть значення 4:"))]
min_number = min(numbers)
cos_min_number = math.cos(min_number)
print(f"Косинус мінімального числа ({min_number}): {cos_min_number}")