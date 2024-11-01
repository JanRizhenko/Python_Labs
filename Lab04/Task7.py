import random

numbers = [round(random.uniform(-100, 100), 2) for _ in range(30)]

min_abs_element = min(numbers, key=abs)

print("Мінімальний по модулю елемент:", min_abs_element)
print("Список в порядку зростання:", sorted(numbers))