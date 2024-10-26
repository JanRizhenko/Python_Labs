A = int(input("Введіть число A: "))
B = int(input("Введіть число B: "))

if A < B:
    total_sum = 0
    for i in range(A, B + 1):
        total_sum += i
    print("Сума всіх чисел від", A, "до", B, "включно:", total_sum)
else:
    print("Помилка: A має бути менше за B.")