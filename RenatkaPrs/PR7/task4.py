import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

catet1 = float(input("Введіть довжину першого катета: "))
catet2 = float(input("Введіть довжину другого катета: "))

hyp = hypotenuse(catet1, catet2)

print(f"Довжина гіпотенузи: {hyp}")
