numbers = [3, 7, 2, 8, 5, 9, 1]

min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

if min_index > max_index:
    min_index, max_index = max_index, min_index

sum_between = sum(numbers[min_index+1:max_index])

print("Сума елементів між мінімальним та максимальним:", sum_between)
