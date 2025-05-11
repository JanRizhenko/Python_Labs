length = float(input("Введіть довжину прямокутника: "))
width = float(input("Введіть ширину прямокутника: "))

perimeter = 2 * (length + width)
area = length * width


area = round(area, 2)
perimeter = round(perimeter, 2)

print("Периметр прямокутника:", perimeter)
print("Площа прямокутника:", area)
