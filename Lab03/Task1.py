def count_words_starting_with_letter(text, letter):
    # Розбиваємо рядок на слова
    words = text.split()
    # Приводимо літеру до нижнього регістру
    letter = letter.lower()
    # Рахуємо кількість слів, що починаються з заданої літери
    count = sum(1 for word in words if word.lower().startswith(letter))
    return count

input_text = """Розцвітають квіти в Україні,
В небі синьо, в траві зелено.
Вітри дмуть, пташки співають,
Сонце гріє, все навколо.
Від Карпат до Криму простягнулись,
Сади, поля — краса безмежна.
Любов в серцях наших горить,
Квіти в Україні — наш вічний спів."""
print(input_text)

input_letter = input("Введіть літеру: ")

result = count_words_starting_with_letter(input_text, input_letter)
print(f"Кількість слів, що починаються з літери '{input_letter}': {result}")