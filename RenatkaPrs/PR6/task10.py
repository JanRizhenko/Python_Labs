heights = list(map(int, input("Введіть зріст учнів (спаданням): ").split()))

new_height = int(input("Введіть зріст нового учня: "))

position = 1
for height in heights:
    if new_height <= height:
        position += 1
    else:
        break

print("Новий учень має зайняти позицію:", position)
