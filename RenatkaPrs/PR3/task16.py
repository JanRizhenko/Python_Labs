numbers = input("Введіть числа через пробіл: ").split()
numbers = [float(num) for num in numbers]

if numbers:
    average = sum(numbers) / len(numbers)
    print("Середнє арифметичне:", average)
else:
    print("Список порожній.")
