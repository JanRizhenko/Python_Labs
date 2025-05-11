import math

print("Прості числа від 1 до 80:")

for num in range(2, 81):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print()
