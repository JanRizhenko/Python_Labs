numbers = input("Введіть числа через пробіл: ").split()

sum_of_multiples = 0

for num in numbers:
    number = int(num)
    if number % 18 == 0:
        sum_of_multiples += number

print("Сума чисел, кратних 18:", sum_of_multiples)
