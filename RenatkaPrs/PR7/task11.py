def sum_of_numbers(*args):
    if not args:
        return 0
    return sum(args)

result = sum_of_numbers(1, 2, 3, 4)
print(f"Сума чисел: {result}")

result_no_args = sum_of_numbers()
print(f"Сума без чисел: {result_no_args}")
