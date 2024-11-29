import math


def calculate_quadrilateral_area(X, Y, Z, T):
    if X <= 0 or Y <= 0 or Z <= 0 or T <= 0:
        raise ValueError("Усі сторони повинні бути додатними числами.")

    # Площа першого трикутника зі сторонами X і Y (прямокутний трикутник)
    area1 = 0.5 * X * Y
    # Обчислення діагоналі між точками X і Y за теоремою Піфагора
    diagonal = math.sqrt(X ** 2 + Y ** 2)

    # Обчислення площі другого трикутника за формулою Герона

    s = (diagonal + Z + T) / 2
    # Перевірка, чи не є площа другого трикутника від'ємною (негативний корінь)
    if s <= diagonal or s <= Z or s <= T:
        raise ValueError("Неможливо побудувати трикутник з такими сторонами.")
    # Перевірка підкорінної частини (що під квадратним коренем не виходить від'ємне число)
    area2_check = s * (s - diagonal) * (s - Z) * (s - T)
    if area2_check < 0:
        raise ValueError("Неможливо побудувати трикутник з такими сторонами. Значення під коренем від'ємне.")
    area2 = math.sqrt(area2_check)

    total_area = area1 + area2
    return total_area

try:
    X = float(input("Введіть довжину X: "))
    Y = float(input("Введіть довжину Y: "))
    Z = float(input("Введіть довжину Z: "))
    T = float(input("Введіть довжину T: "))

    print(f"Площа чотирикутника: {round(calculate_quadrilateral_area(X, Y, Z, T), 3)}")
except ValueError as e:
    print(f"Помилка: {e}")