def square_numbers(*args):
    return [x**2 for x in args]

result = square_numbers(1, 2, 3, 4)
print(f"Квадрати чисел: {result}")
