def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(N, format_type='list'):
    primes = [i for i in range(2, N + 1) if is_prime(i)]

    if format_type == 'list':
        print(" ".join(map(str, primes)))
    elif format_type == 'column':
        for prime in primes:
            print(prime)
    elif format_type == 'count':
        print(f"Кількість простих чисел: {len(primes)}")

N = int(input("Пошук всіх простих чисел від 0 до "))
format_type = input("Виберіть формат виведення результату (list/column/count): ")
find_primes(N, format_type)