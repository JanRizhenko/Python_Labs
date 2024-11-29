text = """На широкому лузі зеленому пасуться коні. А далі, де сонце сходить, козаки на конях у дозорі."""

print("Текст:\n",text)
count_replacements = text.count('а') + text.count('A')
text = text.replace('а', 'о')
text = text.replace('A', 'O')

total_characters = len(text)

print("\nТекст після замін:\n", text)
print("\nКількість замін:", count_replacements)
print("Кількість символів в рядку:", total_characters)