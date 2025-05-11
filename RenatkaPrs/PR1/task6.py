import math

r = float(input("Введіть радіус кола: "))
alpha = float(input("Введіть центральний кут (в градусах): "))

s = (math.pi * r**2 * alpha) / 360

s = round(s, 2)

print("Площа кругового сектора:", s)
