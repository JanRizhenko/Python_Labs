text = input("Введіть текст: ")
letter = input("Введіть літеру: ").lower()

words = text.split()
count = 0

for word in words:
    if len(word) >= 1 and word[0].lower() == letter and word[-1].lower() == letter:
        count += 1

print("Кількість слів, що починаються і закінчуються літерою", letter, ":", count)
