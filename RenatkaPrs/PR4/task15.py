numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

print("Парні елементи списку:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
