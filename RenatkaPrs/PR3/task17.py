numbers = input("Введіть числа через пробіл: ").split()
numbers = [float(num) for num in numbers]

if numbers:
    print("Максимальне значення:", max(numbers))
    print("Мінімальне значення:", min(numbers))
else:
    print("Список порожній.")
