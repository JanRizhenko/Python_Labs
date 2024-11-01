import random

numbers = [random.randint(-100, 100) for _ in range(30)]

max_element = max(numbers)
max_index = numbers.index(max_element)

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Список:", numbers)
print("Максимальний елемент:", max_element, "\nІндекс максимального елемента:", max_index)
if odd_numbers:
    print("Список непарних чисел в порядку зменшення:", sorted(odd_numbers, reverse=True))
else:
    print("Непарних чисел немає")