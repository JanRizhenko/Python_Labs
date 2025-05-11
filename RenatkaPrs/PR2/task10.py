import math

r = abs(float(input("Введіть радіус r: ")))

n = int(input("Оберіть номер послуги: \n"
              "1 - довжина кола\n"
              "2 - площа круга\n"
              "3 - об’єм кулі\n"
              "4 - площа поверхні кулі\n"))

if n == 1:
    result = 2 * math.pi * r
    print("Довжина кола:", result)
elif n == 2:
    result = math.pi * r**2
    print("Площа круга:", result)
elif n == 3:
    result = (4/3) * math.pi * r**3
    print("Об’єм кулі:", result)
elif n == 4:
    result = 4 * math.pi * r**2
    print("Площа поверхні кулі:", result)
else:
    print("Невірний номер послуги. Введіть число від 1 до 4.")
