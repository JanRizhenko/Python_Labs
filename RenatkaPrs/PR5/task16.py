text = input("Введіть рядок: ")

result = ''
for char in text:
    if not ('0' <= char <= '9'):
        result += char

print(result)
