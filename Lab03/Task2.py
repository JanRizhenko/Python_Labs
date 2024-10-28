def replace_colons_with_percent(text):
    # Підраховуємо кількість замін
    replacement_count = text.count(":")
    # Замінюємо всі двокрапки на відсотки
    new_text = text.replace(":", "%")
    return new_text, replacement_count

input_text = """Зустрічались ми знову і знову:
У снах, у мріях, у хвилинах щастя:
Там, де зірки падали з небес:
Слідом за нами, знов і знову:
Так, як серце прагне без кінця:
Світло йде, мов промінь ясний:
Любов – це сила й кохання:"""
print("Текст до заміни:\n",input_text)

# Викликаємо функцію
new_text, count = replace_colons_with_percent(input_text)

print("\nТекст після заміни:\n", new_text)
print("Кількість замін:", count)