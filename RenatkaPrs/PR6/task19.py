print("Завдання 19: Перевірка повторів чисел у послідовності")

nums = list(map(int, input("Введіть послідовність чисел: ").split()))
seen = set()

for num in nums:
    if num in seen:
        print(f"{num}: YES")
    else:
        print(f"{num}: NO")
        seen.add(num)
