surname = "Рупета"
text = input("Введіть рядок: ")
count = 0

for letter in surname.lower():
    count += text.lower().count(letter)

print(f"Загальна кількість входжень символів прізвища '{surname}': {count}")
