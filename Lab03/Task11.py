text = "This is an example sentence to calculate the number of vowels."
print("Початковий текст:\n", text, "\n")

vowels = "aeiou"

vowel_count = sum(1 for char in text.lower() if char in vowels)

print("Кількість голосних літер:", vowel_count, "\n")