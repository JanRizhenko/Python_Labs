import math

numbers = [1, 4, 9, 16, 25, 30, 36, 49, 50, 64, 81, 100, 121]

generator = [num for num in numbers if int(math.sqrt(num)) ** 2 == num]

for num in generator:
    print(num)