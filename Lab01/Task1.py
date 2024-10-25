# Функція, що дозволяє вводити int та float
def convert_input(value):
    try:
        return int(value)
    except ValueError:
        return float(value)

# Створення змінних та надання їм float або int значень
a = convert_input(input("Введіть значення для змінної a: "))
b = convert_input(input("Введіть значення для змінної b: "))
c = convert_input(input("Введіть значення для змінної c: "))
d = convert_input(input("Введіть значення для змінної d: "))

print("Значення змінних:")
print("a =", a, "Тип:", type(a))
print("b =", b, "Тип:", type(b))
print("c =", c, "Тип:", type(c))
print("d =", d, "Тип:", type(d))

# Дії над числами, зазначені в завданні 2
results = [
    round(a + b, 3), #додавання
    round(c - b, 3), #віднімання
    round(d * a, 3), #множення
    round(b / d, 3), #ділення
    round(c ** a, 3), #піднесення до ступеня
    round(a // a, 3), #цілочисленне ділення
    round(d % b, 3) #остача від ділення двох чисел
]

# Результати
print("Результати операцій:")
print(f"{a} + {b} = {results[0]} (додавання)")
print(f"{c} - {b} = {results[1]} (віднімання)")
print(f"{d} * {a} = {results[2]} (множення)")
print(f"{b} / {d} = {results[3]} (ділення)")
print(f"{c} ** {a} = {results[4]} (піднесення до ступеня)")
print(f"{a} // {a} = {results[5]} (цілочисленне ділення)")
print(f"{d} % {b} = {results[6]} (остача від ділення)")

# Кількість елементів у списку results
num_elements = len(results)
print("\nКількість елементів у списку результатів:", num_elements)

# Виведення всіх парних елементів списку
even_elements = [elem for elem in results if elem % 2 == 0]
if not even_elements:
    print("Парні елементи у списку відсутні.")
else:
    print("Парні елементи у списку результатів:", even_elements)

print("\nСписок елементів:", results)

# Обмін місцями другого та п'ятого елемента
results[1], results[4] = results[4], results[1]
print("Отриманий список після обміну місцями другого та п’ятого елемента:", results)

# Завдання 5
name = input("Введіть ваше прізвище та ім'я: ")
print("\nВиконавець лабораторної роботи:", name)
print("У цій лабораторній роботі ми ознайомились з основами мови Python.")
print("Ми виконали арифметичні операції, обробили результати та працювали зі списками.")
print("Ця лабораторна робота дозволила зрозуміти, як працювати з даними в Python.")