n = int(input("Введіть число n: "))

found = False
for i in range(1, 150):
    square = i ** 2
    if square > n:
        print("Перше число більше n:", square,"\n Число, що в квадраті більше за n: ",i)
        found = True
        break

if not found:
    print("Не знайдено число більше n у межах від 1 до 150.")