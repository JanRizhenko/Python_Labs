name = "Рената"
symbol = input("Введіть символ для перевірки: ")

if symbol in name:
    print(f"Символ '{symbol}' є частиною ім'я {name}.")
else:
    print(f"Символ '{symbol}' не є частиною ім'я {name}.")
