base_triangle = float(input("Введіть основу трикутника: "))
height = float(input("Введіть висоту трикутника: "))
area = 0.5 * base_triangle * height
print("Площа: ", area)
if int(area) % 2 == 0:
    print("Площа / 2:", area / 2)
else:
    print("Не можу ділити на 2!")