numbers = list(map(int, input("Введіть 10 чисел через пробіл: ").split()))

max_element = max(numbers)

squared_smaller = sorted([num ** 2 for num in numbers if num < max_element], reverse=True)

print("Максимальний елемент:", max_element)
print("Квадрати менших чисел в порядку зменшення:", squared_smaller)