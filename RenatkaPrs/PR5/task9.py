text = input("Введіть рядок: ")

filtered = ''.join(c for c in text if ord(c) >= ord('A'))
print("Результат:", filtered)
