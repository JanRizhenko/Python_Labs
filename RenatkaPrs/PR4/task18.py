numbers = list(map(int, input("Введіть послідовність чисел через пробіл: ").split()))

min_num = min(numbers)
max_num = max(numbers)
count = len(numbers)
average = sum(numbers) / count

print(f"Найменше число: {min_num}")
print(f"Найбільше число: {max_num}")
print(f"Кількість чисел у списку: {count}")
print(f"Середнє значення: {average}")
