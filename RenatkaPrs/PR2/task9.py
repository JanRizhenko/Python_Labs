a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

print("1. Обидва додатні:", a > 0 and b > 0)

print("2. Одне непарне і ділиться на 7:",
      (a % 2 != 0 and a % 7 == 0) or (b % 2 != 0 and b % 7 == 0))

print("3. Одне >0 і <10, інше <0 і >-10:",
      (a > 0 and a < 10 and b < 0 and b > -10) or
      (b > 0 and b < 10 and a < 0 and a > -10))

print("4. Хоча б одне <5:", a < 5 or b < 5)

print("5. Обидва >10 і <20:", a > 10 and a < 20 and b > 10 and b < 20)

print("6. Одне парне і >20, інше непарне і <10:",
      (a % 2 == 0 and a > 20 and b % 2 != 0 and b < 10) or
      (b % 2 == 0 and b > 20 and a % 2 != 0 and a < 10))

print("7. Сума парна або одне <0:", (a + b) % 2 == 0 or a < 0 or b < 0)

print("8. Обидва <0 або одне >100:", (a < 0 and b < 0) or a > 100 or b > 100)

print("9. Сума = 100 або одне <0:", (a + b == 100) or a < 0 or b < 0)

print("10. Одне кратне 3 або кратне 5:",
      (a % 3 == 0 or a % 5 == 0) or (b % 3 == 0 or b % 5 == 0))
