import random

numbers = [random.randint(-10, 10) for _ in range(20)]

odd_index_sum = sum(numbers[i] for i in range(1, len(numbers), 2))

print("Список:", numbers)
print("Сума елементів з непарними індексами:", odd_index_sum)