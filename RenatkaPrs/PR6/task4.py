nums = list(map(int, input("Введіть цілі числа через пробіл: ").split()))
n = int(input("Введіть ціле число: "))

print(f"Числа, що менше {n}:")
print(*[x for x in nums if x < n])