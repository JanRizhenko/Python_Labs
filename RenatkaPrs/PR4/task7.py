numbers = [1, 5, 7, 2, 5, 3, 7, 8, 9, 5]

sum = sum(num for num in numbers if num == 5 or num == 7)

print("Сума елементів, які дорівнюють 5 або 7:", sum)
