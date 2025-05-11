numbers = input("Введіть числа через пробіл: ").split()

sum_of_evens = 0

for num in numbers:
    number = int(num)
    if number % 2 == 0:
        sum_of_evens += number

print("Сума парних чисел:", sum_of_evens)
