numbers = list(map(int, input("Введіть список чисел через пробіл: ").split()))

positive_numbers = [num for num in numbers if num > 0]
other_numbers = [num for num in numbers if num <= 0]

print("Додатні елементи:", positive_numbers)
print("Інші елементи:", other_numbers)