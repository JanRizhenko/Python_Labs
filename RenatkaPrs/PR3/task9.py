import random

numbers = [random.randint(1, 100) for _ in range(20)]

print("Згенеровані числа:")
for num in numbers:
    print(num, end=", ")

print()

count = 0
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        count += 1

print("Кількість чисел, що діляться на 3 і 5:", count)
