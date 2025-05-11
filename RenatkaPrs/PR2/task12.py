number = int(input("Введіть кількість гривень: "))

last_digit = number % 10
last_two_digits = number % 100

if 11 <= last_two_digits <= 14:
    word = "гривень"
elif last_digit == 1:
    word = "гривня"
elif 2 <= last_digit <= 4:
    word = "гривні"
else:
    word = "гривень"

# Виводимо результат
print(f"{number} {word}")
