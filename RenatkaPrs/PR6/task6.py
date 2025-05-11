nums = list(map(int, input("Введіть список чисел: ").split()))
positive_count = sum(1 for x in nums if x > 0)
print("Кількість додатних елементів:", positive_count)
