surname = input("Прізвище: ")
name = input("Ім’я: ")
patronymic = input("По батькові: ")

initials = f"{name[0].upper()}.{patronymic[0].upper()}.{surname}"
print(initials)