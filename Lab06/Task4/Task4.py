import os

original_file = "learning_python.txt"

new_directory = "new_directory"
os.makedirs(new_directory, exist_ok=True)

true_file = os.path.join(new_directory, "true_statements.txt")
false_file = os.path.join(new_directory, "false_statements.txt")

modified_file = os.path.join(new_directory, "learning_c.txt")

with open(original_file, "r", encoding="utf-8") as infile, \
     open(modified_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        modified_line = line.replace("Python", "C")
        outfile.write(modified_line)

print(f"Файл зі зміненими рядками створено: {modified_file}")

with open(modified_file, "r", encoding="utf-8") as infile, \
     open(true_file, "w", encoding="utf-8") as true_outfile, \
     open(false_file, "w", encoding="utf-8") as false_outfile:

    for line in infile:
        print(f"Чи актуальне це твердження? {line.strip()}")
        user_response = input("Введіть 'y' для так або 'n' для ні: ").strip().lower()

        if user_response == "y":
            true_outfile.write(line)
        elif user_response == "n":
            false_outfile.write(line)
        else:
            print("Некоректна відповідь. Пропускаємо це твердження.")