max_of_two = lambda x, y: x if x > y else y

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
result = max_of_two(num1, num2)
print(f"Більше число: {result}")
