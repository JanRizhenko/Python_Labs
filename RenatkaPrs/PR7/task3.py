def rectangle_area(a, b):
    return a * b

length = float(input("Введіть довжину прямокутника: "))
width = float(input("Введіть ширину прямокутника: "))

area = rectangle_area(length, width)

print("Площа прямокутника:", area)
