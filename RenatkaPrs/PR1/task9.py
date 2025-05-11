import cmath

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

discriminant = cmath.sqrt(b**2 - 4*a*c)

x1 = (-b + discriminant) / (2 * a)
x2 = (-b - discriminant) / (2 * a)

print("Корінь x1:", x1)
print("Корінь x2:", x2)
