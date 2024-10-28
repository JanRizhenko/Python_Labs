text = "This is another example sentence to calculate the number of consonants."
print("Початковий текст:\n", text, "\n")

consonants = "bcdfghjklmnpqrstvwxyz"

consonant_count = sum(1 for char in text.lower() if char in consonants)

print("Кількість приголосних літер:", consonant_count, "\n")