import random

numbers = [random.randint(1, 100) for _ in range(30)]

print("Згенеровані числа:")
for num in numbers:
    print(num, end=", ")
print()

count = 0
for num in numbers:
    if num % 2 == 0 and num % 3 == 0:
        count += 1

print("Кількість парних чисел, кратних 3:", count)
