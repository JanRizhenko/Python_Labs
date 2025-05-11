nums = list(map(int, input("Введіть список чисел: ").split()))
squares = [x**2 for x in nums]
print("Квадрати чисел:", *squares)
