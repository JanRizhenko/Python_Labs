nums = list(map(int, input("Введіть список чисел: ").split()))
even_nums = [x for x in nums if x % 2 == 0]
print("Парні елементи списку:", *even_nums)
