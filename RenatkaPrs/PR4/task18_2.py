numbers_str = input("Введіть числа, розділені комами: ")

numbers_list = [int(num) for num in numbers_str.split(",")]
numbers_tuple = tuple(numbers_list)

print(f"Список: {numbers_list}")
print(f"Кортеж: {numbers_tuple}")