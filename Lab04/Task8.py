import random

numbers = [round(random.uniform(-100, 100),2) for _ in range(30)]

split_lists = [numbers[i:i + 3] for i in range(0, 30, 3)]

sorted_split_lists = sorted(split_lists, key=lambda x: sum(abs(num) for num in x))

print("Список з 10 списків по 3 елементи, відсортований за сумою модулів:")
for lst in sorted_split_lists:
    print(lst)