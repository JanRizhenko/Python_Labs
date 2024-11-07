def filter_list(nums, bottom, upper):
    try:
        MIN = min(nums)
        MAX = max(nums)
        result = [num for num in nums if MIN + bottom <= num <= MAX - upper]
        return result
    except ValueError:
        print("Список не може бути порожнім")
        return []

try:
    nums = list(map(int, input("Введіть список чисел (через пробіл): ").split()))
    bottom = int(input("Введіть нижню межу bottom: "))
    upper = int(input("Введіть верхню межу upper: "))

    filtered_nums = filter_list(nums, bottom, upper)
    print("Отриманий відфільтрований список:", filtered_nums)
except ValueError:
    print("Введено неправильні дані")