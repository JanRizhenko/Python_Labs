user_input = input("Введіть цілі числа через пробіл: ")

numbers = list(map(int, user_input.split()))

print("Елементи у зворотному порядку:")
for num in reversed(numbers):
    print(num)