def is_inside_circle(x, y, a, b, R):
    return (x - a)**2 + (y - b)**2 < R**2

a = float(input("Введіть координату a центру кола: "))
b = float(input("Введіть координату b центру кола: "))
R = float(input("Введіть радіус кола R: "))

points = [
    ('P', float(input("Введіть р1: ")), float(input("Введіть р2: "))),
    ('F', float(input("Введіть f1: ")), float(input("Введіть f2: "))),
    ('L', float(input("Введіть l1: ")), float(input("Введіть l2: ")))
]

count_inside = 0
for name, x, y in points:
    if is_inside_circle(x, y, a, b, R):
        print(f"Точка {name} знаходиться всередині кола")
        count_inside += 1
    else:
        print(f"Точка {name} не знаходиться всередині кола")

print(f"Кількість точок, що лежать всередині кола: {count_inside}")