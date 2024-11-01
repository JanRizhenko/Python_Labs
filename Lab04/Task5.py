import random

numbers = [random.randint(-100, 100) for _ in range(30)]

negative_pairs = [(numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1) if numbers[i] < 0 and numbers[i + 1] < 0]

print("Список:", numbers)
print("Пари від’ємних чисел поруч:", negative_pairs)