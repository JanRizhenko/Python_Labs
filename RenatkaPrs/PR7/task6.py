import math

def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

a = float(input("Введіть першу сторону трикутника: "))
b = float(input("Введіть другу сторону трикутника: "))
c = float(input("Введіть третю сторону трикутника: "))

if is_right_triangle(a, b, c):
    print("Трикутник є прямокутним.")
else:
    print("Трикутник не є прямокутним.")
