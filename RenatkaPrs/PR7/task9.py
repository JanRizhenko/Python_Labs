def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Введіть натуральне число: "))

result = factorial(num)

print(f"Факторіал числа {num} дорівнює {result}")
