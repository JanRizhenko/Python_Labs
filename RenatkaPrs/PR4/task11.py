numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

numbers = numbers[-2:] + numbers[:-2]

print("Список після переміщення двох останніх елементів:", numbers)
