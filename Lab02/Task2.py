year = int(input("Рік:"))
is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
days_in_year = 366 if is_leap_year else 365
print("Кількість днів у році:", days_in_year)