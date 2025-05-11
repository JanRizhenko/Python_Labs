numbers = [10, 15, 20, 33, 50, 100, 8, 25, 3, 60]

generator = [num ** 2 for num in numbers if num % 5 == 0]

for num in generator:
    print(num)