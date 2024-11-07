def count_divisors(num):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    return divisors

def find_number_with_max_divisors(M, N):
    max_divisors = 0
    numbers = []
    for i in range(M, N + 1):
        divisors = count_divisors(i)
        if divisors > max_divisors:
            max_divisors = divisors
            numbers = [i]
        elif divisors == max_divisors:
            numbers.append(i)
    return numbers, max_divisors

M = int(input("Введіть початок інтервалу M: "))
N = int(input("Введіть кінець інтервалу N: "))

numbers, max_divisors = find_number_with_max_divisors(M, N)
print("Числа з найбільшою кількістю дільників:", numbers)
print(f"Кількість дільників: {max_divisors}")