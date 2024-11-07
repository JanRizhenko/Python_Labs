import math

def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

cathetus1 = float(input("Введіть перший катет для першого трикутника: "))
cathetus2 = float(input("Введіть другий катет для першого трикутника: "))
hyp1 = round(hypotenuse(cathetus1, cathetus2), 3)

cathetus3 = float(input("Введіть перший катет для другого трикутника: "))
cathetus4 = float(input("Введіть другий катет для другого трикутника: "))
hyp2 = round(hypotenuse(cathetus3, cathetus4), 3)

print(f"Гіпотенуза першого трикутника: {hyp1}")
print(f"Гіпотенуза другого трикутника: {hyp2}")

if hyp1 > hyp2:
    print("Гіпотенуза першого трикутника більша.")
elif hyp1 < hyp2:
    print("Гіпотенуза другого трикутника більша.")
else:
    print("Гіпотенузи однакові.")