import time
import os

def add_guest_to_book(guest_name, file_name="guest_book.txt"):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    greeting = f"Привіт, {guest_name}! (Додано: {current_time})"
    print(greeting)
    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{greeting}\n")
    update_last_modified_time(file_name)

def update_last_modified_time(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()
        last_modified = f"Останні зміни: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
        if len(lines) > 0 and "Останні зміни:" in lines[-1]:
            lines[-1] = last_modified
        else:
            lines.append(last_modified)
            lines.append("-" * 50 + "\n")
        with open(file_name, "w", encoding="utf-8") as file:
            file.writelines(lines)

print("Введіть імена гостей. Для завершення введіть 'вихід'.")
while True:
    guest_name = input("Введіть ім'я: ").strip()
    if guest_name.lower() == 'вихід':
        print("Роботу завершено.")
        break
    elif guest_name:
        add_guest_to_book(guest_name)