def find_divisible_numbers(n, divisors):
    return [i for i in range(1, n + 1) if all(i % d == 0 for d in divisors)]

n = int(input("Введіть число n: "))
divisors = list(map(int, input("Введіть числа, на які повинні ділитися знайдені числа, через пробіл: ").split()))

result = find_divisible_numbers(n, divisors)
print(f"Натуральні числа, що не перевищують {n} і діляться на всі задані числа: {result}")