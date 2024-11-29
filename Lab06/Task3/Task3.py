with open("learning_python.txt", "w", encoding="utf-8") as file:
    file.write("Python можна використати для аналізу даних.\n")
    file.write("Python можна використати для створення веб-додатків.\n")
    file.write("Python можна використати для машинного навчання.\n")
    file.write("Python можна використати для автоматизації задач.\n")

filename = "learning_python.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file.readlines()]

    sorted_lines = sorted(lines, key=len, reverse=True)

    print("Вміст файлу, відсортований за довжиною рядків:")
    for line in sorted_lines:
        print(line)

except FileNotFoundError:
    print(f"Файл '{filename}' не знайдено. Будь ласка, створіть його спочатку.")

print(f"Файл '{filename}' створено та заповнено.")