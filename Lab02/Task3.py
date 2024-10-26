purchase_amount = float(input("Введіть вартість покупки: "))
discount = 0.05 if purchase_amount > 1000 else 0.03 if purchase_amount > 500 else 0
total_amount = purchase_amount * (1 - discount)
print("Сума зі знижкою:", round(total_amount, 3), "грн")