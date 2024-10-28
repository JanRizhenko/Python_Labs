text = "Alice and Bob went to Paris. They visited the Eiffel Tower and enjoyed their trip."
print("Початковий текст:\n", text, "\n")

capitalized_words = [word for word in text.split() if word.istitle()]

print("Імена і власні назви:", capitalized_words, "\n")