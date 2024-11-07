import math


def calculate_quadrilateral_area(X, Y, Z, T):
    # Площа першого трикутника зі сторонами X і Y (прямокутний трикутник)
    area1 = 0.5 * X * Y
    # Обчислення діагоналі між точками X і Y за теоремою Піфагора
    diagonal = math.sqrt(X ** 2 + Y ** 2)

    # Обчислення площі другого трикутника за формулою Герона
    s = (diagonal + Z + T) / 2  # Півпериметр трикутника
    area2 = math.sqrt(s * (s - diagonal) * (s - Z) * (s - T))
    # Загальна площа чотирикутника
    total_area = area1 + area2
    return total_area

X = float(input("Введіть довжину X: "))
Y = float(input("Введіть довжину Y: "))
Z = float(input("Введіть довжину Z: "))
T = float(input("Введіть довжину T: "))

print(f"Площа чотирикутника: {round(calculate_quadrilateral_area(X, Y, Z, T), 3)}")