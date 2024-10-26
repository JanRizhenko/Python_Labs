A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

if A < B:
    sum_squares = 0
    for i in range(A, B + 1):
        sum_squares += i ** 2
    print("Сума квадратів всіх чисел від", A, "до", B, "включно:", sum_squares)
else:
    print("Помилка: A має бути менше за B.")