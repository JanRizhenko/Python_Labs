text = "Це текст, в якому потрібно видалити всі літери 'о'."
print("Текст:\n",text)
new_text = text.replace("о", "")
deleted_count = len(text) - len(new_text)

print("\nРезультат після видалення літер 'о':\n", new_text)
print("\nКількість видалених символів 'о':", deleted_count)