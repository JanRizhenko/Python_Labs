text = input("Введіть рядок, що містить цифри: ")

digit_counts = {}

for char in text:
    if char.isdigit():
        digit_counts[char] = digit_counts.get(char, 0) + 1

print("Цифри, що трапляються рівно два рази:")
for digit, count in digit_counts.items():
    if count == 2:
        print(digit, end=' ')
