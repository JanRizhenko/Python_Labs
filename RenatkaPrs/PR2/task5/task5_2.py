grade = int(input("Введіть оцінку студента (від 1 до 12): "))

if grade >= 10:
    print("Відмінно")
elif grade >= 7:
    print("Добре")
elif grade >= 4:
    print("Задовільно")
else:
    print("Незадовільно")