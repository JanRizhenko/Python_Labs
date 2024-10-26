a = int(input("Введіть число a (a ≤ 200): "))
b = int(input("Введіть число b: "))

if a <= 200:
    total_sum = 0
    count = 0
    for i in range(a, b + 1):
        total_sum += i
        count += 1
    if count > 0:
        average = total_sum / count
        print("Середнє арифметичне чисел від", a, "до", b, ":", average)
    else:
        print("Діапазон порожній.")
else:
    print("Помилка: значення a повинно бути менше або дорівнювати 200.")