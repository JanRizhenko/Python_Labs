numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

unique_elements = [num for num in numbers if numbers.count(num) == 1]

print("Елементи, які зустрічаються лише один раз:")
print(*unique_elements)
