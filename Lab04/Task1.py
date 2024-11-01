numbers = list(map(int, input("Введіть список чисел через пробіл: ").split()))

max_element = max(numbers)
print("Максимальний елемент:", max_element)

print("Список у зворотному порядку:", numbers[::-1])