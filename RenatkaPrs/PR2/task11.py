a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, /, *, mod, pow, div): ")

if operation == '+':
    print("Результат:", a + b)
elif operation == '-':
    print("Результат:", a - b)
elif operation == '*':
    print("Результат:", a * b)
elif operation == '/':
    if b == 0:
        print("Ділення на 0!")
    else:
        print("Результат:", a / b)
elif operation == 'mod':
    if b == 0:
        print("Ділення на 0!")
    else:
        print("Результат:", a % b)
elif operation == 'pow':
    print("Результат:", a ** b)
elif operation == 'div':
    if b == 0:
        print("Ділення на 0!")
    else:
        print("Результат:", a // b)
else:
    print("Невідома операція!")
