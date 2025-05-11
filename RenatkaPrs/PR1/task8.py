dev_hours = float(input("Введіть кількість годин, витрачених на розробку програмного продукту: "))
hourly_rate = float(input("Введіть погодинну оплату програміста: "))

salary = round(dev_hours * hourly_rate, 2)

print("Заробітна плата програміста:", salary)