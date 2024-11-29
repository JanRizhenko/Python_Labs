import re

def count_words_starting_with_letter(text, letter):
    letter = letter.lower()
    count = 0

    words = text.split()
    for word in words:
        cleaned_word = re.sub(r'^[^\wА-Яа-я]+', '', word)
        if cleaned_word.lower().startswith(letter):
            count += 1

    return count

input_text = """Розцвітають квіти в Україні,
В небі синьо, в траві зелено.
Вітри дмуть, пташки співають,
Сонце гріє, все навколо.
Від Карпат до Криму простягнулись,
Сади, поля — !!!краса безмежна.
Любов в серцях наших горить,
Квіти в Україні — наш вічний спів."""
print(input_text)

input_letter = input("Введіть літеру: ")

result = count_words_starting_with_letter(input_text, input_letter)
print(f"Кількість слів, що починаються з літери '{input_letter}': {result}")