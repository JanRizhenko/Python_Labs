text = "Це текст, в якому будемо рахувати, скільки разів зустрічається слово 'текст'."
word_to_find = input("Яке слово хочемо знайти? ").strip()
print("Початковий текст:\n", text, "\n")

word_count = text.lower().count(word_to_find.lower())

print(f"Кількість входжень слова '{word_to_find}':", word_count, "\n")