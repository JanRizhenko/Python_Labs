expr = input("Введіть вираз (наприклад, '20 plus 7'): ")
a_str, op, b_str = expr.split()
a = int(a_str)
b = int(b_str)

if op == "plus":
    result = a + b
elif op == "minus":
    result = a - b
elif op == "multiply":
    result = a * b
elif op == "divide":
    result = a // b
else:
    result = "Невідомий оператор"

print("Результат:", result)
