a = int(input("Введіть число a: "))
b = int(input("Введіть число b (b ≥ a): "))

if b >= a:
    total_sum = 0
    current = a
    while current <= b:
        total_sum += current
        current += 1
    print("Сума всіх цілих чисел від", a, "до", b, "включно:", total_sum)
else:
    print("Помилка: значення b повинно бути більше або дорівнювати a.")