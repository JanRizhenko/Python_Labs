numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
n = int(input("Введіть число n: "))

print("Елементи, що менші за n:")
for num in numbers:
    if num < n:
        print(num, end=" ")
