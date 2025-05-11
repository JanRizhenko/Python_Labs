numbers = list(map(int, input("Введіть числа через пробіл (від 0 до 10): ").split()))

print("Елементи з парними індексами:")
for i in range(0, len(numbers), 2):
    print(numbers[i], end=" ")
