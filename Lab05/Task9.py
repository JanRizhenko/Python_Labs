import time
import random
import math

# Декоратор для вимірювання часу виконання
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

# Завдання 6: Пошук числа з найбільшою кількістю дільників
def count_divisors(num):
    divisors = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors += 1
            if i != num // i:
                divisors += 1
    return divisors

@timer
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

# Завдання 7: Пошук простих чисел
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@timer
def find_primes(N, format_type='list'):
    primes = [i for i in range(2, N + 1) if is_prime(i)]

    if format_type == 'list':
        print(" ".join(map(str, primes)))
    elif format_type == 'column':
        for prime in primes:
            print(prime)
    elif format_type == 'count':
        print(f"Кількість простих чисел: {len(primes)}")

# Завдання 8: Фільтрація списку чисел
@timer
def filter_list(nums, bottom, upper):
    try:
        MIN = min(nums)
        MAX = max(nums)
        result = [num for num in nums if MIN + bottom <= num <= MAX - upper]
        return result
    except ValueError:
        print("Список не може бути порожнім")
        return []

# Тестування для різних значень n
for n in range(1, 7):
    size = 10 ** n
    print(f"Тестування для {size} елементів:")

    # Тест для завдання 6
    M = 1
    N = size
    print("Завдання 6:")
    find_number_with_max_divisors(M, N)

    # Тест для завдання 7
    print("Завдання 7:")
    find_primes(size, 'count')

    # Тест для завдання 8
    nums = random.sample(range(1, size + 1), size)
    bottom, upper = random.randint(1, size // 10), random.randint(1, size // 10)
    print("Завдання 8:")
    filter_list(nums, bottom, upper)

    print("=" * 75)
