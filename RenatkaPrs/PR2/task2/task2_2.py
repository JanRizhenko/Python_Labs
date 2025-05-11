num = int(input("Введіть температуру (ціле число): "))

if num > 0:
    print(f"{num}° — це {num} градусів тепла.")
elif num < 0:
    print(f"{num}° — це {abs(num)} градусів морозу.")
else:
    print("Температура близька до нуля.")