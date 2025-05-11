def is_even(number):
    return number % 2 == 0

num = int(input("Введіть число: "))

if is_even(num):
    print("Число парне.")
else:
    print("Число непарне.")
