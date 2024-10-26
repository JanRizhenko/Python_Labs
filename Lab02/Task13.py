a = int(input("Введіть число a (0 ≤ a ≤ 50): "))

if 0 <= a <= 50:
    total_sum = 0
    for i in range(a, 51):
        total_sum += i ** 2
    print("Сума квадратів чисел від", a, "до 50:", total_sum)
else:
    print("Помилка: значення a повинно бути в межах від 0 до 50.")