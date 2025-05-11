month = int(input("Введіть номер місяця народження (1-12): "))
day = int(input("Введіть день народження (1-31): "))

if (month == 3 and day >= 21) or (month == 4 and day <= 20):
    zodiac = "Овен"
elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
    zodiac = "Телець"
elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
    zodiac = "Близнюки"
elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
    zodiac = "Рак"
elif (month == 7 and day >= 23) or (month == 8 and day <= 23):
    zodiac = "Лев"
elif (month == 8 and day >= 24) or (month == 9 and day <= 22):
    zodiac = "Діва"
elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
    zodiac = "Терези"
elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
    zodiac = "Скорпіон"
elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
    zodiac = "Стрілець"
elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
    zodiac = "Козоріг"
elif (month == 1 and day >= 21) or (month == 2 and day <= 20):
    zodiac = "Водолій"
elif (month == 2 and day >= 21) or (month == 3 and day <= 20):
    zodiac = "Риби"
else:
    zodiac = "Невірна дата"

print(f"Ваш знак зодіаку: {zodiac}")
